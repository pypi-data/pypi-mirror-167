#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/8/26 10:48
# @Author  : jeremy
# @File    : bootmain.py



import sys
from ui.bootview import Ui_boot_MainWindow
from PySide6.QtWidgets import QWidget,QApplication, QMainWindow,QMessageBox,QFileDialog,QButtonGroup
import os
import serial
import serial.tools.list_ports
import traceback
from PySide6.QtCore import QTimer,Qt,Signal
from PySide6.QtGui import QTextCursor
import time
from threading import Thread
from datetime import datetime
# from numba import jit,typed
# from qt_material import apply_stylesheet
from diskcache import Cache
import crcmod.predefined


class CRCGenerator(object):
    def __init__(self):
    # crcmod is a module for crc algrithms inpython
    # It concludes the modules likecrc-8,crc-16...
    # you can refer to the website below:
    # http://crcmod.sourceforge.net/crcmod.predefined.html
        self.module = 'crc-16-maxim'#crc-8 crc-16-usb crc-32-mpeg 此三个分别对应当前三种模式
    def config_crc(self,i):
        if i==1:
            self.crc = crcmod.predefined.Crc('crc-8')
        elif i==2:
            self.crc = crcmod.predefined.Crc('crc-16')
        elif i==3:
            self.crc = crcmod.predefined.Crc('crc-32-mpeg')



    def create(self, input,lenn):
        # t1 = time.time()
        hexData=bytes(input[0:lenn])
        #0.015902280807495117s

#-0.991527
        # print hexData
        # hexData = input.replace(' ', '').replace('0x', '').replace(',', '')
        # hexData = binascii.unhexlify(hexData)

        self.crc.crcValue=0

        self.crc.update(hexData)
        result = self.crc.crcValue
        # print(time.time()-t1)

        return result

# if __name__ == "__main__":
#     crc = CRCGenerator()
#     crc.config_crc(2)
#     crc.create('01 02 03')

# 127999
# 0x39b1

# 127999
# 0x34b9




#

# from PySide6.QtGui import QTextCursor
# @jit(nopython=True) # jit，numba装饰器中的一种
#
# def crc16_checkte(p, len):
#
#
#     wCRCin = 0x0
#     wCPoly = 0x1021
#     wChar = 0
#     for i in range(len):
#         pidx = (i & 0xFFFFFFFC) | (3 - (i & 3))
#
#         y = 0
#         x=p[pidx]
#
#         for i in range(8):
#
#             if (0 != (x & (1 << i))):
#                 # print(i)
#                 # print(1<<(7-i))
#                 y |= 1 << (7 - i)
#
#         wChar =y# self.invert_8(p[pidx])
#         wCRCin ^= (wChar << 8)
#
#         for j in range(8):
#             if (0x8000 == (wCRCin & 0x8000)):
#                 wCRCin = (wCRCin << 1) ^ wCPoly
#             else:
#                 wCRCin <<= 1
#     y = 0
#     x=wCRCin
#
#     for i in range(16):
#
#         if (0 != (x & (1 << i))):
#             # print(i)
#             # print(1<<(7-i))
#             y |= 1 << (15 - i)
#     return y
    # return self.invert_16(wCRCin)
    # return ii


help_text="""
1.扫描并打开串口
2.打开HEX文件
3.选择下载模式
4.选择擦除位置
5.选择升级后是否立即执行APP程序
6.设置APP起始地址
"""

