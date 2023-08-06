#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/8/26 15:09
# @Author  : jeremy
# @File    : TEST.py


# def checksum(p, len, offset=0):
#     # return self.uchar_checksum(p)
#     sum = 0
#     i = offset
#     for i in range(len):
#
#         sum = sum + p[i]
#         if sum > 255:
#             sum = sum - 256
#     return sum  # &0xff
#
#
# DS=[6,249,0,0,255,255]
# print(DS[1:])
    #FA 01 02 00 09 00 06 1A 80 A6 7E


# print(checksum([0xFA,0x01,0x02,0x00,0x09,0x00,0x6,0x1A,0x80],9))

# print(crc16([0xFA,0x01,0x02,0x00,0x09,0x00,0x6,0x1A,0x80],9))
#
# input_s ="01 02 03 04 05 06 07 08 99 1A 0B"
# input_s = input_s.strip()
# send_list = []
# while input_s != '':
#     try:
#         num = int(input_s[0:2], 16)
#     except ValueError:
#         print(0)
#     input_s = input_s[2:].strip()
#     send_list.append(num)
# input_s = bytes(send_list)
# print(send_list)
# print(input_s)
# rev = to_hexstring(send_list)
# print(rev)

#b'\xe6\x88\x91\xe6\x98\xaf\xe4\xb8\x9c\xe5\xb0\x8f\xe4\xb8\x9c'
#b'\xce\xd2\xca\xc7\xb6\xab\xd0\xa1\xb6\xab'
# if(0xFA==250):
#     print(123)
# data=[5,6]
# print('APP校验码错误，程序烧录失败，校验码为：0x{:02X}{:02X}'.format(data[0],data[1]))
# text='23'
# print("%05d:" % 1+text)




import time
import tkinter
import tkinter.ttk

def show():
    for i in range(94):
        progressbarOne.step(1)
        root.update()
        # print(progressbarOne.cget('value'))
        time.sleep(0.05)
    root.destroy()
    # while progressbarOne.cget('value') <= progressbarOne['maximum']:
    #     progressbarOne.step(2)
    #     root.update()
    #     print(progressbarOne.cget('value'))
    #     time.sleep(0.05)


def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)

    root.geometry(size)
    root.update()


root = tkinter.Tk()
root.overrideredirect(1)
# root.geometry('550x320')
center_window(root, 550,320)
start_label = tkinter.Label(root, text='程序正在初始化，请耐心等待~')

start_label.pack(expand=tkinter.YES)

progressbarOne = tkinter.ttk.Progressbar(root, length=500, mode='determinate', orient=tkinter.HORIZONTAL)
progressbarOne.pack(side=tkinter.BOTTOM)

progressbarOne['maximum'] = 95
progressbarOne['value'] = 0

# button = tkinter.Button(root, text='Running', command=show)
# button.pack(pady=5)
show()
root.mainloop()
