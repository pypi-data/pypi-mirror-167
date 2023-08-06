# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bootview.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPlainTextEdit, QProgressBar, QPushButton, QRadioButton,
    QSizePolicy, QStatusBar, QTextEdit, QWidget)

class Ui_boot_MainWindow(object):
    def setupUi(self, boot_MainWindow):
        if not boot_MainWindow.objectName():
            boot_MainWindow.setObjectName(u"boot_MainWindow")
        boot_MainWindow.resize(797, 608)
        self.centralwidget = QWidget(boot_MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.i2c_mode__radioButton = QRadioButton(self.centralwidget)
        self.i2c_mode__radioButton.setObjectName(u"i2c_mode__radioButton")
        self.i2c_mode__radioButton.setGeometry(QRect(20, 100, 95, 20))
        self.uart_mode__radioButton = QRadioButton(self.centralwidget)
        self.uart_mode__radioButton.setObjectName(u"uart_mode__radioButton")
        self.uart_mode__radioButton.setGeometry(QRect(20, 140, 95, 20))
        self.update_appall_radio = QRadioButton(self.centralwidget)
        self.update_appall_radio.setObjectName(u"update_appall_radio")
        self.update_appall_radio.setGeometry(QRect(170, 110, 181, 20))
        self.update_app_part_radio = QRadioButton(self.centralwidget)
        self.update_app_part_radio.setObjectName(u"update_app_part_radio")
        self.update_app_part_radio.setGeometry(QRect(170, 160, 231, 20))
        self.update_and_run_checkbutton = QCheckBox(self.centralwidget)
        self.update_and_run_checkbutton.setObjectName(u"update_and_run_checkbutton")
        self.update_and_run_checkbutton.setGeometry(QRect(450, 110, 181, 20))
        self.update_app_Button = QPushButton(self.centralwidget)
        self.update_app_Button.setObjectName(u"update_app_Button")
        self.update_app_Button.setGeometry(QRect(20, 220, 111, 24))
        self.check_is_updatesucess_Button = QPushButton(self.centralwidget)
        self.check_is_updatesucess_Button.setObjectName(u"check_is_updatesucess_Button")
        self.check_is_updatesucess_Button.setGeometry(QRect(190, 220, 111, 24))
        self.start_address_label = QLabel(self.centralwidget)
        self.start_address_label.setObjectName(u"start_address_label")
        self.start_address_label.setGeometry(QRect(450, 160, 111, 21))
        self.adress_Edit = QLineEdit(self.centralwidget)
        self.adress_Edit.setObjectName(u"adress_Edit")
        self.adress_Edit.setGeometry(QRect(560, 160, 113, 20))
        self.iap_usermanual_TextEdit = QPlainTextEdit(self.centralwidget)
        self.iap_usermanual_TextEdit.setObjectName(u"iap_usermanual_TextEdit")
        self.iap_usermanual_TextEdit.setGeometry(QRect(20, 270, 391, 91))
        self.app_check_codeEdit = QLineEdit(self.centralwidget)
        self.app_check_codeEdit.setObjectName(u"app_check_codeEdit")
        self.app_check_codeEdit.setGeometry(QRect(430, 270, 271, 20))
        self.bootloader_versionEdit = QLineEdit(self.centralwidget)
        self.bootloader_versionEdit.setObjectName(u"bootloader_versionEdit")
        self.bootloader_versionEdit.setGeometry(QRect(430, 300, 271, 20))
        self.update_sucess_timeEdit = QLineEdit(self.centralwidget)
        self.update_sucess_timeEdit.setObjectName(u"update_sucess_timeEdit")
        self.update_sucess_timeEdit.setGeometry(QRect(430, 340, 271, 20))
        self.clean_informaiton_Button = QPushButton(self.centralwidget)
        self.clean_informaiton_Button.setObjectName(u"clean_informaiton_Button")
        self.clean_informaiton_Button.setGeometry(QRect(430, 370, 75, 24))
        self.information_textEdit = QTextEdit(self.centralwidget)
        self.information_textEdit.setObjectName(u"information_textEdit")
        self.information_textEdit.setGeometry(QRect(10, 410, 771, 111))
        self.update_progressBar = QProgressBar(self.centralwidget)
        self.update_progressBar.setObjectName(u"update_progressBar")
        self.update_progressBar.setGeometry(QRect(10, 540, 781, 23))
        self.update_progressBar.setValue(24)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 20, 335, 26))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.serial_deviceBox = QComboBox(self.layoutWidget)
        self.serial_deviceBox.setObjectName(u"serial_deviceBox")

        self.horizontalLayout.addWidget(self.serial_deviceBox)

        self.scan_serialButton = QPushButton(self.layoutWidget)
        self.scan_serialButton.setObjectName(u"scan_serialButton")

        self.horizontalLayout.addWidget(self.scan_serialButton)

        self.open_hexfile_Button = QPushButton(self.layoutWidget)
        self.open_hexfile_Button.setObjectName(u"open_hexfile_Button")

        self.horizontalLayout.addWidget(self.open_hexfile_Button)

        boot_MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(boot_MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 797, 22))
        boot_MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(boot_MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        boot_MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(boot_MainWindow)

        QMetaObject.connectSlotsByName(boot_MainWindow)
    # setupUi

    def retranslateUi(self, boot_MainWindow):
        boot_MainWindow.setWindowTitle(QCoreApplication.translate("boot_MainWindow", u"Merops BootLoader IAP升级工具V0.1", None))
        self.i2c_mode__radioButton.setText(QCoreApplication.translate("boot_MainWindow", u"I2C", None))
        self.uart_mode__radioButton.setText(QCoreApplication.translate("boot_MainWindow", u"UART", None))
        self.update_appall_radio.setText(QCoreApplication.translate("boot_MainWindow", u"\u5347\u7ea7\u7a0b\u5e8f\u524d\u5148\u64e6\u9664\u6574\u4e2aAPP\u533a", None))
        self.update_app_part_radio.setText(QCoreApplication.translate("boot_MainWindow", u"APP\u533a\u53ea\u8986\u76d6\u65b0\u7a0b\u5e8f\uff0c\u5269\u4f59\u7a7a\u95f4\u4e0d\u64e6\u9664", None))
        self.update_and_run_checkbutton.setText(QCoreApplication.translate("boot_MainWindow", u"\u5347\u7ea7\u6210\u529f\u540e\u7acb\u5373\u6267\u884cAPP\u7a0b\u5e8f", None))
        self.update_app_Button.setText(QCoreApplication.translate("boot_MainWindow", u"\u5347\u7ea7APP\u533a\u7a0b\u5e8f", None))
        self.check_is_updatesucess_Button.setText(QCoreApplication.translate("boot_MainWindow", u"\u786e\u8ba4\u5347\u7ea7\u662f\u5426\u6210\u529f", None))
        self.start_address_label.setText(QCoreApplication.translate("boot_MainWindow", u"APP\u7a0b\u5e8f\u8d77\u59cb\u5730\u57400x", None))
        self.adress_Edit.setText(QCoreApplication.translate("boot_MainWindow", u"0", None))
        self.app_check_codeEdit.setText(QCoreApplication.translate("boot_MainWindow", u"APP\u7a0b\u5e8f\u6821\u9a8c\u7801\uff1a", None))
        self.bootloader_versionEdit.setText(QCoreApplication.translate("boot_MainWindow", u"BootlLoader\u7248\u672c\u53f7\uff1a", None))
        self.update_sucess_timeEdit.setText(QCoreApplication.translate("boot_MainWindow", u"\u70e7\u5f55\u6210\u529f\u6b21\u6570\uff1a0", None))
        self.clean_informaiton_Button.setText(QCoreApplication.translate("boot_MainWindow", u"\u6e05\u7a7a\u4fe1\u606f\u680f", None))
        self.scan_serialButton.setText(QCoreApplication.translate("boot_MainWindow", u"\u626b\u63cf\u5e76\u6253\u5f00\u4e32\u53e3", None))
        self.open_hexfile_Button.setText(QCoreApplication.translate("boot_MainWindow", u"\u6253\u5f00HEX\u6587\u4ef6", None))
    # retranslateUi