class Serial_boot(QMainWindow, Ui_boot_MainWindow):
    # 定义一个信号
    progressmsg = Signal(int)
    informationmsg = Signal(str,classmethod)
    def __init__(self):
        super(Serial_boot, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("I2C Download demo0.90")
        self.ser = serial.Serial()
        self.ser.timeout = 2
        self.scan_serialButton.clicked.connect(self.scan_port)
        self.serial_port=0
        self.check_is_updatesucess_Button.clicked.connect(self.check_app_version)
        self.open_hexfile_Button.clicked.connect(self.readIAPhexfile)
        self.clean_informaiton_Button.clicked.connect(self.information_textEdit_clear)
        self.clean_informaiton_Button.setText("清除信息栏")
        self.iap_usermanual_TextEdit.setPlainText(help_text)
        self.iap_usermanual_TextEdit.setStyleSheet("{background-color:#fff}")

        self.flashcode = 0

        self.psendbuff = [255] *320
        # 定时器接收数据
        # self.timer = QTimer(self)
        # self.timer.timeout.connect(self.data_receive)
        self.progress_value=0
        self.hexfile_isopen = False
        self.update_app_Button.clicked.connect(self.II2Cdownload)
        self.delay_time = QTimer(self)
        self.delay_tt=0
        self.is_download_work=0
        self.hex_crc_code=0
        self.text_num = 0
        self.update_progressBar.setVisible(False)
        self.update_progressBar.setValue(0)
        self.update_sucess_num=0
        self.progressmsg.connect(self.progessbarshow)
        self.informationmsg.connect(self.information_msg_show)
        self.iic_uart_mode=QButtonGroup(self)
        self.iic_uart_mode.addButton(self.i2c_mode__radioButton)
        self.iic_uart_mode.addButton(self.uart_mode__radioButton)
        # self.i2c_mode__radioButton.setChecked(True)
        self.uart_mode__radioButton.setChecked(True)
        self.all_part_radio_group=QButtonGroup()
        self.all_part_radio_group.addButton(self.update_appall_radio)
        self.all_part_radio_group.addButton(self.update_app_part_radio)

        self.update_app_part_radio.setChecked(True)
        self.update_and_run_checkbutton.setChecked(True)
        self.adress_Edit.editingFinished.connect(self.address_save)


        self.delay_time.start(100)#10ms
        self.delay_time.timeout.connect(self.delay_)
        self.information_textEdit.setTextColor(Qt.black)

        #
        self.cache_path="C:/Users/"+os.environ[ 'USERNAME' ]+"/Documents/sinomcu"
        self.start_address=0

        self.crc = CRCGenerator()
        self.crc.config_crc(2)
        self.init_cache=Cache(self.cache_path)
        self.scan_port_staus=0

        self.scan_port()
        self.address_get()

        self.autoupdate_app_Button.clicked.connect(self.auto_update_test_use)
        self.autoupdate_staus=0
        self.autoupdate_download_staus = 0
        self.fail_time=0
        #print(type(Qt.black))
    def auto_update_test_use(self):
        if self.autoupdate_staus==0:
            self.autoupdate_app_Button.setText("停止自动升级")
            self.autoupdate_staus =1
            if self.autoupdate_download_staus ==0:
                t1 = Thread(target=self.auto_update_test_loop, args=())

                t1.start()
        else:
            self.autoupdate_app_Button.setText("自动连续升级")
            self.autoupdate_staus =0
            pass
    def auto_update_test_loop(self):
        while self.autoupdate_staus==1:
            self.autoupdate_download_staus = 1
            time.sleep(3)
            self.I2Cdownloadr()
            self.autoupdate_download_staus = 0
            pass


    def address_get(self):
        address=self.init_cache.get("address")
        if address==None:
            pass
        else:
            self.adress_Edit.setText(address)
    def address_save(self):
        self.init_cache.set("address",str(self.adress_Edit.text()),expire=88864,read=True,tag="data",retry=True)


    def path_get(self,key):
        return self.init_cache.get(key, default=None,  expire_time=False, tag=False)

    def path_set(self,key,value):
        self.init_cache.set(key,value,expire=88864,read=True,tag="data",retry=True)
    def progessbarshow(self,i):
        if i==0:
            self.update_progressBar.setVisible(True)
        elif i==100:
            self.update_progressBar.setVisible(False)
        self.update_progressBar.setValue(i)
    def progressbar_emit(self,i):
        self.progressmsg.emit(i)
    def information_textEdit_clear(self):
        self.information_textEdit.clear()
        self.text_num=0
        # self.tset_send()

    def information_show(self,text,color):
        self.informationmsg.emit(text,color)
    def information_msg_show(self,text,color):
        if color==Qt.black:#Qt.darkBlue
            self.information_textEdit.setTextColor(color)
            self.information_textEdit.append("%06d：" % self.text_num+text+"\r\n")
            self.information_textEdit.moveCursor(QTextCursor.End)
        else:
            self.information_textEdit.setTextColor(color)
            self.information_textEdit.append("%06d：" % self.text_num+text+"\r\n")
            self.information_textEdit.moveCursor(QTextCursor.End)
            # self.information_textEdit.setTextColor(Qt.black)
        self.text_num = self.text_num + 1
    # def information_show(self,text,color):
    #
    #     if color==Qt.black:#Qt.darkBlue
    #         self.information_textEdit.setTextColor(color)
    #         self.information_textEdit.append("%06d：" % self.text_num+text+"\r\n")
    #     else:
    #         self.information_textEdit.setTextColor(color)
    #         self.information_textEdit.append("%06d：" % self.text_num+text+"\r\n")
    #         # self.information_textEdit.setTextColor(Qt.black)
    #     self.text_num = self.text_num + 1


    def delay_(self):
        self.delay_tt=self.delay_tt-1

        if self.delay_tt<0:
            self.delay_tt=0


    def scan_port(self):
        if self.scan_port_staus==0:
            self.scan_port_staus =1
            if self.serial_port == 0:
                t1 = Thread(target=self.scan_portr, args=())

                t1.start()
            else:
                if self.ser.isOpen():
                    self.ser.close()
                    self.serial_deviceBox.clear()
                    self.scan_serialButton.setText("扫描并打开串口")
                    self.information_show("烧录设备已断开", Qt.black)
                    self.serial_port = 0
                    self.scan_port_staus = 0

        else:
            self.information_show("正在扫描中，请稍等~", Qt.blue)





    def scan_portr(self):

        # 检测所有存在的串口，将信息存储在字典中
        self.Com_Dict = {}
        port_list = list(serial.tools.list_ports.comports())
        # print(port_list)
        # self.s1__box_2.clear()
        self.serial_deviceBox.clear()
        if len(port_list)!=0:
            for port in port_list:

                self.Com_Dict["%s" % port[0]] = "%s" % port[1]

                if self.ser.isOpen():

                    self.ser.close()
                    if self.port_open(port[0]):
                        self.serial_deviceBox.addItem(port[0])
                        self.scan_serialButton.setText("关闭串口")
                        self.information_show('与烧录器连接成功!', Qt.black)
                        self.serial_port = 1

                        break
                else:
                    # 待实现握手打开串口功能
                    if self.port_open(port[0]):
                        self.serial_deviceBox.addItem(port[0])
                        self.scan_serialButton.setText("关闭串口")
                        self.information_show('与烧录器连接成功!', Qt.black)
                        self.serial_port = 1
                        break
            if self.serial_port == 0:


                self.information_show('与烧录器连接失败，请重新插拔设备并重试连接!', Qt.red)

            # print(self.Com_Dict)
            # # self.s1__box_2.addItem(port[0])
        else:

            self.serial_deviceBox.addItem('no com device')
        self.scan_port_staus = 0

        #
        # if len(self.Com_Dict) == 0:
        #     print(0)
            # self.state_label.setText(" 无串口")

    # 打开串口
    def port_close(self):
        self.ser.close()
    def port_open(self,com):
        self.ser.port = com
        self.ser.baudrate = 921600#115200
        self.ser.bytesize = 8
        self.ser.stopbits = 1
        self.ser.parity = "N"

        try:
            self.ser.open()

            if self.check_boot_versionr():

                return True
            else:

                self.ser.close()
                return False
            #self.timer.start(2)

        except:
            print(traceback.format_exc())

            #QMessageBox.critical(self, "Port Error", "此串口不能被打开！")
            return False
        return False

        # 打开串口接收定时器，周期为2ms

        # t1 = threading.Thread(target=self.run, args=("t1",))  # 后期采用多线程实现1MHz频率的数据接收
        # t1.setDaemon(True)
        # t1.start()

    # 串口信息

    def checksum(self,p, len, offset=0):
        #return self.uchar_checksum(p)
        sum = 0
        i = offset
        for i in range(len):

            sum =sum +p[i]
            if sum>255:
                sum=sum-256
        return sum#&0xff

    def check_app_version(self):
        if self.is_download_work == 0:

            if self.hexfile_isopen == True:
                t1 = Thread(target=self.check_app_versionr, args=())

                t1.start()
            else:

                self.information_show('请先打开HEX文件', Qt.red)
                return False
        else:

            self.information_show('程序升级正在进行，请耐心等待!', Qt.black)



    def check_app_versionr(self):
        if self.check_boot_versionr():
            pass
        else:
            self.information_show('请重新连接设备！', Qt.red)
            return False
        if self.uart_mode__radioButton.isChecked():
            self.cmd_shell = "7C 01 FE FF 7E"
            if self.ser.isOpen():
                pass
            else:
                self.information_show('请先打开串口！', Qt.red)
                return False

            try:
                num = self.ser.inWaiting()
                # print(num)
            except:
                # self.port_close()
                return False
            if num > 0:
                data = self.ser.read(num)
                # print(data)

            self.send_data(self.cmd_shell)
            self.delay_tt = 5
            while self.ser.inWaiting() < 9:  # 无限循环...

                if self.delay_tt == 0:
                    self.information_show('与烧录器连接失败，请重新插拔设备后再次尝试!', Qt.red)
                    #
                    # self.iapI2cEnterFlag = True
                    return False
            data = self.ser.read(10)
            out_s = ""
            if ((0x7C != data[0]) or (0x01 != data[1]) or (0x55 != data[3])):
                # for i in range(0, len(data)):
                #     out_s = out_s + '{:02X}'.format(data[i]) + ' '
                # print(out_s)

                self.information_show('通信建立失败，请重新连接!', Qt.red)

                return False

            self.bootloader_versionEdit.setText("Bootloader版本号：V{:02X}".format(data[7]))
            if (0x55 != data[4]):
                self.information_show('当前APP区无程序！', Qt.red)


            else:
                if (self.hex_crc_code == (data[5] << 8 | data[6])):

                    self.information_show('APP程序已经烧录成功！！！', Qt.black)
                else:
                    if ((data[5] << 8 | data[6]) == 0):
                        self.information_show('APP程序烧录过程中中断，程序烧录失败,校验码为：0x0000！！！', Qt.red)

                    else:
                        self.information_show('APP校验码错误，程序烧录失败，校验码为：0x{:02X}{:02X}'.format(data[5], data[6]), Qt.red)
        else:
            self.cmd_shell = "FA 01 34 00 06 CB 00 7E"
            if self.ser.isOpen():
                pass
            else:
                self.information_show('请先打开串口！', Qt.red)
                return False

            try:
                num = self.ser.inWaiting()
                # print(num)
            except:
                # self.port_close()
                return False
            if num > 0:
                data = self.ser.read(num)
                # print(data)

            self.send_data(self.cmd_shell)
            self.delay_tt = 5
            while self.ser.inWaiting() < 12:  # 无限循环...

                if self.delay_tt == 0:
                    self.information_show('与烧录器连接失败，请重新插拔设备后再次尝试!', Qt.red)
                    #
                    # self.iapI2cEnterFlag = True
                    return False
            data = self.ser.read(12)
            out_s = ""
            if ((0xFA != data[0]) or (0x00 != data[1]) or (0x34 != data[2]) or (0x55 != data[5])):
                # for i in range(0, len(data)):
                #     out_s = out_s + '{:02X}'.format(data[i]) + ' '
                # print(out_s)

                self.information_show('通信建立失败，请重新连接!', Qt.red)

                return False

            self.bootloader_versionEdit.setText("Bootloader版本号：V{:02X}".format(data[6]))
            if (0x55 != data[7]):
                self.information_show('当前APP区无程序！', Qt.red)


            else:
                if (self.hex_crc_code == (data[8] << 8 | data[9])):

                    self.information_show('APP程序已经烧录成功！！！', Qt.black)
                else:
                    if ((data[8] << 8 | data[9]) == 0):
                        self.information_show('APP程序烧录过程中中断，程序烧录失败,校验码为：0x0000！！！', Qt.red)

                    else:
                        self.information_show('APP校验码错误，程序烧录失败，校验码为：0x{:02X}{:02X}'.format(data[8], data[9]), Qt.red)


    def check_boot_versionr(self):

        if self.uart_mode__radioButton.isChecked():
            self.bootloader_versionEdit.setText("Bootloader版本号：    ")
            self.cmd_shell = "7C 01 FE FF 7E"

            try:
                num = self.ser.inWaiting()
            except:
                self.port_close()
                return False
            if num > 0:
                data = self.ser.read(num)

            self.send_data(self.cmd_shell)

            self.delay_tt = 5
            while self.ser.inWaiting() < 9:  # 无限循环...

                if self.delay_tt == 0:

                    # self.information_show('与烧录器连接失败，请选择正确的串口号!!', Qt.red)

                    return False
            data = self.ser.read(10)
            if ((0x7C != data[0]) or (0x01 != data[1]) or (0x55 != data[3])):
                self.information_show('与烧录器连接失败!', Qt.red)
            else:
                return True
        else:
            self.cmd_shell = "FA 01 02 00 09 00 06 1A 80 A6 7E"

            try:
                num = self.ser.inWaiting()
            except:
                # self.port_close()
                return False
            if num > 0:
                data = self.ser.read(num)

            self.send_data(self.cmd_shell)
            self.delay_tt = 5

            while self.ser.inWaiting() < 8:  # 无限循环...
                if self.delay_tt == 0:
                    # self.iapI2cEnterFlag = True
                    return False

            data = self.ser.read(8)

            if ((0xFA != data[0]) or (0x00 != data[1]) or (0x02 != data[2]) or (0x55 != data[5])):

                self.information_show('与烧录器连接失败!', Qt.red)

                return False
            else:

                return True




    def invert_8(self,x):
        y = 0
        for i in range(8):

            if (0 != (x & (1 << i))):
                # print(i)
                # print(1<<(7-i))
                y |= 1 << (7 - i)
        return y

    def invert_16(self,x):
        y = 0

        for i in range(16):

            if (0 != (x & (1 << i))):
                # print(i)
                # print(1<<(7-i))
                y |= 1 << (15 - i)
        return y

    #
    # def crc16_check(self,p, len):
    #     pp=typed.List()
    #     for i in range(len):
    #         pp.append(p[i])
    #     # [pp.append(x) for x in p]
    #
    #     return crc16_checkte(pp,len)
        # wCRCin = 0x0
        # wCPoly = 0x1021
        # wChar = 0
        # for i in range(len):
        #     pidx = (i & 0xFFFFFFFC) | (3 - (i & 3))
        #     wChar = self.invert_8(p[pidx])
        #     wCRCin ^= (wChar << 8)
        #
        #     for j in range(8):
        #         if (0x8000 == (wCRCin & 0x8000)):
        #             wCRCin = (wCRCin << 1) ^ wCPoly
        #         else:
        #             wCRCin <<= 1
        # return self.invert_16(wCRCin)
    def II2Cdownload(self):
        if self.is_download_work == 0:


            t1 = Thread(target=self.I2Cdownloadr, args=())
            t1.start()
        else:

            self.information_show('程序升级正在进行，请耐心等待!', Qt.black)

    def I2Cdownloadr(self):  # 此方法采用多线程执行，以防while 造成卡死

        if self.I2Cdownloadrr():
            pass
        else:
            self.fail_time=self.fail_time+1
            self.fail_time_label.setText(str(self.fail_time))
            self.is_download_work = 0
            self.progressbar_emit(100)
        pass


    def I2Cdownloadrr(self):#此方法采用多线程执行，以防while 造成卡死
        try:
            if self.ser.isOpen():
                pass
            else:
                self.information_show('请先选择并打开正确端口后再次尝试!', Qt.red)
                return False
            self.is_download_work = 1
            if self.hexfile_isopen == True:
                pass
            else:

                self.information_show('请先打开HEX文件!', Qt.red)
                return False

            #print(self.start_address)

            if self.start_address != int(self.adress_Edit.text()):
                self.information_show('程序起始地址不匹配，请重新确认后再次烧录!', Qt.red)
                return False
            self.information_show('开始建立通信!', Qt.black)
            self.progress_value = 0
            self.progressbar_emit(self.progress_value)

            if self.uart_mode__radioButton.isChecked():
                self.bootloader_versionEdit.setText("Bootloader版本号：    ")
                self.cmd_shell = "7C 01 FE FF 7E"

                try:
                    num = self.ser.inWaiting()
                except:
                    self.port_close()
                    return False
                if num > 0:
                    data = self.ser.read(num)

                self.send_data(self.cmd_shell)

                self.delay_tt = 50
                while self.ser.inWaiting() < 9:  # 无限循环...

                    if self.delay_tt == 0:
                        self.information_show('与烧录器连接失败，请选择正确的串口号!!', Qt.red)

                        return False
                data = self.ser.read(10)
                if ((0x7C != data[0]) or (0x01 != data[1]) or (0x55 != data[3])):
                    self.information_show('与烧录器连接失败!', Qt.red)



                self.cmd_shell = "7C 02 FD FF 7E"
                try:
                    num = self.ser.inWaiting()
                except:
                    self.port_close()
                    return False
                if num > 0:
                    data = self.ser.read(num)
                self.send_data(self.cmd_shell)
                self.delay_tt = 50
                while self.ser.inWaiting() < 9:  # 无限循环...

                    if self.delay_tt == 0:
                        self.information_show('与烧录器连接失败，请选择正确的串口号!', Qt.red)

                        return False
                data = self.ser.read(10)
                if ((0x7C != data[0]) or (0x02 != data[1]) or (0x55 != data[3])):

                    self.information_show('flash关闭写保护失败!', Qt.red)
                # else:
                #
                #     self.bootloader_versionEdit.setText("flash关闭写保护成功")

                # self.cmd_shell = "7C 06 F9 00 00 FF FF FD 7E"
                # try:
                #     num = self.ser.inWaiting()
                # except:
                #     self.port_close()
                #     return False
                # if num > 0:
                #       data = self.ser.read(num)
                # self.send_data(self.cmd_shell)
                # self.delay_tt = 50
                # while self.ser.inWaiting() < 9:  # 无限循环...
                #
                #     if self.delay_tt == 0:
                #         self.information_show('校验码设置超时接收!', Qt.red)
                #
                #         self.iapI2cEnterFlag = True
                #         return False
                # data = self.ser.read(10)
                # if ((0x7C != data[0]) or (0x06 != data[1]) or (0x55 != data[3])):
                #     self.information_textEdit.append('校验码设置失败!！!')

                self.cmd_shell = "7C 04 FB FF 7E"
                try:
                    num = self.ser.inWaiting()
                except:
                    self.port_close()
                    return False
                if num > 0:
                    data = self.ser.read(num)
                self.send_data(self.cmd_shell)
                self.delay_tt = 50
                while self.ser.inWaiting() < 9:  # 无限循环...

                    if self.delay_tt == 0:
                        self.information_show('app程序区擦除接收超时!', Qt.red)

                        self.iapI2cEnterFlag = True
                        return False
                data = self.ser.read(10)
                if ((0x7C != data[0]) or (0x04 != data[1]) or (0x55 != data[3])):
                    self.information_textEdit.append('app程序区擦除失败!！!')
                ########################################是否全擦除，待后续添加##############################################

                cnt = self.flashcodeSize
                i = 0
                lenn = 0
                addrWrite =0# self.start_address
                # startaddress = self.start_address


                self.information_show('正在烧录程序中，请保持线路连接......', Qt.black)
                start_time = time.time()

                while (cnt > 0):

                    if cnt > 256:
                        lenn = 256
                    else:
                        lenn = cnt
                    psendbuff = []
                    psendbuff.append(124)
                    psendbuff.append(5)
                    psendbuff.append(250)


                    # psendbuff.append((lenn + 10) >> 8 & 0xFF)
                    # psendbuff.append((lenn + 10) >> 0 & 0xFF)
                    psendbuff.append((addrWrite >> 24) & 0xFF)
                    psendbuff.append((addrWrite >> 16) & 0xFF)
                    psendbuff.append((addrWrite >> 8) & 0xFF)
                    psendbuff.append((addrWrite >> 0) & 0xFF)
                    psendbuff.append(self.checksum(psendbuff[3:7],4,0))
                    psendbuff.append(lenn - 1)

                    for i in range(lenn):
                        psendbuff.append(self.flashcode[addrWrite])
                        addrWrite = addrWrite + 1
                    csum = self.checksum(psendbuff[1:], len(psendbuff)-1, 0)

                    psendbuff.append(csum)

                    psendbuff.append(126)

                    # try:
                    #     num = self.ser.inWaiting()
                    # except:
                    #     self.port_close()
                    #     return False
                    # if num > 0:
                    #     data = self.ser.read(num)
                    #
                    # Hex_str = bytes(psendbuff)
                    # self.ser.write(Hex_str)
                    # self.delay_tt = 50
                    #
                    # while self.ser.inWaiting() < 8:  # 无限循环...
                    #
                    #     if self.delay_tt == 0:
                    #         self.information_textEdit.append('超时接收!')
                    #         self.iapI2cEnterFlag = True
                    #         return False
                    time_error = 0
                    for i in range(3):#后期改为3
                        time_error = time_error + 1
                        if self.hex_send_only(psendbuff):
                            break
                        else:

                            if time_error == 3:
                                self.information_textEdit.append('超时接收!')
                                return False
                    data = self.ser.read(10)

                    if ((0x7C != data[0]) or (0x05 != data[1]) or (0x55 != data[3])):

                        self.information_show('程序升级失败，请检查线路连接是否正常！', Qt.red)
                        if ((0x7C != data[0])):
                            self.information_show('包头接收错误！', Qt.red)
                            return False

                        if (0x05 != data[1]):
                            self.information_show('命令接收错误！', Qt.red)
                            return False

                        if (0x55 != data[3]):
                            self.information_show('下载程序出错，可以尝试先板子重新上电，再按下升级按钮!！', Qt.red)
                            return False

                    cnt -= lenn

                    if (self.progress_value < 99):
                        self.progress_value = int(addrWrite * 100 / self.flashcodeSize)
                        self.progressbar_emit(self.progress_value)
                        # self.update_progressBar.setValue(self.progress_value)

                # self.hex_crc_code

                psendbuff = []
                psendbuff.append(124)#"7C 06 F9 00 00 FF FF FD 7E"
                psendbuff.append(6)
                psendbuff.append(249)
                psendbuff.append(0)
                psendbuff.append(0)
                checksum_low = self.hex_crc_code & 0xFF

                checksum_high = (self.hex_crc_code >> 8) & 0xFF

                psendbuff.append(checksum_high)
                psendbuff.append(checksum_low)

                csum = self.checksum(psendbuff[1:], len(psendbuff)-1, 0)

                psendbuff.append(csum)
                psendbuff.append(126)

                try:
                    num = self.ser.inWaiting()
                except:
                    self.port_close()
                    return False
                if num > 0:
                    data = self.ser.read(num)
                Hex_str = bytes(psendbuff)
                self.ser.write(Hex_str)
                self.delay_tt = 50
                while self.ser.inWaiting() < 9:  # 无限循环...

                    if self.delay_tt == 0:
                        self.information_show('与烧录器连接失败，请选择正确的串口号!', Qt.red)
                        self.progressbar_emit(100)

                        return False
                data = self.ser.read(10)
                if ((0x7C != data[0]) or (0x06 != data[1]) or (0x55 != data[3])):
                    self.information_show('Flash写入失败，请再次尝试！', Qt.red)
                    self.progressbar_emit(100)
                    return False

                # flash写保护指令
                self.cmd_shell = "7C 03 FC FF 7E"
                try:
                    num = self.ser.inWaiting()
                except:
                    self.port_close()
                    return False
                if num > 0:
                    data = self.ser.read(num)
                self.send_data(self.cmd_shell)
                self.delay_tt = 50
                while self.ser.inWaiting() < 9:  # 无限循环...

                    if self.delay_tt == 0:
                        self.information_show('与烧录器连接失败，请选择正确的串口号!', Qt.red)
                        self.progressbar_emit(100)
                        self.iapI2cEnterFlag = True
                        return False
                data = self.ser.read(10)
                if ((0x7C != data[0]) or (0x03 != data[1]) or (0x55 != data[3])):
                    self.information_show('Flash写入失败，请再次尝试！', Qt.red)
                    self.progressbar_emit(100)
                    return False

                # 跳入app程序
                if self.update_and_run_checkbutton.isChecked():
                    self.cmd_shell = "7C 07 F8 FF 7E"
                    try:
                        num = self.ser.inWaiting()
                    except:
                        self.port_close()
                        return False
                    if num > 0:
                        data = self.ser.read(num)
                    self.send_data(self.cmd_shell)
                    self.progressbar_emit(100)
                    self.information_show('程序跳转至APP程序，执行APP程序！', Qt.black)

                # self.update_progressBar.setValue(100)
                # self.update_progressBar.setVisible(False)
                self.progressbar_emit(100)
                end_time = time.time() - start_time
                self.information_show("程序烧录耗时：{:.02f}s".format(end_time), Qt.black)
                self.update_sucess_num = self.update_sucess_num + 1
                self.update_sucess_timeEdit.setText("烧录成功次数：{0}".format(self.update_sucess_num))


            else:
                self.bootloader_versionEdit.setText("Bootloader版本号：    ")
                self.cmd_shell = "FA 01 02 00 09 00 06 1A 80 A6 7E"

                try:
                    num = self.ser.inWaiting()
                except:
                    self.port_close()
                    return False
                if num > 0:
                    data = self.ser.read(num)

                self.send_data(self.cmd_shell)

                self.delay_tt = 50
                while self.ser.inWaiting() < 8:  # 无限循环...

                    if self.delay_tt == 0:
                        self.information_show('与烧录器连接失败，请选择正确的串口号!!', Qt.red)

                        self.iapI2cEnterFlag = True
                        return False
                data = self.ser.read(8)
                if ((0xFA != data[0]) or (0x00 != data[1]) or (0x02 != data[2]) or (0x55 != data[5])):
                    self.information_show('与烧录器连接失败!', Qt.red)
                self.cmd_shell = "FA 01 34 00 06 CB 00 7E"
                try:
                    num = self.ser.inWaiting()
                except:
                    self.port_close()
                    return False
                if num > 0:
                    data = self.ser.read(num)
                self.send_data(self.cmd_shell)
                self.delay_tt = 50
                while self.ser.inWaiting() < 12:  # 无限循环...

                    if self.delay_tt == 0:
                        self.information_show('与烧录器连接失败，请选择正确的串口号!', Qt.red)

                        self.iapI2cEnterFlag = True
                        return False
                data = self.ser.read(12)
                if ((0xFA != data[0]) or (0x00 != data[1]) or (0x34 != data[2]) or (0x55 != data[5])):

                    self.information_show('与烧录器连接失败，请选择正确的串口号!', Qt.red)
                else:

                    self.bootloader_versionEdit.setText("Bootloader版本号：V" + '{:02X}'.format(data[6]))

                self.cmd_shell = "FA 01 31 00 06 CE 00 7E"
                try:
                    num = self.ser.inWaiting()
                except:
                    self.port_close()
                    return False
                if num > 0:
                    data = self.ser.read(num)
                self.send_data(self.cmd_shell)
                self.delay_tt = 50
                while self.ser.inWaiting() < 8:  # 无限循环...

                    if self.delay_tt == 0:
                        self.information_show('与烧录器连接失败，请选择正确的串口号!', Qt.red)

                        self.iapI2cEnterFlag = True
                        return False
                data = self.ser.read(8)
                if ((0xFA != data[0]) or (0x00 != data[1]) or (0x31 != data[2]) or (0x55 != data[5])):
                    self.information_textEdit.append('FLASH自检失败！!')

                ########################################是否全擦除，待后续添加##############################################

                cnt = self.flashcodeSize
                i = 0
                lenn = 0
                addrWrite = 0;


                self.information_show('正在烧录程序中，请保持线路连接......', Qt.black)
                start_time = time.time()

                while (cnt > 0):

                    if cnt > 256:
                        lenn = 256
                    else:
                        lenn = cnt
                    psendbuff = []
                    psendbuff.append(250)
                    psendbuff.append(1)
                    psendbuff.append(51)
                    psendbuff.append((lenn + 10) >> 8 & 0xFF)
                    psendbuff.append((lenn + 10) >> 0 & 0xFF)
                    psendbuff.append((addrWrite >> 24) & 0xFF)
                    psendbuff.append((addrWrite >> 16) & 0xFF)
                    psendbuff.append((addrWrite >> 8) & 0xFF)
                    psendbuff.append((addrWrite >> 0) & 0xFF)
                    psendbuff.append(lenn - 1)

                    for i in range(lenn):
                        psendbuff.append(self.flashcode[addrWrite])
                        addrWrite = addrWrite + 1
                    csum = self.checksum(psendbuff, len(psendbuff), 0)

                    psendbuff.append(csum)

                    psendbuff.append(126)

                    # try:
                    #     num = self.ser.inWaiting()
                    # except:
                    #     self.port_close()
                    #     return False
                    # if num > 0:
                    #     data = self.ser.read(num)
                    #
                    # Hex_str = bytes(psendbuff)
                    # self.ser.write(Hex_str)
                    # self.delay_tt = 50
                    #
                    # while self.ser.inWaiting() < 8:  # 无限循环...
                    #
                    #     if self.delay_tt == 0:
                    #         self.information_textEdit.append('超时接收!')
                    #         self.iapI2cEnterFlag = True
                    #         return False
                    time_error = 0
                    for i in range(3):
                        time_error = time_error + 1
                        if self.hex_send_only(psendbuff):
                            break
                        else:

                            if time_error == 3:
                                self.information_textEdit.append('超时接收!')
                                return False
                    data = self.ser.read(8)

                    if ((0xFA != data[0]) or (0x00 != data[1]) or (0x33 != data[2]) or (0x55 != data[5])):

                        self.information_show('程序升级失败，请检查线路连接是否正常！', Qt.red)
                        if ((0xFA != data[0])):
                            self.information_show('包头接收错误！', Qt.red)
                            return False

                        if (0x33 != data[2]):
                            self.information_show('命令接收错误！', Qt.red)
                            return False

                        if (0x55 != data[5]):
                            self.information_show('下载程序出错，可以尝试先板子重新上电，再按下升级按钮!！', Qt.red)
                            return False

                    cnt -= lenn

                    if (self.progress_value < 99):
                        self.progress_value = int(addrWrite * 100 / self.flashcodeSize)
                        self.progressbar_emit(self.progress_value)
                        # self.update_progressBar.setValue(self.progress_value)

                # self.hex_crc_code

                psendbuff = []
                psendbuff.append(250)
                psendbuff.append(1)
                psendbuff.append(55)
                psendbuff.append(0)
                psendbuff.append(8)
                psendbuff.append(200)
                checksum_low = self.hex_crc_code & 0xFF

                checksum_high = (self.hex_crc_code >> 8) & 0xFF

                psendbuff.append(checksum_high)
                psendbuff.append(checksum_low)
                csum = self.checksum(psendbuff, len(psendbuff), 0)

                psendbuff.append(csum)
                psendbuff.append(126)

                try:
                    num = self.ser.inWaiting()
                except:
                    self.port_close()
                    return False
                if num > 0:
                    data = self.ser.read(num)
                Hex_str = bytes(psendbuff)
                self.ser.write(Hex_str)
                self.delay_tt = 50
                while self.ser.inWaiting() < 8:  # 无限循环...

                    if self.delay_tt == 0:
                        self.information_show('与烧录器连接失败，请选择正确的串口号!', Qt.red)
                        self.progressbar_emit(100)
                        self.iapI2cEnterFlag = True
                        return False
                data = self.ser.read(8)
                if ((0xFA != data[0]) or (0x00 != data[1]) or (0x36 != data[2]) or (0x55 != data[5])):
                    self.information_show('Flash写入失败，请再次尝试！', Qt.red)
                    self.progressbar_emit(100)
                    return False

                # flash写保护指令
                self.cmd_shell = "FA 01 32 00 06 CD 00 7E"
                try:
                    num = self.ser.inWaiting()
                except:
                    self.port_close()
                    return False
                if num > 0:
                    data = self.ser.read(num)
                self.send_data(self.cmd_shell)
                self.delay_tt = 50
                while self.ser.inWaiting() < 8:  # 无限循环...

                    if self.delay_tt == 0:
                        self.information_show('与烧录器连接失败，请选择正确的串口号!', Qt.red)
                        self.progressbar_emit(100)
                        self.iapI2cEnterFlag = True
                        return False
                data = self.ser.read(8)
                if ((0xFA != data[0]) or (0x00 != data[1]) or (0x32 != data[2]) or (0x55 != data[5])):
                    self.information_show('Flash写入失败，请再次尝试！', Qt.red)
                    self.progressbar_emit(100)
                    return False

                # 跳入app程序
                if self.update_and_run_checkbutton.isChecked():
                    self.cmd_shell = "FA 01 35 00 06 CA 00 7E"
                    try:
                        num = self.ser.inWaiting()
                    except:
                        self.port_close()
                        return False
                    if num > 0:
                        data = self.ser.read(num)
                    self.send_data(self.cmd_shell)
                    self.progressbar_emit(100)
                    self.information_show('程序跳转至APP程序，执行APP程序！', Qt.black)

                # self.update_progressBar.setValue(100)
                # self.update_progressBar.setVisible(False)
                self.progressbar_emit(100)
                end_time = time.time() - start_time
                self.information_show("程序烧录耗时：{:.02f}s".format(end_time), Qt.black)
                self.update_sucess_num = self.update_sucess_num + 1
                self.update_sucess_timeEdit.setText("烧录成功次数：{0}".format(self.update_sucess_num))

            self.is_download_work = 0


            return True
        except:
            print(traceback.format_exc())


    def hex_send_only(self,psendbuff):
        try:
            num = self.ser.inWaiting()
        except:
            self.port_close()
            return False
        if num > 0:
            data = self.ser.read(num)

        Hex_str = bytes(psendbuff)
        self.ser.write(Hex_str)
        self.delay_tt = 50

        while self.ser.inWaiting() < 8:  # 无限循环...

            if self.delay_tt == 0:
                # self.information_textEdit.append('超时接收!')

                return False
        return True

    def tset_send(self):
        cnt = self.flashcodeSize
        i = 0
        lenn = 0
        addrWrite = 0;

        self.information_show('正在烧录程序中，请保持线路连接......', Qt.black)
        start_time = time.time()


        if cnt > int(self.adress_Edit.text()):
            lenn = int(self.adress_Edit.text())
        else:
            lenn = cnt
        psendbuff = []
        psendbuff.append(250)
        psendbuff.append(1)
        psendbuff.append(51)
        psendbuff.append((lenn + 10) >> 8 & 0xFF)
        psendbuff.append((lenn + 10) >> 0 & 0xFF)
        psendbuff.append((addrWrite >> 24) & 0xFF)
        psendbuff.append((addrWrite >> 16) & 0xFF)
        psendbuff.append((addrWrite >> 8) & 0xFF)
        psendbuff.append((addrWrite >> 0) & 0xFF)
        psendbuff.append(lenn - 1)

        for i in range(lenn):
            psendbuff.append(self.flashcode[addrWrite])
            addrWrite = addrWrite + 1
        csum = self.checksum(psendbuff, len(psendbuff), 0)

        psendbuff.append(csum)

        psendbuff.append(126)

        try:
            num = self.ser.inWaiting()
        except:
            self.port_close()
            return False
        if num > 0:
            data = self.ser.read(num)

        Hex_str = bytes(psendbuff)
        self.ser.write(Hex_str)
        self.delay_tt = 20

        while self.ser.inWaiting() < 8:  # 无限循环...

            if self.delay_tt == 0:
                self.information_textEdit.append('超时接收!')
                self.iapI2cEnterFlag = True
                return False
        data = self.ser.read(8)

        if ((0xFA != data[0]) or (0x00 != data[1]) or (0x33 != data[2]) or (0x55 != data[5])):

            self.information_show('程序升级失败，请检查线路连接是否正常！', Qt.red)
            if ((0xFA != data[0])):
                self.information_show('包头接收错误！', Qt.red)
                return False

            if (0x33 != data[2]):
                self.information_show('命令接收错误！', Qt.red)
                return False

            if (0x55 != data[5]):
                self.information_show('下载程序出错，可以尝试先板子重新上电，再按下升级按钮!！', Qt.red)
                return False

        cnt -= lenn

    def readIAPhexfile(self):


        try:
            flashStartAddr = 0x00000000
            flashEndAddr = 0x00000000


            forlder=self.init_cache.get("path")
            if forlder ==None:
                forlder = "./"
            else:
                if os.path.exists(forlder):
                    pass
                else:
                    forlder = "./"




            filepath, filetype = QFileDialog.getOpenFileName(self,
                                                             "选取文件",
                                                             forlder,
                                                             "HEX Files (*.hex)")

            new_forlder=os.path.dirname(filepath)
            if new_forlder!=forlder:
                self.init_cache.set("path",new_forlder)


            # self.init_cache.set("path", "12122")

            if os.path.isfile(filepath):

                try:
                    first_line=0
                    self.start_address=0
                    self.flashcode = [255] * 131072

                    fileHandler = open(filepath, "r")
                    while True:
                        # Get next line from file
                        line = fileHandler.readline()
                        # If line is empty then end of file reached
                        if not line:
                            break
                        l_line=line.strip()
                        if (l_line[0:1]==":"):
                            datalength = int(l_line[1:3], 16)
                            startAddress = int(l_line[3:7], 16)
                            # if first_line==0:
                            #     self.start_address=startAddress
                            #     first_line=1
                            # elif first_line==1:
                            #     self.start_address=startAddress
                            #     first_line=2

                            type = int(l_line[7:9], 16)
                            if type == 4:
                                baseAddr = int(l_line[9:13], 16)
                                baseAddr <<= 16

                            elif type == 0:
                                if first_line == 0:
                                    self.start_address = startAddress+baseAddr
                                    first_line = 1

                                for j in range(datalength):
                                    addrIdx = (baseAddr + startAddress + j)& 0xFFFFFF
                                    if (flashEndAddr < addrIdx):
                                        flashEndAddr = addrIdx
                                    addrIdx -= flashStartAddr
                                    if (addrIdx >= 130560):
                                        self.information_show('加载HEX文件超过128K，请重新加载！！！', Qt.red)

                                    self.flashcode[addrIdx]=int(l_line[9 + 2 * j: 9 + 2 * j + 2],16)
                                    #flashcode.append(bytes.fromhex(l_line[9 + 2 * j: 9 + 2 * j + 2]))
                        else:
                            break
                    self.flashcodeSize = flashEndAddr - flashStartAddr + 1
                    self.information_show("程序大小为：{0}个字节".format(self.flashcodeSize), Qt.black)

                    if(self.flashcodeSize>0):
                        CRC16_ds_LEN=(int((self.flashcodeSize-1)/512)+1)*512


                        crc16= self.crc.create(self.flashcode,CRC16_ds_LEN)#self.crc16_check(self.flashcode,CRC16_ds_LEN)
                        self.hex_crc_code=crc16
                        self.hexfile_isopen=True
                        self.app_check_codeEdit.setText("APP程序校验码：0x{0:2X}".format(self.hex_crc_code))
                        self.information_show("APP程序校验码：0x{0:2X}".format(self.hex_crc_code), Qt.black)

                    fileHandler.close()
                    #print(self.start_address)
                except:  # 捕获除与程序退出sys.exit()相关之外的所有异常
                    print(traceback.format_exc())
                    self.hexfile_isopen = False
                    # sys.exit()
            else:
                pass

            # 加载xml文件获取树
        except:
            print(traceback.format_exc())
    def closeEvent(self,e):
        try:
            if self.ser.isOpen():
                self.ser.close()
            pass
        except:
            print(traceback.format_exc())

    def send_data(self,hexdata):
        try:
            if self.ser.isOpen():
                Hex_str = bytes.fromhex(hexdata)
                self.ser.write(Hex_str)
        except:
            print(traceback.format_exc())









def main_run():
    app = 0
    app = QApplication(sys.argv)

    myshow = Serial_boot()
    myshow.show()
    # apply_stylesheet(app, theme='dark_teal.xml')

    sys.exit(app.exec())

if __name__ == '__main__':

    app = 0
    app = QApplication(sys.argv)

    myshow = Serial_boot()
    myshow.show()
    #apply_stylesheet(app, theme='dark_teal.xml')

    sys.exit(app.exec())


    # app = QApplication(sys.argv)
    # mainview = QMainWindow()
    # bootloader = Ui_boot_MainWindow()
    #
    # bootloader.setupUi(mainview)
    # ds = BootLoader()
    # ds.port_check()
    # mainview.show()
    #
    #
    #
    # sys.exit(app.exec())

