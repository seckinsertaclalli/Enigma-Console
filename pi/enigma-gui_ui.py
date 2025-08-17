# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'enigma-gui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import new-res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(480, 800)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 480, 800))
        self.first_page = QWidget()
        self.first_page.setObjectName(u"first_page")
        self.background = QLabel(self.first_page)
        self.background.setObjectName(u"background")
        self.background.setGeometry(QRect(0, 0, 480, 800))
        self.background.setStyleSheet(u"background-image: url(bg-vertical.png);")
        self.enigmatext = QLabel(self.first_page)
        self.enigmatext.setObjectName(u"enigmatext")
        self.enigmatext.setGeometry(QRect(0, 100, 480, 51))
        font = QFont()
        font.setFamily(u"Montserrat Black")
        font.setPointSize(35)
        self.enigmatext.setFont(font)
        self.enigmatext.setStyleSheet(u"color:rgba(255,255,255,255);\n"
"")
        self.enigmatext.setTextFormat(Qt.PlainText)
        self.enigmatext.setAlignment(Qt.AlignCenter)
        self.consoletext = QLabel(self.first_page)
        self.consoletext.setObjectName(u"consoletext")
        self.consoletext.setGeometry(QRect(0, 150, 480, 51))
        font1 = QFont()
        font1.setFamily(u"Montserrat Light")
        font1.setPointSize(31)
        self.consoletext.setFont(font1)
        self.consoletext.setStyleSheet(u"color:rgba(255,255,255,255);\n"
"")
        self.consoletext.setTextFormat(Qt.AutoText)
        self.consoletext.setAlignment(Qt.AlignCenter)
        self.create_pass_label = QLineEdit(self.first_page)
        self.create_pass_label.setObjectName(u"create_pass_label")
        self.create_pass_label.setGeometry(QRect(110, 310, 260, 60))
        font2 = QFont()
        font2.setPointSize(20)
        self.create_pass_label.setFont(font2)
        self.create_pass_label.setMouseTracking(False)
        self.create_pass_label.setFocusPolicy(Qt.NoFocus)
        self.create_pass_label.setAutoFillBackground(False)
        self.create_pass_label.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:3px solid rgba(237, 237, 237, 237);\n"
"color:rgba(237, 237, 237, 237);\n"
"padding-bottom:7px;\n"
"background-color: rgba(0, 0, 0, 0);")
        self.create_pass_label.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText)
        self.create_pass_label.setFrame(True)
        self.create_pass_label.setEchoMode(QLineEdit.Password)
        self.create_pass_label.setAlignment(Qt.AlignCenter)
        self.create_pass_label.setProperty("clearButtonEnabled", False)
        self.ff_logo = QLabel(self.first_page)
        self.ff_logo.setObjectName(u"ff_logo")
        self.ff_logo.setGeometry(QRect(150, 620, 180, 180))
        self.ff_logo.setStyleSheet(u"border-image: url(Transperent-Logo.png);")
        self.without_pass_button = QPushButton(self.first_page)
        self.without_pass_button.setObjectName(u"without_pass_button")
        self.without_pass_button.setGeometry(QRect(110, 410, 260, 60))
        font3 = QFont()
        font3.setFamily(u"Tahoma")
        font3.setPointSize(12)
        self.without_pass_button.setFont(font3)
        self.without_pass_button.setStyleSheet(u"\n"
"       QPushButton{background-color:rgba(0, 0, 0, 0);border: 2px solid  rgba(237, 237, 237, 237);border-radius: 5px;padding: 5px;color:rgba(237, 237, 237, 237);background-color:  rgba(96, 96, 96, 96);}QPushButton:pressed {background-color: rgba(196, 196, 196, 196);}\n"
"        ")
        self.stackedWidget.addWidget(self.first_page)
        self.create_password_page1 = QWidget()
        self.create_password_page1.setObjectName(u"create_password_page1")
        self.background_2 = QLabel(self.create_password_page1)
        self.background_2.setObjectName(u"background_2")
        self.background_2.setGeometry(QRect(0, 0, 480, 800))
        self.background_2.setStyleSheet(u"background-image: url(bg-vertical.png);")
        self.enigmatext_2 = QLabel(self.create_password_page1)
        self.enigmatext_2.setObjectName(u"enigmatext_2")
        self.enigmatext_2.setGeometry(QRect(0, 10, 480, 51))
        self.enigmatext_2.setFont(font)
        self.enigmatext_2.setStyleSheet(u"color:rgba(255,255,255,255);\n"
"")
        self.enigmatext_2.setTextFormat(Qt.PlainText)
        self.enigmatext_2.setAlignment(Qt.AlignCenter)
        self.consoletext_2 = QLabel(self.create_password_page1)
        self.consoletext_2.setObjectName(u"consoletext_2")
        self.consoletext_2.setGeometry(QRect(0, 60, 480, 51))
        self.consoletext_2.setFont(font1)
        self.consoletext_2.setStyleSheet(u"\n"
"color:rgba(255,255,255,255);")
        self.consoletext_2.setTextFormat(Qt.AutoText)
        self.consoletext_2.setAlignment(Qt.AlignCenter)
        self.num4_pushbutton = QPushButton(self.create_password_page1)
        self.num4_pushbutton.setObjectName(u"num4_pushbutton")
        self.num4_pushbutton.setGeometry(QRect(60, 360, 100, 100))
        font4 = QFont()
        font4.setPointSize(23)
        font4.setBold(True)
        font4.setWeight(75)
        self.num4_pushbutton.setFont(font4)
        self.num4_pushbutton.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num4_pushbutton.setIconSize(QSize(50, 50))
        self.num4_pushbutton.setAutoDefault(False)
        self.num4_pushbutton.setFlat(True)
        self.num7_pushbutton = QPushButton(self.create_password_page1)
        self.num7_pushbutton.setObjectName(u"num7_pushbutton")
        self.num7_pushbutton.setGeometry(QRect(60, 490, 100, 100))
        self.num7_pushbutton.setFont(font4)
        self.num7_pushbutton.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num5_pushbutton = QPushButton(self.create_password_page1)
        self.num5_pushbutton.setObjectName(u"num5_pushbutton")
        self.num5_pushbutton.setGeometry(QRect(190, 360, 100, 100))
        self.num5_pushbutton.setFont(font4)
        self.num5_pushbutton.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num0_pushbutton = QPushButton(self.create_password_page1)
        self.num0_pushbutton.setObjectName(u"num0_pushbutton")
        self.num0_pushbutton.setGeometry(QRect(190, 620, 100, 100))
        self.num0_pushbutton.setFont(font4)
        self.num0_pushbutton.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num6_pushbutton = QPushButton(self.create_password_page1)
        self.num6_pushbutton.setObjectName(u"num6_pushbutton")
        self.num6_pushbutton.setGeometry(QRect(320, 360, 100, 100))
        self.num6_pushbutton.setFont(font4)
        self.num6_pushbutton.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.ent_pushbutton = QPushButton(self.create_password_page1)
        self.ent_pushbutton.setObjectName(u"ent_pushbutton")
        self.ent_pushbutton.setGeometry(QRect(320, 620, 100, 100))
        font5 = QFont()
        font5.setPointSize(20)
        font5.setBold(True)
        font5.setWeight(75)
        self.ent_pushbutton.setFont(font5)
        self.ent_pushbutton.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num1_pushbutton = QPushButton(self.create_password_page1)
        self.num1_pushbutton.setObjectName(u"num1_pushbutton")
        self.num1_pushbutton.setGeometry(QRect(60, 230, 100, 100))
        self.num1_pushbutton.setFont(font4)
        self.num1_pushbutton.setStyleSheet(u"\n"
"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num1_pushbutton.setIconSize(QSize(50, 50))
        self.num1_pushbutton.setAutoDefault(True)
        self.num1_pushbutton.setFlat(False)
        self.num8_pushbutton = QPushButton(self.create_password_page1)
        self.num8_pushbutton.setObjectName(u"num8_pushbutton")
        self.num8_pushbutton.setGeometry(QRect(190, 490, 100, 100))
        self.num8_pushbutton.setFont(font4)
        self.num8_pushbutton.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.del_pushbutton = QPushButton(self.create_password_page1)
        self.del_pushbutton.setObjectName(u"del_pushbutton")
        self.del_pushbutton.setGeometry(QRect(60, 620, 100, 100))
        self.del_pushbutton.setFont(font5)
        self.del_pushbutton.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num3_pushbutton = QPushButton(self.create_password_page1)
        self.num3_pushbutton.setObjectName(u"num3_pushbutton")
        self.num3_pushbutton.setGeometry(QRect(320, 230, 100, 100))
        self.num3_pushbutton.setFont(font4)
        self.num3_pushbutton.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num9_pushbutton = QPushButton(self.create_password_page1)
        self.num9_pushbutton.setObjectName(u"num9_pushbutton")
        self.num9_pushbutton.setGeometry(QRect(320, 490, 100, 100))
        self.num9_pushbutton.setFont(font4)
        self.num9_pushbutton.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num2_pushbutton = QPushButton(self.create_password_page1)
        self.num2_pushbutton.setObjectName(u"num2_pushbutton")
        self.num2_pushbutton.setGeometry(QRect(190, 230, 100, 100))
        self.num2_pushbutton.setFont(font4)
        self.num2_pushbutton.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.create_password_2 = QLineEdit(self.create_password_page1)
        self.create_password_2.setObjectName(u"create_password_2")
        self.create_password_2.setGeometry(QRect(100, 130, 280, 60))
        self.create_password_2.setFont(font2)
        self.create_password_2.setAutoFillBackground(False)
        self.create_password_2.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:3px solid rgba(237, 237, 237, 237);\n"
"color:rgba(237, 237, 237, 237);\n"
"padding-bottom:7px;\n"
"background-color: rgba(0, 0, 0, 0);")
        self.create_password_2.setFrame(True)
        self.create_password_2.setEchoMode(QLineEdit.Password)
        self.create_password_2.setAlignment(Qt.AlignCenter)
        self.create_password_2.setProperty("clearButtonEnabled", False)
        self.control1_pushbutton = QPushButton(self.create_password_page1)
        self.control1_pushbutton.setObjectName(u"control1_pushbutton")
        self.control1_pushbutton.setGeometry(QRect(70, 50, 30, 30))
        self.control1_pushbutton.setFont(font4)
        self.control1_pushbutton.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 15px; \n"
"        background-color: transparent; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(96, 96, 96, 96); \n"
" }")
        self.control1_pushbutton.setIconSize(QSize(50, 50))
        self.control1_pushbutton.setAutoDefault(True)
        self.control1_pushbutton.setFlat(False)
        self.control2_pushbutton = QPushButton(self.create_password_page1)
        self.control2_pushbutton.setObjectName(u"control2_pushbutton")
        self.control2_pushbutton.setGeometry(QRect(380, 50, 30, 30))
        self.control2_pushbutton.setFont(font4)
        self.control2_pushbutton.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 15px; \n"
"        background-color: transparent; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(96, 96, 96, 96); \n"
" }")
        self.control2_pushbutton.setIconSize(QSize(50, 50))
        self.control2_pushbutton.setAutoDefault(True)
        self.control2_pushbutton.setFlat(False)
        self.stackedWidget.addWidget(self.create_password_page1)
        self.again_password_page = QWidget()
        self.again_password_page.setObjectName(u"again_password_page")
        self.background_3 = QLabel(self.again_password_page)
        self.background_3.setObjectName(u"background_3")
        self.background_3.setGeometry(QRect(0, 0, 480, 800))
        self.background_3.setStyleSheet(u"background-image: url(bg-vertical.png);")
        self.confirm_password_button = QLineEdit(self.again_password_page)
        self.confirm_password_button.setObjectName(u"confirm_password_button")
        self.confirm_password_button.setGeometry(QRect(100, 130, 280, 60))
        self.confirm_password_button.setFont(font2)
        self.confirm_password_button.setFocusPolicy(Qt.NoFocus)
        self.confirm_password_button.setAutoFillBackground(False)
        self.confirm_password_button.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:3px solid rgba(237, 237, 237, 237);\n"
"color:rgba(237, 237, 237, 237);\n"
"padding-bottom:7px;\n"
"background-color: rgba(0, 0, 0, 0);")
        self.confirm_password_button.setFrame(True)
        self.confirm_password_button.setEchoMode(QLineEdit.Password)
        self.confirm_password_button.setAlignment(Qt.AlignCenter)
        self.confirm_password_button.setProperty("clearButtonEnabled", False)
        self.num2_pushbutton_2 = QPushButton(self.again_password_page)
        self.num2_pushbutton_2.setObjectName(u"num2_pushbutton_2")
        self.num2_pushbutton_2.setGeometry(QRect(190, 230, 100, 100))
        self.num2_pushbutton_2.setFont(font4)
        self.num2_pushbutton_2.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num1_pushbutton_2 = QPushButton(self.again_password_page)
        self.num1_pushbutton_2.setObjectName(u"num1_pushbutton_2")
        self.num1_pushbutton_2.setGeometry(QRect(60, 230, 100, 100))
        self.num1_pushbutton_2.setFont(font4)
        self.num1_pushbutton_2.setStyleSheet(u"\n"
"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num1_pushbutton_2.setIconSize(QSize(50, 50))
        self.num1_pushbutton_2.setAutoDefault(True)
        self.num1_pushbutton_2.setFlat(False)
        self.num3_pushbutton_2 = QPushButton(self.again_password_page)
        self.num3_pushbutton_2.setObjectName(u"num3_pushbutton_2")
        self.num3_pushbutton_2.setGeometry(QRect(320, 230, 100, 100))
        self.num3_pushbutton_2.setFont(font4)
        self.num3_pushbutton_2.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.control1_pushbutton_2 = QPushButton(self.again_password_page)
        self.control1_pushbutton_2.setObjectName(u"control1_pushbutton_2")
        self.control1_pushbutton_2.setGeometry(QRect(70, 50, 30, 30))
        self.control1_pushbutton_2.setFont(font4)
        self.control1_pushbutton_2.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 15px; \n"
"        background-color: #00FF00; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(96, 96, 96, 96); \n"
" }")
        self.control1_pushbutton_2.setIconSize(QSize(50, 50))
        self.control1_pushbutton_2.setAutoDefault(True)
        self.control1_pushbutton_2.setFlat(False)
        self.ent_pushbutton_2 = QPushButton(self.again_password_page)
        self.ent_pushbutton_2.setObjectName(u"ent_pushbutton_2")
        self.ent_pushbutton_2.setGeometry(QRect(320, 620, 100, 100))
        self.ent_pushbutton_2.setFont(font5)
        self.ent_pushbutton_2.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num8_pushbutton_2 = QPushButton(self.again_password_page)
        self.num8_pushbutton_2.setObjectName(u"num8_pushbutton_2")
        self.num8_pushbutton_2.setGeometry(QRect(190, 490, 100, 100))
        self.num8_pushbutton_2.setFont(font4)
        self.num8_pushbutton_2.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.enigmatext_3 = QLabel(self.again_password_page)
        self.enigmatext_3.setObjectName(u"enigmatext_3")
        self.enigmatext_3.setGeometry(QRect(0, 10, 480, 51))
        self.enigmatext_3.setFont(font)
        self.enigmatext_3.setStyleSheet(u"color:rgba(255,255,255,255);\n"
"")
        self.enigmatext_3.setTextFormat(Qt.PlainText)
        self.enigmatext_3.setAlignment(Qt.AlignCenter)
        self.num6_pushbutton_2 = QPushButton(self.again_password_page)
        self.num6_pushbutton_2.setObjectName(u"num6_pushbutton_2")
        self.num6_pushbutton_2.setGeometry(QRect(320, 360, 100, 100))
        self.num6_pushbutton_2.setFont(font4)
        self.num6_pushbutton_2.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.control2_pushbutton_2 = QPushButton(self.again_password_page)
        self.control2_pushbutton_2.setObjectName(u"control2_pushbutton_2")
        self.control2_pushbutton_2.setGeometry(QRect(380, 50, 30, 30))
        self.control2_pushbutton_2.setFont(font4)
        self.control2_pushbutton_2.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 15px; \n"
"        background-color: transparent; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(96, 96, 96, 96); \n"
" }")
        self.control2_pushbutton_2.setIconSize(QSize(50, 50))
        self.control2_pushbutton_2.setAutoDefault(True)
        self.control2_pushbutton_2.setFlat(False)
        self.num7_pushbutton_2 = QPushButton(self.again_password_page)
        self.num7_pushbutton_2.setObjectName(u"num7_pushbutton_2")
        self.num7_pushbutton_2.setGeometry(QRect(60, 490, 100, 100))
        self.num7_pushbutton_2.setFont(font4)
        self.num7_pushbutton_2.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.del_pushbutton_2 = QPushButton(self.again_password_page)
        self.del_pushbutton_2.setObjectName(u"del_pushbutton_2")
        self.del_pushbutton_2.setGeometry(QRect(60, 620, 100, 100))
        self.del_pushbutton_2.setFont(font5)
        self.del_pushbutton_2.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num4_pushbutton_2 = QPushButton(self.again_password_page)
        self.num4_pushbutton_2.setObjectName(u"num4_pushbutton_2")
        self.num4_pushbutton_2.setGeometry(QRect(60, 360, 100, 100))
        self.num4_pushbutton_2.setFont(font4)
        self.num4_pushbutton_2.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num4_pushbutton_2.setIconSize(QSize(50, 50))
        self.num4_pushbutton_2.setAutoDefault(False)
        self.num4_pushbutton_2.setFlat(True)
        self.num5_pushbutton_2 = QPushButton(self.again_password_page)
        self.num5_pushbutton_2.setObjectName(u"num5_pushbutton_2")
        self.num5_pushbutton_2.setGeometry(QRect(190, 360, 100, 100))
        self.num5_pushbutton_2.setFont(font4)
        self.num5_pushbutton_2.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num9_pushbutton_2 = QPushButton(self.again_password_page)
        self.num9_pushbutton_2.setObjectName(u"num9_pushbutton_2")
        self.num9_pushbutton_2.setGeometry(QRect(320, 490, 100, 100))
        self.num9_pushbutton_2.setFont(font4)
        self.num9_pushbutton_2.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.consoletext_3 = QLabel(self.again_password_page)
        self.consoletext_3.setObjectName(u"consoletext_3")
        self.consoletext_3.setGeometry(QRect(0, 60, 480, 51))
        self.consoletext_3.setFont(font1)
        self.consoletext_3.setStyleSheet(u"\n"
"color:rgba(255,255,255,255);")
        self.consoletext_3.setTextFormat(Qt.AutoText)
        self.consoletext_3.setAlignment(Qt.AlignCenter)
        self.num0_pushbutton_2 = QPushButton(self.again_password_page)
        self.num0_pushbutton_2.setObjectName(u"num0_pushbutton_2")
        self.num0_pushbutton_2.setGeometry(QRect(190, 620, 100, 100))
        self.num0_pushbutton_2.setFont(font4)
        self.num0_pushbutton_2.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.stackedWidget.addWidget(self.again_password_page)
        self.password_done_page = QWidget()
        self.password_done_page.setObjectName(u"password_done_page")
        self.background_4 = QLabel(self.password_done_page)
        self.background_4.setObjectName(u"background_4")
        self.background_4.setGeometry(QRect(0, 0, 480, 800))
        self.background_4.setStyleSheet(u"background-image: url(bg-vertical.png);")
        self.enigmatext_4 = QLabel(self.password_done_page)
        self.enigmatext_4.setObjectName(u"enigmatext_4")
        self.enigmatext_4.setGeometry(QRect(0, 100, 480, 51))
        self.enigmatext_4.setFont(font)
        self.enigmatext_4.setStyleSheet(u"color:rgba(255,255,255,255);\n"
"")
        self.enigmatext_4.setTextFormat(Qt.PlainText)
        self.enigmatext_4.setAlignment(Qt.AlignCenter)
        self.consoletext_4 = QLabel(self.password_done_page)
        self.consoletext_4.setObjectName(u"consoletext_4")
        self.consoletext_4.setGeometry(QRect(0, 150, 480, 51))
        self.consoletext_4.setFont(font1)
        self.consoletext_4.setStyleSheet(u"color:rgba(255,255,255,255);\n"
"")
        self.consoletext_4.setTextFormat(Qt.AutoText)
        self.consoletext_4.setAlignment(Qt.AlignCenter)
        self.finish_text = QLabel(self.password_done_page)
        self.finish_text.setObjectName(u"finish_text")
        self.finish_text.setGeometry(QRect(0, 290, 480, 51))
        font6 = QFont()
        font6.setFamily(u"Montserrat Light")
        font6.setPointSize(35)
        self.finish_text.setFont(font6)
        self.finish_text.setStyleSheet(u"color:rgba(255,255,255,255);\n"
"")
        self.finish_text.setTextFormat(Qt.PlainText)
        self.finish_text.setAlignment(Qt.AlignCenter)
        self.security_text = QLabel(self.password_done_page)
        self.security_text.setObjectName(u"security_text")
        self.security_text.setGeometry(QRect(0, 340, 480, 51))
        font7 = QFont()
        font7.setFamily(u"Montserrat Medium")
        font7.setPointSize(15)
        self.security_text.setFont(font7)
        self.security_text.setStyleSheet(u"color:rgba(255,255,255,255);\n"
"")
        self.security_text.setTextFormat(Qt.PlainText)
        self.security_text.setAlignment(Qt.AlignCenter)
        self.securit_code_label = QLineEdit(self.password_done_page)
        self.securit_code_label.setObjectName(u"securit_code_label")
        self.securit_code_label.setGeometry(QRect(100, 410, 280, 60))
        font8 = QFont()
        font8.setPointSize(16)
        self.securit_code_label.setFont(font8)
        self.securit_code_label.setMouseTracking(False)
        self.securit_code_label.setFocusPolicy(Qt.NoFocus)
        self.securit_code_label.setAutoFillBackground(False)
        self.securit_code_label.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:3px solid rgba(237, 237, 237, 237);\n"
"color:rgba(237, 237, 237, 237);\n"
"padding-bottom:7px;\n"
"background-color: rgba(0, 0, 0, 0);")
        self.securit_code_label.setFrame(True)
        self.securit_code_label.setEchoMode(QLineEdit.Normal)
        self.securit_code_label.setAlignment(Qt.AlignCenter)
        self.securit_code_label.setReadOnly(True)
        self.securit_code_label.setProperty("clearButtonEnabled", False)
        self.info_text = QLabel(self.password_done_page)
        self.info_text.setObjectName(u"info_text")
        self.info_text.setGeometry(QRect(90, 490, 311, 131))
        font9 = QFont()
        font9.setFamily(u"Montserrat Medium")
        font9.setPointSize(12)
        font9.setStrikeOut(False)
        self.info_text.setFont(font9)
        self.info_text.setLayoutDirection(Qt.LeftToRight)
        self.info_text.setAutoFillBackground(False)
        self.info_text.setStyleSheet(u"color:rgba(255,255,255,255);\n"
"")
        self.info_text.setTextFormat(Qt.AutoText)
        self.info_text.setScaledContents(False)
        self.info_text.setAlignment(Qt.AlignCenter)
        self.info_text.setWordWrap(True)
        self.continue_button = QPushButton(self.password_done_page)
        self.continue_button.setObjectName(u"continue_button")
        self.continue_button.setEnabled(True)
        self.continue_button.setGeometry(QRect(200, 630, 80, 80))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.continue_button.sizePolicy().hasHeightForWidth())
        self.continue_button.setSizePolicy(sizePolicy)
        font10 = QFont()
        font10.setKerning(False)
        self.continue_button.setFont(font10)
        self.continue_button.setLayoutDirection(Qt.LeftToRight)
        self.continue_button.setStyleSheet(u"QPushButton {border-radius: 40px;}QPushButton:pressed {background-color: rgba(196, 196, 196, 196);}\n"
"")
        icon = QIcon()
        icon.addFile(u"continue-icon.png", QSize(), QIcon.Active, QIcon.On)
        self.continue_button.setIcon(icon)
        self.continue_button.setIconSize(QSize(80, 80))
        self.continue_button.setCheckable(False)
        self.continue_button.setAutoRepeat(False)
        self.stackedWidget.addWidget(self.password_done_page)
        self.main_page = QWidget()
        self.main_page.setObjectName(u"main_page")
        self.background_5 = QLabel(self.main_page)
        self.background_5.setObjectName(u"background_5")
        self.background_5.setGeometry(QRect(0, 0, 480, 800))
        self.background_5.setStyleSheet(u"background-image: url(bg-vertical.png);")
        self.enigmatext_5 = QLabel(self.main_page)
        self.enigmatext_5.setObjectName(u"enigmatext_5")
        self.enigmatext_5.setGeometry(QRect(0, 100, 480, 51))
        self.enigmatext_5.setFont(font)
        self.enigmatext_5.setStyleSheet(u"color:rgba(255,255,255,255);\n"
"")
        self.enigmatext_5.setTextFormat(Qt.PlainText)
        self.enigmatext_5.setAlignment(Qt.AlignCenter)
        self.consoletext_5 = QLabel(self.main_page)
        self.consoletext_5.setObjectName(u"consoletext_5")
        self.consoletext_5.setGeometry(QRect(0, 150, 480, 51))
        self.consoletext_5.setFont(font1)
        self.consoletext_5.setStyleSheet(u"color:rgba(255,255,255,255);\n"
"")
        self.consoletext_5.setTextFormat(Qt.AutoText)
        self.consoletext_5.setAlignment(Qt.AlignCenter)
        self.open_button = QPushButton(self.main_page)
        self.open_button.setObjectName(u"open_button")
        self.open_button.setGeometry(QRect(99, 270, 281, 111))
        font11 = QFont()
        font11.setFamily(u"Tahoma")
        font11.setPointSize(16)
        self.open_button.setFont(font11)
        self.open_button.setStyleSheet(u"QPushButton {\n"
"border-radius: 5px;\n"
"padding: 5px; \n"
"color:#383838;\n"
"background-color:  #DCFFCC;\n"
"}\n"
"QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }\n"
"\n"
"    ")
        self.close_button = QPushButton(self.main_page)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setGeometry(QRect(100, 410, 281, 111))
        self.close_button.setFont(font11)
        self.close_button.setStyleSheet(u"QPushButton {\n"
"border-radius: 5px;\n"
"padding: 5px; \n"
"color:#383838;\n"
"background-color:  #8E6C6C;\n"
"}\n"
"QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }\n"
"\n"
"    ")
        self.ff_logo_2 = QLabel(self.main_page)
        self.ff_logo_2.setObjectName(u"ff_logo_2")
        self.ff_logo_2.setGeometry(QRect(150, 620, 180, 180))
        self.ff_logo_2.setStyleSheet(u"border-image: url(Transperent-Logo.png);")
        self.settings_pushbutton = QPushButton(self.main_page)
        self.settings_pushbutton.setObjectName(u"settings_pushbutton")
        self.settings_pushbutton.setGeometry(QRect(160, 580, 160, 40))
        font12 = QFont()
        font12.setFamily(u"Tahoma")
        font12.setPointSize(15)
        self.settings_pushbutton.setFont(font12)
        self.settings_pushbutton.setStyleSheet(u"\n"
"       QPushButton{background-color:rgba(0, 0, 0, 0);border: 2px solid  rgba(237, 237, 237, 237);border-radius: 5px;padding: 5px;color:rgba(237, 237, 237, 237);padding-bottom:9px;background-color:  rgba(96, 96, 96, 96);} QPushButton:pressed {background-color: rgba(196, 196, 196, 196); }\n"
"       ")
        self.settings_pushbutton.setCheckable(False)
        self.settings_pushbutton.setAutoDefault(False)
        self.stackedWidget.addWidget(self.main_page)
        self.password_open = QWidget()
        self.password_open.setObjectName(u"password_open")
        self.num3_pushbutton_9 = QPushButton(self.password_open)
        self.num3_pushbutton_9.setObjectName(u"num3_pushbutton_9")
        self.num3_pushbutton_9.setGeometry(QRect(320, 230, 100, 100))
        self.num3_pushbutton_9.setFont(font4)
        self.num3_pushbutton_9.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num7_pushbutton_9 = QPushButton(self.password_open)
        self.num7_pushbutton_9.setObjectName(u"num7_pushbutton_9")
        self.num7_pushbutton_9.setGeometry(QRect(60, 490, 100, 100))
        self.num7_pushbutton_9.setFont(font4)
        self.num7_pushbutton_9.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.open_password_button = QLineEdit(self.password_open)
        self.open_password_button.setObjectName(u"open_password_button")
        self.open_password_button.setGeometry(QRect(100, 130, 280, 60))
        self.open_password_button.setFont(font2)
        self.open_password_button.setFocusPolicy(Qt.NoFocus)
        self.open_password_button.setAutoFillBackground(False)
        self.open_password_button.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:3px solid rgba(237, 237, 237, 237);\n"
"color:rgba(237, 237, 237, 237);\n"
"padding-bottom:7px;\n"
"background-color: rgba(0, 0, 0, 0);")
        self.open_password_button.setFrame(True)
        self.open_password_button.setEchoMode(QLineEdit.Password)
        self.open_password_button.setAlignment(Qt.AlignCenter)
        self.open_password_button.setProperty("clearButtonEnabled", False)
        self.ent_pushbutton_9 = QPushButton(self.password_open)
        self.ent_pushbutton_9.setObjectName(u"ent_pushbutton_9")
        self.ent_pushbutton_9.setGeometry(QRect(320, 620, 100, 100))
        self.ent_pushbutton_9.setFont(font5)
        self.ent_pushbutton_9.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.enigmatext_14 = QLabel(self.password_open)
        self.enigmatext_14.setObjectName(u"enigmatext_14")
        self.enigmatext_14.setGeometry(QRect(0, 10, 480, 51))
        self.enigmatext_14.setFont(font)
        self.enigmatext_14.setStyleSheet(u"color:rgba(255,255,255,255);\n"
"")
        self.enigmatext_14.setTextFormat(Qt.PlainText)
        self.enigmatext_14.setAlignment(Qt.AlignCenter)
        self.del_pushbutton_9 = QPushButton(self.password_open)
        self.del_pushbutton_9.setObjectName(u"del_pushbutton_9")
        self.del_pushbutton_9.setGeometry(QRect(60, 620, 100, 100))
        self.del_pushbutton_9.setFont(font5)
        self.del_pushbutton_9.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num6_pushbutton_9 = QPushButton(self.password_open)
        self.num6_pushbutton_9.setObjectName(u"num6_pushbutton_9")
        self.num6_pushbutton_9.setGeometry(QRect(320, 360, 100, 100))
        self.num6_pushbutton_9.setFont(font4)
        self.num6_pushbutton_9.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num0_pushbutton_9 = QPushButton(self.password_open)
        self.num0_pushbutton_9.setObjectName(u"num0_pushbutton_9")
        self.num0_pushbutton_9.setGeometry(QRect(190, 620, 100, 100))
        self.num0_pushbutton_9.setFont(font4)
        self.num0_pushbutton_9.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.background_14 = QLabel(self.password_open)
        self.background_14.setObjectName(u"background_14")
        self.background_14.setGeometry(QRect(0, 0, 480, 800))
        self.background_14.setStyleSheet(u"background-image: url(bg-vertical.png);")
        self.num2_pushbutton_9 = QPushButton(self.password_open)
        self.num2_pushbutton_9.setObjectName(u"num2_pushbutton_9")
        self.num2_pushbutton_9.setGeometry(QRect(190, 230, 100, 100))
        self.num2_pushbutton_9.setFont(font4)
        self.num2_pushbutton_9.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num9_pushbutton_9 = QPushButton(self.password_open)
        self.num9_pushbutton_9.setObjectName(u"num9_pushbutton_9")
        self.num9_pushbutton_9.setGeometry(QRect(320, 490, 100, 100))
        self.num9_pushbutton_9.setFont(font4)
        self.num9_pushbutton_9.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num1_pushbutton_9 = QPushButton(self.password_open)
        self.num1_pushbutton_9.setObjectName(u"num1_pushbutton_9")
        self.num1_pushbutton_9.setGeometry(QRect(60, 230, 100, 100))
        self.num1_pushbutton_9.setFont(font4)
        self.num1_pushbutton_9.setStyleSheet(u"\n"
"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num1_pushbutton_9.setIconSize(QSize(50, 50))
        self.num1_pushbutton_9.setAutoDefault(True)
        self.num1_pushbutton_9.setFlat(False)
        self.consoletext_15 = QLabel(self.password_open)
        self.consoletext_15.setObjectName(u"consoletext_15")
        self.consoletext_15.setGeometry(QRect(0, 60, 480, 51))
        self.consoletext_15.setFont(font1)
        self.consoletext_15.setStyleSheet(u"\n"
"color:rgba(255,255,255,255);")
        self.consoletext_15.setTextFormat(Qt.AutoText)
        self.consoletext_15.setAlignment(Qt.AlignCenter)
        self.num8_pushbutton_9 = QPushButton(self.password_open)
        self.num8_pushbutton_9.setObjectName(u"num8_pushbutton_9")
        self.num8_pushbutton_9.setGeometry(QRect(190, 490, 100, 100))
        self.num8_pushbutton_9.setFont(font4)
        self.num8_pushbutton_9.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num4_pushbutton_9 = QPushButton(self.password_open)
        self.num4_pushbutton_9.setObjectName(u"num4_pushbutton_9")
        self.num4_pushbutton_9.setGeometry(QRect(60, 360, 100, 100))
        self.num4_pushbutton_9.setFont(font4)
        self.num4_pushbutton_9.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num4_pushbutton_9.setIconSize(QSize(50, 50))
        self.num4_pushbutton_9.setAutoDefault(False)
        self.num4_pushbutton_9.setFlat(True)
        self.num5_pushbutton_9 = QPushButton(self.password_open)
        self.num5_pushbutton_9.setObjectName(u"num5_pushbutton_9")
        self.num5_pushbutton_9.setGeometry(QRect(190, 360, 100, 100))
        self.num5_pushbutton_9.setFont(font4)
        self.num5_pushbutton_9.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.stackedWidget.addWidget(self.password_open)
        self.background_14.raise_()
        self.num3_pushbutton_9.raise_()
        self.num7_pushbutton_9.raise_()
        self.open_password_button.raise_()
        self.ent_pushbutton_9.raise_()
        self.enigmatext_14.raise_()
        self.del_pushbutton_9.raise_()
        self.num6_pushbutton_9.raise_()
        self.num0_pushbutton_9.raise_()
        self.num2_pushbutton_9.raise_()
        self.num9_pushbutton_9.raise_()
        self.num1_pushbutton_9.raise_()
        self.consoletext_15.raise_()
        self.num8_pushbutton_9.raise_()
        self.num4_pushbutton_9.raise_()
        self.num5_pushbutton_9.raise_()
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.background_6 = QLabel(self.settings_page)
        self.background_6.setObjectName(u"background_6")
        self.background_6.setGeometry(QRect(0, 0, 480, 800))
        self.background_6.setStyleSheet(u"background-image: url(bg-vertical.png);")
        self.consoletext_6 = QLabel(self.settings_page)
        self.consoletext_6.setObjectName(u"consoletext_6")
        self.consoletext_6.setGeometry(QRect(0, 150, 480, 51))
        self.consoletext_6.setFont(font1)
        self.consoletext_6.setStyleSheet(u"color:rgba(255,255,255,255);\n"
"")
        self.consoletext_6.setTextFormat(Qt.AutoText)
        self.consoletext_6.setAlignment(Qt.AlignCenter)
        self.enigmatext_6 = QLabel(self.settings_page)
        self.enigmatext_6.setObjectName(u"enigmatext_6")
        self.enigmatext_6.setGeometry(QRect(0, 100, 480, 51))
        self.enigmatext_6.setFont(font)
        self.enigmatext_6.setStyleSheet(u"color:rgba(255,255,255,255);\n"
"")
        self.enigmatext_6.setTextFormat(Qt.PlainText)
        self.enigmatext_6.setAlignment(Qt.AlignCenter)
        self.consoletext_7 = QLabel(self.settings_page)
        self.consoletext_7.setObjectName(u"consoletext_7")
        self.consoletext_7.setGeometry(QRect(0, 200, 480, 51))
        font13 = QFont()
        font13.setFamily(u"Montserrat ExtraBold")
        font13.setPointSize(15)
        font13.setUnderline(True)
        self.consoletext_7.setFont(font13)
        self.consoletext_7.setStyleSheet(u"color:rgba(255,255,255,255);\n"
"")
        self.consoletext_7.setTextFormat(Qt.AutoText)
        self.consoletext_7.setAlignment(Qt.AlignCenter)
        self.change_password_label = QPushButton(self.settings_page)
        self.change_password_label.setObjectName(u"change_password_label")
        self.change_password_label.setGeometry(QRect(90, 280, 300, 50))
        self.change_password_label.setFont(font2)
        self.change_password_label.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:3px solid rgba(237, 237, 237, 237);\n"
"color:rgba(237, 237, 237, 237);\n"
"padding-bottom:7px;\n"
"background-color: rgba(0, 0, 0, 0);")
        self.change_condition_lable = QPushButton(self.settings_page)
        self.change_condition_lable.setObjectName(u"change_condition_lable")
        self.change_condition_lable.setGeometry(QRect(90, 360, 300, 50))
        self.change_condition_lable.setFont(font2)
        self.change_condition_lable.setLayoutDirection(Qt.LeftToRight)
        self.change_condition_lable.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:3px solid rgba(237, 237, 237, 237);\n"
"color:rgba(237, 237, 237, 237);\n"
"padding-bottom:7px;\n"
"background-color: rgba(0, 0, 0, 0);")
        self.forgot_security_code_label = QPushButton(self.settings_page)
        self.forgot_security_code_label.setObjectName(u"forgot_security_code_label")
        self.forgot_security_code_label.setGeometry(QRect(90, 450, 300, 50))
        self.forgot_security_code_label.setFont(font3)
        self.forgot_security_code_label.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:3px solid rgba(237, 237, 237, 237);\n"
"color:rgba(237, 237, 237, 237);\n"
"padding-bottom:7px;\n"
"background-color: rgba(0, 0, 0, 0);")
        self.ff_logo_3 = QLabel(self.settings_page)
        self.ff_logo_3.setObjectName(u"ff_logo_3")
        self.ff_logo_3.setGeometry(QRect(150, 620, 180, 180))
        self.ff_logo_3.setStyleSheet(u"border-image: url(Transperent-Logo.png);")
        self.back_button = QPushButton(self.settings_page)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setEnabled(True)
        self.back_button.setGeometry(QRect(200, 540, 80, 80))
        sizePolicy.setHeightForWidth(self.back_button.sizePolicy().hasHeightForWidth())
        self.back_button.setSizePolicy(sizePolicy)
        self.back_button.setFont(font10)
        self.back_button.setLayoutDirection(Qt.LeftToRight)
        self.back_button.setStyleSheet(u"QPushButton { border-radius: 40px;}\n"
"    QPushButton:pressed {background-color: rgba(196, 196, 196, 196); }\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"back-icon.png", QSize(), QIcon.Active, QIcon.On)
        self.back_button.setIcon(icon1)
        self.back_button.setIconSize(QSize(80, 80))
        self.back_button.setCheckable(False)
        self.back_button.setAutoRepeat(False)
        self.label = QLabel(self.settings_page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(5, 780, 150, 15))
        font14 = QFont()
        font14.setPointSize(10)
        self.label.setFont(font14)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2 = QLabel(self.settings_page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(315, 780, 160, 15))
        self.label_2.setFont(font14)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.stackedWidget.addWidget(self.settings_page)
        self.change_password_page = QWidget()
        self.change_password_page.setObjectName(u"change_password_page")
        self.control2_pushbutton_3 = QPushButton(self.change_password_page)
        self.control2_pushbutton_3.setObjectName(u"control2_pushbutton_3")
        self.control2_pushbutton_3.setGeometry(QRect(380, 50, 30, 30))
        self.control2_pushbutton_3.setFont(font4)
        self.control2_pushbutton_3.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 15px; \n"
"        background-color: transparent; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(96, 96, 96, 96); \n"
" }")
        self.control2_pushbutton_3.setIconSize(QSize(50, 50))
        self.control2_pushbutton_3.setAutoDefault(True)
        self.control2_pushbutton_3.setFlat(False)
        self.consoletext_8 = QLabel(self.change_password_page)
        self.consoletext_8.setObjectName(u"consoletext_8")
        self.consoletext_8.setGeometry(QRect(0, 60, 480, 51))
        self.consoletext_8.setFont(font1)
        self.consoletext_8.setStyleSheet(u"\n"
"color:rgba(255,255,255,255);")
        self.consoletext_8.setTextFormat(Qt.AutoText)
        self.consoletext_8.setAlignment(Qt.AlignCenter)
        self.num3_pushbutton_3 = QPushButton(self.change_password_page)
        self.num3_pushbutton_3.setObjectName(u"num3_pushbutton_3")
        self.num3_pushbutton_3.setGeometry(QRect(320, 230, 100, 100))
        self.num3_pushbutton_3.setFont(font4)
        self.num3_pushbutton_3.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.enigmatext_7 = QLabel(self.change_password_page)
        self.enigmatext_7.setObjectName(u"enigmatext_7")
        self.enigmatext_7.setGeometry(QRect(0, 10, 480, 51))
        self.enigmatext_7.setFont(font)
        self.enigmatext_7.setStyleSheet(u"color:rgba(255,255,255,255);\n"
"")
        self.enigmatext_7.setTextFormat(Qt.PlainText)
        self.enigmatext_7.setAlignment(Qt.AlignCenter)
        self.num9_pushbutton_3 = QPushButton(self.change_password_page)
        self.num9_pushbutton_3.setObjectName(u"num9_pushbutton_3")
        self.num9_pushbutton_3.setGeometry(QRect(320, 490, 100, 100))
        self.num9_pushbutton_3.setFont(font4)
        self.num9_pushbutton_3.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num0_pushbutton_3 = QPushButton(self.change_password_page)
        self.num0_pushbutton_3.setObjectName(u"num0_pushbutton_3")
        self.num0_pushbutton_3.setGeometry(QRect(190, 620, 100, 100))
        self.num0_pushbutton_3.setFont(font4)
        self.num0_pushbutton_3.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num1_pushbutton_3 = QPushButton(self.change_password_page)
        self.num1_pushbutton_3.setObjectName(u"num1_pushbutton_3")
        self.num1_pushbutton_3.setGeometry(QRect(60, 230, 100, 100))
        self.num1_pushbutton_3.setFont(font4)
        self.num1_pushbutton_3.setStyleSheet(u"\n"
"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num1_pushbutton_3.setIconSize(QSize(50, 50))
        self.num1_pushbutton_3.setAutoDefault(True)
        self.num1_pushbutton_3.setFlat(False)
        self.create_password_4 = QLineEdit(self.change_password_page)
        self.create_password_4.setObjectName(u"create_password_4")
        self.create_password_4.setGeometry(QRect(100, 130, 280, 60))
        self.create_password_4.setFont(font2)
        self.create_password_4.setFocusPolicy(Qt.NoFocus)
        self.create_password_4.setAutoFillBackground(False)
        self.create_password_4.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:3px solid rgba(237, 237, 237, 237);\n"
"color:rgba(237, 237, 237, 237);\n"
"padding-bottom:7px;\n"
"background-color: rgba(0, 0, 0, 0);")
        self.create_password_4.setFrame(True)
        self.create_password_4.setEchoMode(QLineEdit.Password)
        self.create_password_4.setAlignment(Qt.AlignCenter)
        self.create_password_4.setProperty("clearButtonEnabled", False)
        self.num2_pushbutton_3 = QPushButton(self.change_password_page)
        self.num2_pushbutton_3.setObjectName(u"num2_pushbutton_3")
        self.num2_pushbutton_3.setGeometry(QRect(190, 230, 100, 100))
        self.num2_pushbutton_3.setFont(font4)
        self.num2_pushbutton_3.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num6_pushbutton_3 = QPushButton(self.change_password_page)
        self.num6_pushbutton_3.setObjectName(u"num6_pushbutton_3")
        self.num6_pushbutton_3.setGeometry(QRect(320, 360, 100, 100))
        self.num6_pushbutton_3.setFont(font4)
        self.num6_pushbutton_3.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num8_pushbutton_3 = QPushButton(self.change_password_page)
        self.num8_pushbutton_3.setObjectName(u"num8_pushbutton_3")
        self.num8_pushbutton_3.setGeometry(QRect(190, 490, 100, 100))
        self.num8_pushbutton_3.setFont(font4)
        self.num8_pushbutton_3.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num7_pushbutton_3 = QPushButton(self.change_password_page)
        self.num7_pushbutton_3.setObjectName(u"num7_pushbutton_3")
        self.num7_pushbutton_3.setGeometry(QRect(60, 490, 100, 100))
        self.num7_pushbutton_3.setFont(font4)
        self.num7_pushbutton_3.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.background_7 = QLabel(self.change_password_page)
        self.background_7.setObjectName(u"background_7")
        self.background_7.setGeometry(QRect(0, 0, 480, 800))
        self.background_7.setStyleSheet(u"background-image: url(bg-vertical.png);")
        self.ent_pushbutton_3 = QPushButton(self.change_password_page)
        self.ent_pushbutton_3.setObjectName(u"ent_pushbutton_3")
        self.ent_pushbutton_3.setGeometry(QRect(320, 620, 100, 100))
        self.ent_pushbutton_3.setFont(font5)
        self.ent_pushbutton_3.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num4_pushbutton_3 = QPushButton(self.change_password_page)
        self.num4_pushbutton_3.setObjectName(u"num4_pushbutton_3")
        self.num4_pushbutton_3.setGeometry(QRect(60, 360, 100, 100))
        self.num4_pushbutton_3.setFont(font4)
        self.num4_pushbutton_3.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num4_pushbutton_3.setIconSize(QSize(50, 50))
        self.num4_pushbutton_3.setAutoDefault(False)
        self.num4_pushbutton_3.setFlat(True)
        self.num5_pushbutton_3 = QPushButton(self.change_password_page)
        self.num5_pushbutton_3.setObjectName(u"num5_pushbutton_3")
        self.num5_pushbutton_3.setGeometry(QRect(190, 360, 100, 100))
        self.num5_pushbutton_3.setFont(font4)
        self.num5_pushbutton_3.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.control1_pushbutton_3 = QPushButton(self.change_password_page)
        self.control1_pushbutton_3.setObjectName(u"control1_pushbutton_3")
        self.control1_pushbutton_3.setGeometry(QRect(70, 50, 30, 30))
        self.control1_pushbutton_3.setFont(font4)
        self.control1_pushbutton_3.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 15px; \n"
"        background-color: transparent; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(96, 96, 96, 96); \n"
" }")
        self.control1_pushbutton_3.setIconSize(QSize(50, 50))
        self.control1_pushbutton_3.setAutoDefault(True)
        self.control1_pushbutton_3.setFlat(False)
        self.del_pushbutton_3 = QPushButton(self.change_password_page)
        self.del_pushbutton_3.setObjectName(u"del_pushbutton_3")
        self.del_pushbutton_3.setGeometry(QRect(60, 620, 100, 100))
        self.del_pushbutton_3.setFont(font5)
        self.del_pushbutton_3.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.control1_pushbutton_4 = QPushButton(self.change_password_page)
        self.control1_pushbutton_4.setObjectName(u"control1_pushbutton_4")
        self.control1_pushbutton_4.setGeometry(QRect(20, 50, 30, 30))
        self.control1_pushbutton_4.setFont(font4)
        self.control1_pushbutton_4.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 15px; \n"
"        background-color: transparent; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(96, 96, 96, 96); \n"
" }")
        self.control1_pushbutton_4.setIconSize(QSize(50, 50))
        self.control1_pushbutton_4.setAutoDefault(True)
        self.control1_pushbutton_4.setFlat(False)
        self.stackedWidget.addWidget(self.change_password_page)
        self.background_7.raise_()
        self.control2_pushbutton_3.raise_()
        self.consoletext_8.raise_()
        self.num3_pushbutton_3.raise_()
        self.enigmatext_7.raise_()
        self.num9_pushbutton_3.raise_()
        self.num0_pushbutton_3.raise_()
        self.num1_pushbutton_3.raise_()
        self.create_password_4.raise_()
        self.num2_pushbutton_3.raise_()
        self.num6_pushbutton_3.raise_()
        self.num8_pushbutton_3.raise_()
        self.num7_pushbutton_3.raise_()
        self.ent_pushbutton_3.raise_()
        self.num4_pushbutton_3.raise_()
        self.num5_pushbutton_3.raise_()
        self.control1_pushbutton_3.raise_()
        self.del_pushbutton_3.raise_()
        self.control1_pushbutton_4.raise_()
        self.change_pw_new_pw = QWidget()
        self.change_pw_new_pw.setObjectName(u"change_pw_new_pw")
        self.enigmatext_8 = QLabel(self.change_pw_new_pw)
        self.enigmatext_8.setObjectName(u"enigmatext_8")
        self.enigmatext_8.setGeometry(QRect(0, 10, 480, 51))
        self.enigmatext_8.setFont(font)
        self.enigmatext_8.setStyleSheet(u"color:rgba(255,255,255,255);\n"
"")
        self.enigmatext_8.setTextFormat(Qt.PlainText)
        self.enigmatext_8.setAlignment(Qt.AlignCenter)
        self.create_password_5 = QLineEdit(self.change_pw_new_pw)
        self.create_password_5.setObjectName(u"create_password_5")
        self.create_password_5.setGeometry(QRect(100, 130, 280, 60))
        self.create_password_5.setFont(font2)
        self.create_password_5.setFocusPolicy(Qt.NoFocus)
        self.create_password_5.setAutoFillBackground(False)
        self.create_password_5.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:3px solid rgba(237, 237, 237, 237);\n"
"color:rgba(237, 237, 237, 237);\n"
"padding-bottom:7px;\n"
"background-color: rgba(0, 0, 0, 0);")
        self.create_password_5.setFrame(True)
        self.create_password_5.setEchoMode(QLineEdit.Password)
        self.create_password_5.setAlignment(Qt.AlignCenter)
        self.create_password_5.setProperty("clearButtonEnabled", False)
        self.num5_pushbutton_4 = QPushButton(self.change_pw_new_pw)
        self.num5_pushbutton_4.setObjectName(u"num5_pushbutton_4")
        self.num5_pushbutton_4.setGeometry(QRect(190, 360, 100, 100))
        self.num5_pushbutton_4.setFont(font4)
        self.num5_pushbutton_4.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.del_pushbutton_4 = QPushButton(self.change_pw_new_pw)
        self.del_pushbutton_4.setObjectName(u"del_pushbutton_4")
        self.del_pushbutton_4.setGeometry(QRect(60, 620, 100, 100))
        self.del_pushbutton_4.setFont(font5)
        self.del_pushbutton_4.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.control2_pushbutton_4 = QPushButton(self.change_pw_new_pw)
        self.control2_pushbutton_4.setObjectName(u"control2_pushbutton_4")
        self.control2_pushbutton_4.setGeometry(QRect(380, 50, 30, 30))
        self.control2_pushbutton_4.setFont(font4)
        self.control2_pushbutton_4.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 15px; \n"
"        background-color: transparent; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(96, 96, 96, 96); \n"
" }")
        self.control2_pushbutton_4.setIconSize(QSize(50, 50))
        self.control2_pushbutton_4.setAutoDefault(True)
        self.control2_pushbutton_4.setFlat(False)
        self.control1_pushbutton_5 = QPushButton(self.change_pw_new_pw)
        self.control1_pushbutton_5.setObjectName(u"control1_pushbutton_5")
        self.control1_pushbutton_5.setGeometry(QRect(20, 50, 30, 30))
        self.control1_pushbutton_5.setFont(font4)
        self.control1_pushbutton_5.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 15px; \n"
"        background-color: #00FF00; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(96, 96, 96, 96); \n"
" }")
        self.control1_pushbutton_5.setIconSize(QSize(50, 50))
        self.control1_pushbutton_5.setAutoDefault(True)
        self.control1_pushbutton_5.setFlat(False)
        self.control1_pushbutton_6 = QPushButton(self.change_pw_new_pw)
        self.control1_pushbutton_6.setObjectName(u"control1_pushbutton_6")
        self.control1_pushbutton_6.setGeometry(QRect(70, 50, 30, 30))
        self.control1_pushbutton_6.setFont(font4)
        self.control1_pushbutton_6.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 15px; \n"
"        background-color: transparent; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(96, 96, 96, 96); \n"
" }")
        self.control1_pushbutton_6.setIconSize(QSize(50, 50))
        self.control1_pushbutton_6.setAutoDefault(True)
        self.control1_pushbutton_6.setFlat(False)
        self.consoletext_9 = QLabel(self.change_pw_new_pw)
        self.consoletext_9.setObjectName(u"consoletext_9")
        self.consoletext_9.setGeometry(QRect(0, 60, 480, 51))
        self.consoletext_9.setFont(font1)
        self.consoletext_9.setStyleSheet(u"\n"
"color:rgba(255,255,255,255);")
        self.consoletext_9.setTextFormat(Qt.AutoText)
        self.consoletext_9.setAlignment(Qt.AlignCenter)
        self.num3_pushbutton_4 = QPushButton(self.change_pw_new_pw)
        self.num3_pushbutton_4.setObjectName(u"num3_pushbutton_4")
        self.num3_pushbutton_4.setGeometry(QRect(320, 230, 100, 100))
        self.num3_pushbutton_4.setFont(font4)
        self.num3_pushbutton_4.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num7_pushbutton_4 = QPushButton(self.change_pw_new_pw)
        self.num7_pushbutton_4.setObjectName(u"num7_pushbutton_4")
        self.num7_pushbutton_4.setGeometry(QRect(60, 490, 100, 100))
        self.num7_pushbutton_4.setFont(font4)
        self.num7_pushbutton_4.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num4_pushbutton_4 = QPushButton(self.change_pw_new_pw)
        self.num4_pushbutton_4.setObjectName(u"num4_pushbutton_4")
        self.num4_pushbutton_4.setGeometry(QRect(60, 360, 100, 100))
        self.num4_pushbutton_4.setFont(font4)
        self.num4_pushbutton_4.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num4_pushbutton_4.setIconSize(QSize(50, 50))
        self.num4_pushbutton_4.setAutoDefault(False)
        self.num4_pushbutton_4.setFlat(True)
        self.num9_pushbutton_4 = QPushButton(self.change_pw_new_pw)
        self.num9_pushbutton_4.setObjectName(u"num9_pushbutton_4")
        self.num9_pushbutton_4.setGeometry(QRect(320, 490, 100, 100))
        self.num9_pushbutton_4.setFont(font4)
        self.num9_pushbutton_4.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.ent_pushbutton_4 = QPushButton(self.change_pw_new_pw)
        self.ent_pushbutton_4.setObjectName(u"ent_pushbutton_4")
        self.ent_pushbutton_4.setGeometry(QRect(320, 620, 100, 100))
        self.ent_pushbutton_4.setFont(font5)
        self.ent_pushbutton_4.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num2_pushbutton_4 = QPushButton(self.change_pw_new_pw)
        self.num2_pushbutton_4.setObjectName(u"num2_pushbutton_4")
        self.num2_pushbutton_4.setGeometry(QRect(190, 230, 100, 100))
        self.num2_pushbutton_4.setFont(font4)
        self.num2_pushbutton_4.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num6_pushbutton_4 = QPushButton(self.change_pw_new_pw)
        self.num6_pushbutton_4.setObjectName(u"num6_pushbutton_4")
        self.num6_pushbutton_4.setGeometry(QRect(320, 360, 100, 100))
        self.num6_pushbutton_4.setFont(font4)
        self.num6_pushbutton_4.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num8_pushbutton_4 = QPushButton(self.change_pw_new_pw)
        self.num8_pushbutton_4.setObjectName(u"num8_pushbutton_4")
        self.num8_pushbutton_4.setGeometry(QRect(190, 490, 100, 100))
        self.num8_pushbutton_4.setFont(font4)
        self.num8_pushbutton_4.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num1_pushbutton_4 = QPushButton(self.change_pw_new_pw)
        self.num1_pushbutton_4.setObjectName(u"num1_pushbutton_4")
        self.num1_pushbutton_4.setGeometry(QRect(60, 230, 100, 100))
        self.num1_pushbutton_4.setFont(font4)
        self.num1_pushbutton_4.setStyleSheet(u"\n"
"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num1_pushbutton_4.setIconSize(QSize(50, 50))
        self.num1_pushbutton_4.setAutoDefault(True)
        self.num1_pushbutton_4.setFlat(False)
        self.num0_pushbutton_4 = QPushButton(self.change_pw_new_pw)
        self.num0_pushbutton_4.setObjectName(u"num0_pushbutton_4")
        self.num0_pushbutton_4.setGeometry(QRect(190, 620, 100, 100))
        self.num0_pushbutton_4.setFont(font4)
        self.num0_pushbutton_4.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.background_8 = QLabel(self.change_pw_new_pw)
        self.background_8.setObjectName(u"background_8")
        self.background_8.setGeometry(QRect(0, 0, 480, 800))
        self.background_8.setStyleSheet(u"background-image: url(bg-vertical.png);")
        self.stackedWidget.addWidget(self.change_pw_new_pw)
        self.background_8.raise_()
        self.enigmatext_8.raise_()
        self.create_password_5.raise_()
        self.num5_pushbutton_4.raise_()
        self.del_pushbutton_4.raise_()
        self.control2_pushbutton_4.raise_()
        self.control1_pushbutton_5.raise_()
        self.control1_pushbutton_6.raise_()
        self.consoletext_9.raise_()
        self.num3_pushbutton_4.raise_()
        self.num7_pushbutton_4.raise_()
        self.num4_pushbutton_4.raise_()
        self.num9_pushbutton_4.raise_()
        self.ent_pushbutton_4.raise_()
        self.num2_pushbutton_4.raise_()
        self.num6_pushbutton_4.raise_()
        self.num8_pushbutton_4.raise_()
        self.num1_pushbutton_4.raise_()
        self.num0_pushbutton_4.raise_()
        self.new_pw_confirm_pw = QWidget()
        self.new_pw_confirm_pw.setObjectName(u"new_pw_confirm_pw")
        self.num7_pushbutton_5 = QPushButton(self.new_pw_confirm_pw)
        self.num7_pushbutton_5.setObjectName(u"num7_pushbutton_5")
        self.num7_pushbutton_5.setGeometry(QRect(60, 490, 100, 100))
        self.num7_pushbutton_5.setFont(font4)
        self.num7_pushbutton_5.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.consoletext_10 = QLabel(self.new_pw_confirm_pw)
        self.consoletext_10.setObjectName(u"consoletext_10")
        self.consoletext_10.setGeometry(QRect(0, 60, 480, 51))
        self.consoletext_10.setFont(font1)
        self.consoletext_10.setStyleSheet(u"\n"
"color:rgba(255,255,255,255);")
        self.consoletext_10.setTextFormat(Qt.AutoText)
        self.consoletext_10.setAlignment(Qt.AlignCenter)
        self.enigmatext_9 = QLabel(self.new_pw_confirm_pw)
        self.enigmatext_9.setObjectName(u"enigmatext_9")
        self.enigmatext_9.setGeometry(QRect(0, 10, 480, 51))
        self.enigmatext_9.setFont(font)
        self.enigmatext_9.setStyleSheet(u"color:rgba(255,255,255,255);\n"
"")
        self.enigmatext_9.setTextFormat(Qt.PlainText)
        self.enigmatext_9.setAlignment(Qt.AlignCenter)
        self.num9_pushbutton_5 = QPushButton(self.new_pw_confirm_pw)
        self.num9_pushbutton_5.setObjectName(u"num9_pushbutton_5")
        self.num9_pushbutton_5.setGeometry(QRect(320, 490, 100, 100))
        self.num9_pushbutton_5.setFont(font4)
        self.num9_pushbutton_5.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num2_pushbutton_5 = QPushButton(self.new_pw_confirm_pw)
        self.num2_pushbutton_5.setObjectName(u"num2_pushbutton_5")
        self.num2_pushbutton_5.setGeometry(QRect(190, 230, 100, 100))
        self.num2_pushbutton_5.setFont(font4)
        self.num2_pushbutton_5.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.control1_pushbutton_7 = QPushButton(self.new_pw_confirm_pw)
        self.control1_pushbutton_7.setObjectName(u"control1_pushbutton_7")
        self.control1_pushbutton_7.setGeometry(QRect(20, 50, 30, 30))
        self.control1_pushbutton_7.setFont(font4)
        self.control1_pushbutton_7.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 15px; \n"
"        background-color: #00FF00; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(96, 96, 96, 96); \n"
" }")
        self.control1_pushbutton_7.setIconSize(QSize(50, 50))
        self.control1_pushbutton_7.setAutoDefault(True)
        self.control1_pushbutton_7.setFlat(False)
        self.del_pushbutton_5 = QPushButton(self.new_pw_confirm_pw)
        self.del_pushbutton_5.setObjectName(u"del_pushbutton_5")
        self.del_pushbutton_5.setGeometry(QRect(60, 620, 100, 100))
        self.del_pushbutton_5.setFont(font5)
        self.del_pushbutton_5.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num4_pushbutton_5 = QPushButton(self.new_pw_confirm_pw)
        self.num4_pushbutton_5.setObjectName(u"num4_pushbutton_5")
        self.num4_pushbutton_5.setGeometry(QRect(60, 360, 100, 100))
        self.num4_pushbutton_5.setFont(font4)
        self.num4_pushbutton_5.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num4_pushbutton_5.setIconSize(QSize(50, 50))
        self.num4_pushbutton_5.setAutoDefault(False)
        self.num4_pushbutton_5.setFlat(True)
        self.num6_pushbutton_5 = QPushButton(self.new_pw_confirm_pw)
        self.num6_pushbutton_5.setObjectName(u"num6_pushbutton_5")
        self.num6_pushbutton_5.setGeometry(QRect(320, 360, 100, 100))
        self.num6_pushbutton_5.setFont(font4)
        self.num6_pushbutton_5.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num1_pushbutton_5 = QPushButton(self.new_pw_confirm_pw)
        self.num1_pushbutton_5.setObjectName(u"num1_pushbutton_5")
        self.num1_pushbutton_5.setGeometry(QRect(60, 230, 100, 100))
        self.num1_pushbutton_5.setFont(font4)
        self.num1_pushbutton_5.setStyleSheet(u"\n"
"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num1_pushbutton_5.setIconSize(QSize(50, 50))
        self.num1_pushbutton_5.setAutoDefault(True)
        self.num1_pushbutton_5.setFlat(False)
        self.num8_pushbutton_5 = QPushButton(self.new_pw_confirm_pw)
        self.num8_pushbutton_5.setObjectName(u"num8_pushbutton_5")
        self.num8_pushbutton_5.setGeometry(QRect(190, 490, 100, 100))
        self.num8_pushbutton_5.setFont(font4)
        self.num8_pushbutton_5.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num0_pushbutton_5 = QPushButton(self.new_pw_confirm_pw)
        self.num0_pushbutton_5.setObjectName(u"num0_pushbutton_5")
        self.num0_pushbutton_5.setGeometry(QRect(190, 620, 100, 100))
        self.num0_pushbutton_5.setFont(font4)
        self.num0_pushbutton_5.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num3_pushbutton_5 = QPushButton(self.new_pw_confirm_pw)
        self.num3_pushbutton_5.setObjectName(u"num3_pushbutton_5")
        self.num3_pushbutton_5.setGeometry(QRect(320, 230, 100, 100))
        self.num3_pushbutton_5.setFont(font4)
        self.num3_pushbutton_5.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.control1_pushbutton_8 = QPushButton(self.new_pw_confirm_pw)
        self.control1_pushbutton_8.setObjectName(u"control1_pushbutton_8")
        self.control1_pushbutton_8.setGeometry(QRect(70, 50, 30, 30))
        self.control1_pushbutton_8.setFont(font4)
        self.control1_pushbutton_8.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 15px; \n"
"        background-color: #00FF00; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(96, 96, 96, 96); \n"
" }")
        self.control1_pushbutton_8.setIconSize(QSize(50, 50))
        self.control1_pushbutton_8.setAutoDefault(True)
        self.control1_pushbutton_8.setFlat(False)
        self.num5_pushbutton_5 = QPushButton(self.new_pw_confirm_pw)
        self.num5_pushbutton_5.setObjectName(u"num5_pushbutton_5")
        self.num5_pushbutton_5.setGeometry(QRect(190, 360, 100, 100))
        self.num5_pushbutton_5.setFont(font4)
        self.num5_pushbutton_5.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.ent_pushbutton_5 = QPushButton(self.new_pw_confirm_pw)
        self.ent_pushbutton_5.setObjectName(u"ent_pushbutton_5")
        self.ent_pushbutton_5.setGeometry(QRect(320, 620, 100, 100))
        self.ent_pushbutton_5.setFont(font5)
        self.ent_pushbutton_5.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.background_9 = QLabel(self.new_pw_confirm_pw)
        self.background_9.setObjectName(u"background_9")
        self.background_9.setGeometry(QRect(0, 0, 480, 800))
        self.background_9.setStyleSheet(u"background-image: url(bg-vertical.png);")
        self.create_password_6 = QLineEdit(self.new_pw_confirm_pw)
        self.create_password_6.setObjectName(u"create_password_6")
        self.create_password_6.setGeometry(QRect(100, 130, 280, 60))
        self.create_password_6.setFont(font2)
        self.create_password_6.setFocusPolicy(Qt.NoFocus)
        self.create_password_6.setAutoFillBackground(False)
        self.create_password_6.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:3px solid rgba(237, 237, 237, 237);\n"
"color:rgba(237, 237, 237, 237);\n"
"padding-bottom:7px;\n"
"background-color: rgba(0, 0, 0, 0);")
        self.create_password_6.setFrame(True)
        self.create_password_6.setEchoMode(QLineEdit.Password)
        self.create_password_6.setAlignment(Qt.AlignCenter)
        self.create_password_6.setProperty("clearButtonEnabled", False)
        self.control2_pushbutton_5 = QPushButton(self.new_pw_confirm_pw)
        self.control2_pushbutton_5.setObjectName(u"control2_pushbutton_5")
        self.control2_pushbutton_5.setGeometry(QRect(380, 50, 30, 30))
        self.control2_pushbutton_5.setFont(font4)
        self.control2_pushbutton_5.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 15px; \n"
"        background-color: transparent; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(96, 96, 96, 96); \n"
" }")
        self.control2_pushbutton_5.setIconSize(QSize(50, 50))
        self.control2_pushbutton_5.setAutoDefault(True)
        self.control2_pushbutton_5.setFlat(False)
        self.stackedWidget.addWidget(self.new_pw_confirm_pw)
        self.background_9.raise_()
        self.num7_pushbutton_5.raise_()
        self.consoletext_10.raise_()
        self.enigmatext_9.raise_()
        self.num9_pushbutton_5.raise_()
        self.num2_pushbutton_5.raise_()
        self.control1_pushbutton_7.raise_()
        self.del_pushbutton_5.raise_()
        self.num4_pushbutton_5.raise_()
        self.num6_pushbutton_5.raise_()
        self.num1_pushbutton_5.raise_()
        self.num8_pushbutton_5.raise_()
        self.num0_pushbutton_5.raise_()
        self.num3_pushbutton_5.raise_()
        self.control1_pushbutton_8.raise_()
        self.num5_pushbutton_5.raise_()
        self.ent_pushbutton_5.raise_()
        self.create_password_6.raise_()
        self.control2_pushbutton_5.raise_()
        self.new_pw_done_page = QWidget()
        self.new_pw_done_page.setObjectName(u"new_pw_done_page")
        self.security_text_2 = QLabel(self.new_pw_done_page)
        self.security_text_2.setObjectName(u"security_text_2")
        self.security_text_2.setGeometry(QRect(0, 340, 480, 51))
        self.security_text_2.setFont(font7)
        self.security_text_2.setStyleSheet(u"color:rgba(255,255,255,255);\n"
"")
        self.security_text_2.setTextFormat(Qt.PlainText)
        self.security_text_2.setAlignment(Qt.AlignCenter)
        self.finish_text_2 = QLabel(self.new_pw_done_page)
        self.finish_text_2.setObjectName(u"finish_text_2")
        self.finish_text_2.setGeometry(QRect(0, 250, 480, 51))
        self.finish_text_2.setFont(font6)
        self.finish_text_2.setStyleSheet(u"color:rgba(255,255,255,255);\n"
"")
        self.finish_text_2.setTextFormat(Qt.PlainText)
        self.finish_text_2.setAlignment(Qt.AlignCenter)
        self.continue_button_2 = QPushButton(self.new_pw_done_page)
        self.continue_button_2.setObjectName(u"continue_button_2")
        self.continue_button_2.setEnabled(True)
        self.continue_button_2.setGeometry(QRect(200, 630, 80, 80))
        sizePolicy.setHeightForWidth(self.continue_button_2.sizePolicy().hasHeightForWidth())
        self.continue_button_2.setSizePolicy(sizePolicy)
        self.continue_button_2.setFont(font10)
        self.continue_button_2.setLayoutDirection(Qt.LeftToRight)
        self.continue_button_2.setStyleSheet(u"QPushButton {\n"
" border-radius: 40px; \n"
"\n"
"\n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }\n"
"")
        self.continue_button_2.setIcon(icon)
        self.continue_button_2.setIconSize(QSize(80, 80))
        self.continue_button_2.setCheckable(False)
        self.continue_button_2.setAutoRepeat(False)
        self.enigmatext_10 = QLabel(self.new_pw_done_page)
        self.enigmatext_10.setObjectName(u"enigmatext_10")
        self.enigmatext_10.setGeometry(QRect(0, 100, 480, 51))
        self.enigmatext_10.setFont(font)
        self.enigmatext_10.setStyleSheet(u"color:rgba(255,255,255,255);\n"
"")
        self.enigmatext_10.setTextFormat(Qt.PlainText)
        self.enigmatext_10.setAlignment(Qt.AlignCenter)
        self.background_10 = QLabel(self.new_pw_done_page)
        self.background_10.setObjectName(u"background_10")
        self.background_10.setGeometry(QRect(0, 0, 480, 800))
        self.background_10.setStyleSheet(u"background-image: url(bg-vertical.png);")
        self.info_text_2 = QLabel(self.new_pw_done_page)
        self.info_text_2.setObjectName(u"info_text_2")
        self.info_text_2.setGeometry(QRect(90, 490, 311, 131))
        self.info_text_2.setFont(font9)
        self.info_text_2.setLayoutDirection(Qt.LeftToRight)
        self.info_text_2.setAutoFillBackground(False)
        self.info_text_2.setStyleSheet(u"color:rgba(255,255,255,255);\n"
"")
        self.info_text_2.setTextFormat(Qt.AutoText)
        self.info_text_2.setScaledContents(False)
        self.info_text_2.setAlignment(Qt.AlignCenter)
        self.info_text_2.setWordWrap(True)
        self.securit_code_label_2 = QLineEdit(self.new_pw_done_page)
        self.securit_code_label_2.setObjectName(u"securit_code_label_2")
        self.securit_code_label_2.setGeometry(QRect(100, 410, 280, 60))
        self.securit_code_label_2.setFont(font8)
        self.securit_code_label_2.setFocusPolicy(Qt.NoFocus)
        self.securit_code_label_2.setAutoFillBackground(False)
        self.securit_code_label_2.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:3px solid rgba(237, 237, 237, 237);\n"
"color:rgba(237, 237, 237, 237);\n"
"padding-bottom:7px;\n"
"background-color: rgba(0, 0, 0, 0);")
        self.securit_code_label_2.setFrame(True)
        self.securit_code_label_2.setEchoMode(QLineEdit.Normal)
        self.securit_code_label_2.setAlignment(Qt.AlignCenter)
        self.securit_code_label_2.setReadOnly(True)
        self.securit_code_label_2.setProperty("clearButtonEnabled", False)
        self.consoletext_11 = QLabel(self.new_pw_done_page)
        self.consoletext_11.setObjectName(u"consoletext_11")
        self.consoletext_11.setGeometry(QRect(0, 150, 480, 51))
        self.consoletext_11.setFont(font1)
        self.consoletext_11.setStyleSheet(u"color:rgba(255,255,255,255);\n"
"")
        self.consoletext_11.setTextFormat(Qt.AutoText)
        self.consoletext_11.setAlignment(Qt.AlignCenter)
        self.security_text_3 = QLabel(self.new_pw_done_page)
        self.security_text_3.setObjectName(u"security_text_3")
        self.security_text_3.setGeometry(QRect(0, 300, 480, 51))
        font15 = QFont()
        font15.setFamily(u"Montserrat SemiBold")
        font15.setPointSize(12)
        font15.setBold(False)
        font15.setItalic(True)
        font15.setWeight(50)
        self.security_text_3.setFont(font15)
        self.security_text_3.setStyleSheet(u"color:rgba(255,255,255,255);\n"
"")
        self.security_text_3.setTextFormat(Qt.PlainText)
        self.security_text_3.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.new_pw_done_page)
        self.background_10.raise_()
        self.security_text_2.raise_()
        self.finish_text_2.raise_()
        self.continue_button_2.raise_()
        self.enigmatext_10.raise_()
        self.info_text_2.raise_()
        self.securit_code_label_2.raise_()
        self.consoletext_11.raise_()
        self.security_text_3.raise_()
        self.securitycode_change_pw = QWidget()
        self.securitycode_change_pw.setObjectName(u"securitycode_change_pw")
        self.enigmatext_11 = QLabel(self.securitycode_change_pw)
        self.enigmatext_11.setObjectName(u"enigmatext_11")
        self.enigmatext_11.setGeometry(QRect(0, 10, 480, 51))
        self.enigmatext_11.setFont(font)
        self.enigmatext_11.setStyleSheet(u"color:rgba(255,255,255,255);\n"
"")
        self.enigmatext_11.setTextFormat(Qt.PlainText)
        self.enigmatext_11.setAlignment(Qt.AlignCenter)
        self.create_password_7 = QLineEdit(self.securitycode_change_pw)
        self.create_password_7.setObjectName(u"create_password_7")
        self.create_password_7.setGeometry(QRect(100, 130, 280, 60))
        self.create_password_7.setFont(font2)
        self.create_password_7.setFocusPolicy(Qt.NoFocus)
        self.create_password_7.setAutoFillBackground(False)
        self.create_password_7.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:3px solid rgba(237, 237, 237, 237);\n"
"color:rgba(237, 237, 237, 237);\n"
"padding-bottom:7px;\n"
"background-color: rgba(0, 0, 0, 0);")
        self.create_password_7.setFrame(True)
        self.create_password_7.setEchoMode(QLineEdit.Normal)
        self.create_password_7.setAlignment(Qt.AlignCenter)
        self.create_password_7.setProperty("clearButtonEnabled", False)
        self.num5_pushbutton_6 = QPushButton(self.securitycode_change_pw)
        self.num5_pushbutton_6.setObjectName(u"num5_pushbutton_6")
        self.num5_pushbutton_6.setGeometry(QRect(190, 360, 100, 100))
        self.num5_pushbutton_6.setFont(font4)
        self.num5_pushbutton_6.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.del_pushbutton_6 = QPushButton(self.securitycode_change_pw)
        self.del_pushbutton_6.setObjectName(u"del_pushbutton_6")
        self.del_pushbutton_6.setGeometry(QRect(60, 620, 100, 100))
        self.del_pushbutton_6.setFont(font5)
        self.del_pushbutton_6.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.control2_pushbutton_6 = QPushButton(self.securitycode_change_pw)
        self.control2_pushbutton_6.setObjectName(u"control2_pushbutton_6")
        self.control2_pushbutton_6.setGeometry(QRect(380, 50, 30, 30))
        self.control2_pushbutton_6.setFont(font4)
        self.control2_pushbutton_6.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 15px; \n"
"        background-color: transparent; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(96, 96, 96, 96); \n"
" }")
        self.control2_pushbutton_6.setIconSize(QSize(50, 50))
        self.control2_pushbutton_6.setAutoDefault(True)
        self.control2_pushbutton_6.setFlat(False)
        self.control1_pushbutton_9 = QPushButton(self.securitycode_change_pw)
        self.control1_pushbutton_9.setObjectName(u"control1_pushbutton_9")
        self.control1_pushbutton_9.setGeometry(QRect(20, 50, 30, 30))
        self.control1_pushbutton_9.setFont(font4)
        self.control1_pushbutton_9.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 15px; \n"
"        background-color: transparent; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(96, 96, 96, 96); \n"
" }")
        self.control1_pushbutton_9.setIconSize(QSize(50, 50))
        self.control1_pushbutton_9.setAutoDefault(True)
        self.control1_pushbutton_9.setFlat(False)
        self.control1_pushbutton_10 = QPushButton(self.securitycode_change_pw)
        self.control1_pushbutton_10.setObjectName(u"control1_pushbutton_10")
        self.control1_pushbutton_10.setGeometry(QRect(70, 50, 30, 30))
        self.control1_pushbutton_10.setFont(font4)
        self.control1_pushbutton_10.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 15px; \n"
"        background-color: transparent; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(96, 96, 96, 96); \n"
" }")
        self.control1_pushbutton_10.setIconSize(QSize(50, 50))
        self.control1_pushbutton_10.setAutoDefault(True)
        self.control1_pushbutton_10.setFlat(False)
        self.consoletext_12 = QLabel(self.securitycode_change_pw)
        self.consoletext_12.setObjectName(u"consoletext_12")
        self.consoletext_12.setGeometry(QRect(0, 60, 480, 51))
        self.consoletext_12.setFont(font1)
        self.consoletext_12.setStyleSheet(u"\n"
"color:rgba(255,255,255,255);")
        self.consoletext_12.setTextFormat(Qt.AutoText)
        self.consoletext_12.setAlignment(Qt.AlignCenter)
        self.num3_pushbutton_6 = QPushButton(self.securitycode_change_pw)
        self.num3_pushbutton_6.setObjectName(u"num3_pushbutton_6")
        self.num3_pushbutton_6.setGeometry(QRect(320, 230, 100, 100))
        self.num3_pushbutton_6.setFont(font4)
        self.num3_pushbutton_6.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num7_pushbutton_6 = QPushButton(self.securitycode_change_pw)
        self.num7_pushbutton_6.setObjectName(u"num7_pushbutton_6")
        self.num7_pushbutton_6.setGeometry(QRect(60, 490, 100, 100))
        self.num7_pushbutton_6.setFont(font4)
        self.num7_pushbutton_6.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num4_pushbutton_6 = QPushButton(self.securitycode_change_pw)
        self.num4_pushbutton_6.setObjectName(u"num4_pushbutton_6")
        self.num4_pushbutton_6.setGeometry(QRect(60, 360, 100, 100))
        self.num4_pushbutton_6.setFont(font4)
        self.num4_pushbutton_6.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num4_pushbutton_6.setIconSize(QSize(50, 50))
        self.num4_pushbutton_6.setAutoDefault(False)
        self.num4_pushbutton_6.setFlat(True)
        self.num9_pushbutton_6 = QPushButton(self.securitycode_change_pw)
        self.num9_pushbutton_6.setObjectName(u"num9_pushbutton_6")
        self.num9_pushbutton_6.setGeometry(QRect(320, 490, 100, 100))
        self.num9_pushbutton_6.setFont(font4)
        self.num9_pushbutton_6.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.ent_pushbutton_6 = QPushButton(self.securitycode_change_pw)
        self.ent_pushbutton_6.setObjectName(u"ent_pushbutton_6")
        self.ent_pushbutton_6.setGeometry(QRect(320, 620, 100, 100))
        self.ent_pushbutton_6.setFont(font5)
        self.ent_pushbutton_6.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num2_pushbutton_6 = QPushButton(self.securitycode_change_pw)
        self.num2_pushbutton_6.setObjectName(u"num2_pushbutton_6")
        self.num2_pushbutton_6.setGeometry(QRect(190, 230, 100, 100))
        self.num2_pushbutton_6.setFont(font4)
        self.num2_pushbutton_6.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num6_pushbutton_6 = QPushButton(self.securitycode_change_pw)
        self.num6_pushbutton_6.setObjectName(u"num6_pushbutton_6")
        self.num6_pushbutton_6.setGeometry(QRect(320, 360, 100, 100))
        self.num6_pushbutton_6.setFont(font4)
        self.num6_pushbutton_6.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num1_pushbutton_6 = QPushButton(self.securitycode_change_pw)
        self.num1_pushbutton_6.setObjectName(u"num1_pushbutton_6")
        self.num1_pushbutton_6.setGeometry(QRect(60, 230, 100, 100))
        self.num1_pushbutton_6.setFont(font4)
        self.num1_pushbutton_6.setStyleSheet(u"\n"
"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num1_pushbutton_6.setIconSize(QSize(50, 50))
        self.num1_pushbutton_6.setAutoDefault(True)
        self.num1_pushbutton_6.setFlat(False)
        self.num8_pushbutton_6 = QPushButton(self.securitycode_change_pw)
        self.num8_pushbutton_6.setObjectName(u"num8_pushbutton_6")
        self.num8_pushbutton_6.setGeometry(QRect(190, 490, 100, 100))
        self.num8_pushbutton_6.setFont(font4)
        self.num8_pushbutton_6.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num0_pushbutton_6 = QPushButton(self.securitycode_change_pw)
        self.num0_pushbutton_6.setObjectName(u"num0_pushbutton_6")
        self.num0_pushbutton_6.setGeometry(QRect(190, 620, 100, 100))
        self.num0_pushbutton_6.setFont(font4)
        self.num0_pushbutton_6.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.background_11 = QLabel(self.securitycode_change_pw)
        self.background_11.setObjectName(u"background_11")
        self.background_11.setGeometry(QRect(0, 0, 480, 800))
        self.background_11.setStyleSheet(u"background-image: url(bg-vertical.png);")
        self.stackedWidget.addWidget(self.securitycode_change_pw)
        self.background_11.raise_()
        self.enigmatext_11.raise_()
        self.create_password_7.raise_()
        self.num5_pushbutton_6.raise_()
        self.del_pushbutton_6.raise_()
        self.control2_pushbutton_6.raise_()
        self.control1_pushbutton_9.raise_()
        self.control1_pushbutton_10.raise_()
        self.consoletext_12.raise_()
        self.num3_pushbutton_6.raise_()
        self.num7_pushbutton_6.raise_()
        self.num4_pushbutton_6.raise_()
        self.num9_pushbutton_6.raise_()
        self.ent_pushbutton_6.raise_()
        self.num2_pushbutton_6.raise_()
        self.num6_pushbutton_6.raise_()
        self.num1_pushbutton_6.raise_()
        self.num8_pushbutton_6.raise_()
        self.num0_pushbutton_6.raise_()
        self.securitycode_change_pw2 = QWidget()
        self.securitycode_change_pw2.setObjectName(u"securitycode_change_pw2")
        self.num7_pushbutton_7 = QPushButton(self.securitycode_change_pw2)
        self.num7_pushbutton_7.setObjectName(u"num7_pushbutton_7")
        self.num7_pushbutton_7.setGeometry(QRect(60, 490, 100, 100))
        self.num7_pushbutton_7.setFont(font4)
        self.num7_pushbutton_7.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.consoletext_13 = QLabel(self.securitycode_change_pw2)
        self.consoletext_13.setObjectName(u"consoletext_13")
        self.consoletext_13.setGeometry(QRect(0, 60, 480, 51))
        self.consoletext_13.setFont(font1)
        self.consoletext_13.setStyleSheet(u"\n"
"color:rgba(255,255,255,255);")
        self.consoletext_13.setTextFormat(Qt.AutoText)
        self.consoletext_13.setAlignment(Qt.AlignCenter)
        self.enigmatext_12 = QLabel(self.securitycode_change_pw2)
        self.enigmatext_12.setObjectName(u"enigmatext_12")
        self.enigmatext_12.setGeometry(QRect(0, 10, 480, 51))
        self.enigmatext_12.setFont(font)
        self.enigmatext_12.setStyleSheet(u"color:rgba(255,255,255,255);\n"
"")
        self.enigmatext_12.setTextFormat(Qt.PlainText)
        self.enigmatext_12.setAlignment(Qt.AlignCenter)
        self.num9_pushbutton_7 = QPushButton(self.securitycode_change_pw2)
        self.num9_pushbutton_7.setObjectName(u"num9_pushbutton_7")
        self.num9_pushbutton_7.setGeometry(QRect(320, 490, 100, 100))
        self.num9_pushbutton_7.setFont(font4)
        self.num9_pushbutton_7.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num2_pushbutton_7 = QPushButton(self.securitycode_change_pw2)
        self.num2_pushbutton_7.setObjectName(u"num2_pushbutton_7")
        self.num2_pushbutton_7.setGeometry(QRect(190, 230, 100, 100))
        self.num2_pushbutton_7.setFont(font4)
        self.num2_pushbutton_7.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.control1_pushbutton_11 = QPushButton(self.securitycode_change_pw2)
        self.control1_pushbutton_11.setObjectName(u"control1_pushbutton_11")
        self.control1_pushbutton_11.setGeometry(QRect(20, 50, 30, 30))
        self.control1_pushbutton_11.setFont(font4)
        self.control1_pushbutton_11.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 15px; \n"
"        background-color: #00FF00; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(96, 96, 96, 96); \n"
" }")
        self.control1_pushbutton_11.setIconSize(QSize(50, 50))
        self.control1_pushbutton_11.setAutoDefault(True)
        self.control1_pushbutton_11.setFlat(False)
        self.del_pushbutton_7 = QPushButton(self.securitycode_change_pw2)
        self.del_pushbutton_7.setObjectName(u"del_pushbutton_7")
        self.del_pushbutton_7.setGeometry(QRect(60, 620, 100, 100))
        self.del_pushbutton_7.setFont(font5)
        self.del_pushbutton_7.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num4_pushbutton_7 = QPushButton(self.securitycode_change_pw2)
        self.num4_pushbutton_7.setObjectName(u"num4_pushbutton_7")
        self.num4_pushbutton_7.setGeometry(QRect(60, 360, 100, 100))
        self.num4_pushbutton_7.setFont(font4)
        self.num4_pushbutton_7.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num4_pushbutton_7.setIconSize(QSize(50, 50))
        self.num4_pushbutton_7.setAutoDefault(False)
        self.num4_pushbutton_7.setFlat(True)
        self.num6_pushbutton_7 = QPushButton(self.securitycode_change_pw2)
        self.num6_pushbutton_7.setObjectName(u"num6_pushbutton_7")
        self.num6_pushbutton_7.setGeometry(QRect(320, 360, 100, 100))
        self.num6_pushbutton_7.setFont(font4)
        self.num6_pushbutton_7.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num1_pushbutton_7 = QPushButton(self.securitycode_change_pw2)
        self.num1_pushbutton_7.setObjectName(u"num1_pushbutton_7")
        self.num1_pushbutton_7.setGeometry(QRect(60, 230, 100, 100))
        self.num1_pushbutton_7.setFont(font4)
        self.num1_pushbutton_7.setStyleSheet(u"\n"
"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num1_pushbutton_7.setIconSize(QSize(50, 50))
        self.num1_pushbutton_7.setAutoDefault(True)
        self.num1_pushbutton_7.setFlat(False)
        self.num8_pushbutton_7 = QPushButton(self.securitycode_change_pw2)
        self.num8_pushbutton_7.setObjectName(u"num8_pushbutton_7")
        self.num8_pushbutton_7.setGeometry(QRect(190, 490, 100, 100))
        self.num8_pushbutton_7.setFont(font4)
        self.num8_pushbutton_7.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num0_pushbutton_7 = QPushButton(self.securitycode_change_pw2)
        self.num0_pushbutton_7.setObjectName(u"num0_pushbutton_7")
        self.num0_pushbutton_7.setGeometry(QRect(190, 620, 100, 100))
        self.num0_pushbutton_7.setFont(font4)
        self.num0_pushbutton_7.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num3_pushbutton_7 = QPushButton(self.securitycode_change_pw2)
        self.num3_pushbutton_7.setObjectName(u"num3_pushbutton_7")
        self.num3_pushbutton_7.setGeometry(QRect(320, 230, 100, 100))
        self.num3_pushbutton_7.setFont(font4)
        self.num3_pushbutton_7.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.control1_pushbutton_12 = QPushButton(self.securitycode_change_pw2)
        self.control1_pushbutton_12.setObjectName(u"control1_pushbutton_12")
        self.control1_pushbutton_12.setGeometry(QRect(70, 50, 30, 30))
        self.control1_pushbutton_12.setFont(font4)
        self.control1_pushbutton_12.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 15px; \n"
"        background-color: transparent; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(96, 96, 96, 96); \n"
" }")
        self.control1_pushbutton_12.setIconSize(QSize(50, 50))
        self.control1_pushbutton_12.setAutoDefault(True)
        self.control1_pushbutton_12.setFlat(False)
        self.num5_pushbutton_7 = QPushButton(self.securitycode_change_pw2)
        self.num5_pushbutton_7.setObjectName(u"num5_pushbutton_7")
        self.num5_pushbutton_7.setGeometry(QRect(190, 360, 100, 100))
        self.num5_pushbutton_7.setFont(font4)
        self.num5_pushbutton_7.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.ent_pushbutton_7 = QPushButton(self.securitycode_change_pw2)
        self.ent_pushbutton_7.setObjectName(u"ent_pushbutton_7")
        self.ent_pushbutton_7.setGeometry(QRect(320, 620, 100, 100))
        self.ent_pushbutton_7.setFont(font5)
        self.ent_pushbutton_7.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.background_12 = QLabel(self.securitycode_change_pw2)
        self.background_12.setObjectName(u"background_12")
        self.background_12.setGeometry(QRect(0, 0, 480, 800))
        self.background_12.setStyleSheet(u"background-image: url(bg-vertical.png);")
        self.create_password_8 = QLineEdit(self.securitycode_change_pw2)
        self.create_password_8.setObjectName(u"create_password_8")
        self.create_password_8.setGeometry(QRect(100, 130, 280, 60))
        self.create_password_8.setFont(font2)
        self.create_password_8.setAutoFillBackground(False)
        self.create_password_8.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:3px solid rgba(237, 237, 237, 237);\n"
"color:rgba(237, 237, 237, 237);\n"
"padding-bottom:7px;\n"
"background-color: rgba(0, 0, 0, 0);")
        self.create_password_8.setFrame(True)
        self.create_password_8.setEchoMode(QLineEdit.Password)
        self.create_password_8.setAlignment(Qt.AlignCenter)
        self.create_password_8.setProperty("clearButtonEnabled", False)
        self.control2_pushbutton_7 = QPushButton(self.securitycode_change_pw2)
        self.control2_pushbutton_7.setObjectName(u"control2_pushbutton_7")
        self.control2_pushbutton_7.setGeometry(QRect(380, 50, 30, 30))
        self.control2_pushbutton_7.setFont(font4)
        self.control2_pushbutton_7.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 15px; \n"
"        background-color: transparent; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(96, 96, 96, 96); \n"
" }")
        self.control2_pushbutton_7.setIconSize(QSize(50, 50))
        self.control2_pushbutton_7.setAutoDefault(True)
        self.control2_pushbutton_7.setFlat(False)
        self.stackedWidget.addWidget(self.securitycode_change_pw2)
        self.background_12.raise_()
        self.num7_pushbutton_7.raise_()
        self.consoletext_13.raise_()
        self.enigmatext_12.raise_()
        self.num9_pushbutton_7.raise_()
        self.num2_pushbutton_7.raise_()
        self.control1_pushbutton_11.raise_()
        self.del_pushbutton_7.raise_()
        self.num4_pushbutton_7.raise_()
        self.num6_pushbutton_7.raise_()
        self.num1_pushbutton_7.raise_()
        self.num8_pushbutton_7.raise_()
        self.num0_pushbutton_7.raise_()
        self.num3_pushbutton_7.raise_()
        self.control1_pushbutton_12.raise_()
        self.num5_pushbutton_7.raise_()
        self.ent_pushbutton_7.raise_()
        self.create_password_8.raise_()
        self.control2_pushbutton_7.raise_()
        self.securitycode_change_pw3 = QWidget()
        self.securitycode_change_pw3.setObjectName(u"securitycode_change_pw3")
        self.control1_pushbutton_13 = QPushButton(self.securitycode_change_pw3)
        self.control1_pushbutton_13.setObjectName(u"control1_pushbutton_13")
        self.control1_pushbutton_13.setGeometry(QRect(70, 50, 30, 30))
        self.control1_pushbutton_13.setFont(font4)
        self.control1_pushbutton_13.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 15px; \n"
"        background-color: #00FF00; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(96, 96, 96, 96); \n"
" }")
        self.control1_pushbutton_13.setIconSize(QSize(50, 50))
        self.control1_pushbutton_13.setAutoDefault(True)
        self.control1_pushbutton_13.setFlat(False)
        self.control2_pushbutton_8 = QPushButton(self.securitycode_change_pw3)
        self.control2_pushbutton_8.setObjectName(u"control2_pushbutton_8")
        self.control2_pushbutton_8.setGeometry(QRect(380, 50, 30, 30))
        self.control2_pushbutton_8.setFont(font4)
        self.control2_pushbutton_8.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 15px; \n"
"        background-color: transparent; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(96, 96, 96, 96); \n"
" }")
        self.control2_pushbutton_8.setIconSize(QSize(50, 50))
        self.control2_pushbutton_8.setAutoDefault(True)
        self.control2_pushbutton_8.setFlat(False)
        self.control1_pushbutton_14 = QPushButton(self.securitycode_change_pw3)
        self.control1_pushbutton_14.setObjectName(u"control1_pushbutton_14")
        self.control1_pushbutton_14.setGeometry(QRect(20, 50, 30, 30))
        self.control1_pushbutton_14.setFont(font4)
        self.control1_pushbutton_14.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 15px; \n"
"        background-color: #00FF00; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(96, 96, 96, 96); \n"
" }")
        self.control1_pushbutton_14.setIconSize(QSize(50, 50))
        self.control1_pushbutton_14.setAutoDefault(True)
        self.control1_pushbutton_14.setFlat(False)
        self.num9_pushbutton_8 = QPushButton(self.securitycode_change_pw3)
        self.num9_pushbutton_8.setObjectName(u"num9_pushbutton_8")
        self.num9_pushbutton_8.setGeometry(QRect(320, 490, 100, 100))
        self.num9_pushbutton_8.setFont(font4)
        self.num9_pushbutton_8.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num8_pushbutton_8 = QPushButton(self.securitycode_change_pw3)
        self.num8_pushbutton_8.setObjectName(u"num8_pushbutton_8")
        self.num8_pushbutton_8.setGeometry(QRect(190, 490, 100, 100))
        self.num8_pushbutton_8.setFont(font4)
        self.num8_pushbutton_8.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num0_pushbutton_8 = QPushButton(self.securitycode_change_pw3)
        self.num0_pushbutton_8.setObjectName(u"num0_pushbutton_8")
        self.num0_pushbutton_8.setGeometry(QRect(190, 620, 100, 100))
        self.num0_pushbutton_8.setFont(font4)
        self.num0_pushbutton_8.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num4_pushbutton_8 = QPushButton(self.securitycode_change_pw3)
        self.num4_pushbutton_8.setObjectName(u"num4_pushbutton_8")
        self.num4_pushbutton_8.setGeometry(QRect(60, 360, 100, 100))
        self.num4_pushbutton_8.setFont(font4)
        self.num4_pushbutton_8.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num4_pushbutton_8.setIconSize(QSize(50, 50))
        self.num4_pushbutton_8.setAutoDefault(False)
        self.num4_pushbutton_8.setFlat(True)
        self.num5_pushbutton_8 = QPushButton(self.securitycode_change_pw3)
        self.num5_pushbutton_8.setObjectName(u"num5_pushbutton_8")
        self.num5_pushbutton_8.setGeometry(QRect(190, 360, 100, 100))
        self.num5_pushbutton_8.setFont(font4)
        self.num5_pushbutton_8.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num3_pushbutton_8 = QPushButton(self.securitycode_change_pw3)
        self.num3_pushbutton_8.setObjectName(u"num3_pushbutton_8")
        self.num3_pushbutton_8.setGeometry(QRect(320, 230, 100, 100))
        self.num3_pushbutton_8.setFont(font4)
        self.num3_pushbutton_8.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.ent_pushbutton_8 = QPushButton(self.securitycode_change_pw3)
        self.ent_pushbutton_8.setObjectName(u"ent_pushbutton_8")
        self.ent_pushbutton_8.setGeometry(QRect(320, 620, 100, 100))
        self.ent_pushbutton_8.setFont(font5)
        self.ent_pushbutton_8.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num7_pushbutton_8 = QPushButton(self.securitycode_change_pw3)
        self.num7_pushbutton_8.setObjectName(u"num7_pushbutton_8")
        self.num7_pushbutton_8.setGeometry(QRect(60, 490, 100, 100))
        self.num7_pushbutton_8.setFont(font4)
        self.num7_pushbutton_8.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num6_pushbutton_8 = QPushButton(self.securitycode_change_pw3)
        self.num6_pushbutton_8.setObjectName(u"num6_pushbutton_8")
        self.num6_pushbutton_8.setGeometry(QRect(320, 360, 100, 100))
        self.num6_pushbutton_8.setFont(font4)
        self.num6_pushbutton_8.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.del_pushbutton_8 = QPushButton(self.securitycode_change_pw3)
        self.del_pushbutton_8.setObjectName(u"del_pushbutton_8")
        self.del_pushbutton_8.setGeometry(QRect(60, 620, 100, 100))
        self.del_pushbutton_8.setFont(font5)
        self.del_pushbutton_8.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num2_pushbutton_8 = QPushButton(self.securitycode_change_pw3)
        self.num2_pushbutton_8.setObjectName(u"num2_pushbutton_8")
        self.num2_pushbutton_8.setGeometry(QRect(190, 230, 100, 100))
        self.num2_pushbutton_8.setFont(font4)
        self.num2_pushbutton_8.setStyleSheet(u"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.consoletext_14 = QLabel(self.securitycode_change_pw3)
        self.consoletext_14.setObjectName(u"consoletext_14")
        self.consoletext_14.setGeometry(QRect(0, 60, 480, 51))
        self.consoletext_14.setFont(font1)
        self.consoletext_14.setStyleSheet(u"\n"
"color:rgba(255,255,255,255);")
        self.consoletext_14.setTextFormat(Qt.AutoText)
        self.consoletext_14.setAlignment(Qt.AlignCenter)
        self.num1_pushbutton_8 = QPushButton(self.securitycode_change_pw3)
        self.num1_pushbutton_8.setObjectName(u"num1_pushbutton_8")
        self.num1_pushbutton_8.setGeometry(QRect(60, 230, 100, 100))
        self.num1_pushbutton_8.setFont(font4)
        self.num1_pushbutton_8.setStyleSheet(u"\n"
"QPushButton {\n"
"        color: white; \n"
"        border: 2px solid white; \n"
"        border-radius: 50px; \n"
"        background-color: rgba(96, 96, 96, 96);; \n"
"        padding: 5px; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(196, 196, 196, 196); \n"
"\n"
" }")
        self.num1_pushbutton_8.setIconSize(QSize(50, 50))
        self.num1_pushbutton_8.setAutoDefault(True)
        self.num1_pushbutton_8.setFlat(False)
        self.create_password_9 = QLineEdit(self.securitycode_change_pw3)
        self.create_password_9.setObjectName(u"create_password_9")
        self.create_password_9.setGeometry(QRect(100, 130, 280, 60))
        self.create_password_9.setFont(font2)
        self.create_password_9.setAutoFillBackground(False)
        self.create_password_9.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:3px solid rgba(237, 237, 237, 237);\n"
"color:rgba(237, 237, 237, 237);\n"
"padding-bottom:7px;\n"
"background-color: rgba(0, 0, 0, 0);")
        self.create_password_9.setFrame(True)
        self.create_password_9.setEchoMode(QLineEdit.Password)
        self.create_password_9.setAlignment(Qt.AlignCenter)
        self.create_password_9.setProperty("clearButtonEnabled", False)
        self.enigmatext_13 = QLabel(self.securitycode_change_pw3)
        self.enigmatext_13.setObjectName(u"enigmatext_13")
        self.enigmatext_13.setGeometry(QRect(0, 10, 480, 51))
        self.enigmatext_13.setFont(font)
        self.enigmatext_13.setStyleSheet(u"color:rgba(255,255,255,255);\n"
"")
        self.enigmatext_13.setTextFormat(Qt.PlainText)
        self.enigmatext_13.setAlignment(Qt.AlignCenter)
        self.background_13 = QLabel(self.securitycode_change_pw3)
        self.background_13.setObjectName(u"background_13")
        self.background_13.setGeometry(QRect(0, 0, 480, 800))
        self.background_13.setStyleSheet(u"background-image: url(bg-vertical.png);")
        self.stackedWidget.addWidget(self.securitycode_change_pw3)
        self.background_13.raise_()
        self.control1_pushbutton_13.raise_()
        self.control2_pushbutton_8.raise_()
        self.control1_pushbutton_14.raise_()
        self.num9_pushbutton_8.raise_()
        self.num8_pushbutton_8.raise_()
        self.num0_pushbutton_8.raise_()
        self.num4_pushbutton_8.raise_()
        self.num5_pushbutton_8.raise_()
        self.num3_pushbutton_8.raise_()
        self.ent_pushbutton_8.raise_()
        self.num7_pushbutton_8.raise_()
        self.num6_pushbutton_8.raise_()
        self.del_pushbutton_8.raise_()
        self.num2_pushbutton_8.raise_()
        self.consoletext_14.raise_()
        self.num1_pushbutton_8.raise_()
        self.create_password_9.raise_()
        self.enigmatext_13.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.background.setText("")
        self.enigmatext.setText(QCoreApplication.translate("MainWindow", u"ENIGMA", None))
        self.consoletext.setText(QCoreApplication.translate("MainWindow", u"CONSOLE", None))
        self.create_pass_label.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Create Password", None))
        self.ff_logo.setText("")
        self.without_pass_button.setText(QCoreApplication.translate("MainWindow", u"Continue without Password", None))
        self.background_2.setText("")
        self.enigmatext_2.setText(QCoreApplication.translate("MainWindow", u"ENIGMA", None))
        self.consoletext_2.setText(QCoreApplication.translate("MainWindow", u"CONSOLE", None))
        self.num4_pushbutton.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.num7_pushbutton.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.num5_pushbutton.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.num0_pushbutton.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.num6_pushbutton.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.ent_pushbutton.setText(QCoreApplication.translate("MainWindow", u"ENT", None))
        self.num1_pushbutton.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.num8_pushbutton.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.del_pushbutton.setText(QCoreApplication.translate("MainWindow", u"DEL", None))
        self.num3_pushbutton.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.num9_pushbutton.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.num2_pushbutton.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.create_password_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Create Password", None))
        self.control1_pushbutton.setText("")
        self.control2_pushbutton.setText("")
        self.background_3.setText("")
        self.confirm_password_button.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Confirm Password", None))
        self.num2_pushbutton_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.num1_pushbutton_2.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.num3_pushbutton_2.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.control1_pushbutton_2.setText("")
        self.ent_pushbutton_2.setText(QCoreApplication.translate("MainWindow", u"ENT", None))
        self.num8_pushbutton_2.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.enigmatext_3.setText(QCoreApplication.translate("MainWindow", u"ENIGMA", None))
        self.num6_pushbutton_2.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.control2_pushbutton_2.setText("")
        self.num7_pushbutton_2.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.del_pushbutton_2.setText(QCoreApplication.translate("MainWindow", u"DEL", None))
        self.num4_pushbutton_2.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.num5_pushbutton_2.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.num9_pushbutton_2.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.consoletext_3.setText(QCoreApplication.translate("MainWindow", u"CONSOLE", None))
        self.num0_pushbutton_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.background_4.setText("")
        self.enigmatext_4.setText(QCoreApplication.translate("MainWindow", u"ENIGMA", None))
        self.consoletext_4.setText(QCoreApplication.translate("MainWindow", u"CONSOLE", None))
        self.finish_text.setText(QCoreApplication.translate("MainWindow", u"WELL DONE!", None))
        self.security_text.setText(QCoreApplication.translate("MainWindow", u"Here is your security code:", None))
        self.securit_code_label.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Security Code Here", None))
        self.info_text.setText(QCoreApplication.translate("MainWindow", u"Don't forget to save and keep this code aside. When you forget your password, <strong>you can reset your password using this code.</strong>", None))
        self.continue_button.setText("")
        self.background_5.setText("")
        self.enigmatext_5.setText(QCoreApplication.translate("MainWindow", u"ENIGMA", None))
        self.consoletext_5.setText(QCoreApplication.translate("MainWindow", u"CONSOLE", None))
        self.open_button.setText(QCoreApplication.translate("MainWindow", u"OPEN CONSOLE", None))
        self.close_button.setText(QCoreApplication.translate("MainWindow", u"CLOSE CONSOLE", None))
        self.ff_logo_2.setText("")
        self.settings_pushbutton.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.num3_pushbutton_9.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.num7_pushbutton_9.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.open_password_button.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.ent_pushbutton_9.setText(QCoreApplication.translate("MainWindow", u"ENT", None))
        self.enigmatext_14.setText(QCoreApplication.translate("MainWindow", u"ENIGMA", None))
        self.del_pushbutton_9.setText(QCoreApplication.translate("MainWindow", u"DEL", None))
        self.num6_pushbutton_9.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.num0_pushbutton_9.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.background_14.setText("")
        self.num2_pushbutton_9.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.num9_pushbutton_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.num1_pushbutton_9.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.consoletext_15.setText(QCoreApplication.translate("MainWindow", u"CONSOLE", None))
        self.num8_pushbutton_9.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.num4_pushbutton_9.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.num5_pushbutton_9.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.background_6.setText("")
        self.consoletext_6.setText(QCoreApplication.translate("MainWindow", u"CONSOLE", None))
        self.enigmatext_6.setText(QCoreApplication.translate("MainWindow", u"ENIGMA", None))
        self.consoletext_7.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.change_password_label.setText(QCoreApplication.translate("MainWindow", u"Change Password", None))
        self.change_condition_lable.setText(QCoreApplication.translate("MainWindow", u"Password ON", None))
        self.forgot_security_code_label.setText(QCoreApplication.translate("MainWindow", u"Reset Password with Security Code", None))
        self.ff_logo_3.setText("")
        self.back_button.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.control2_pushbutton_3.setText("")
        self.consoletext_8.setText(QCoreApplication.translate("MainWindow", u"CONSOLE", None))
        self.num3_pushbutton_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.enigmatext_7.setText(QCoreApplication.translate("MainWindow", u"ENIGMA", None))
        self.num9_pushbutton_3.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.num0_pushbutton_3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.num1_pushbutton_3.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.create_password_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Current Password", None))
        self.num2_pushbutton_3.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.num6_pushbutton_3.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.num8_pushbutton_3.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.num7_pushbutton_3.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.background_7.setText("")
        self.ent_pushbutton_3.setText(QCoreApplication.translate("MainWindow", u"ENT", None))
        self.num4_pushbutton_3.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.num5_pushbutton_3.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.control1_pushbutton_3.setText("")
        self.del_pushbutton_3.setText(QCoreApplication.translate("MainWindow", u"DEL", None))
        self.control1_pushbutton_4.setText("")
        self.enigmatext_8.setText(QCoreApplication.translate("MainWindow", u"ENIGMA", None))
        self.create_password_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"New Password", None))
        self.num5_pushbutton_4.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.del_pushbutton_4.setText(QCoreApplication.translate("MainWindow", u"DEL", None))
        self.control2_pushbutton_4.setText("")
        self.control1_pushbutton_5.setText("")
        self.control1_pushbutton_6.setText("")
        self.consoletext_9.setText(QCoreApplication.translate("MainWindow", u"CONSOLE", None))
        self.num3_pushbutton_4.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.num7_pushbutton_4.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.num4_pushbutton_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.num9_pushbutton_4.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.ent_pushbutton_4.setText(QCoreApplication.translate("MainWindow", u"ENT", None))
        self.num2_pushbutton_4.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.num6_pushbutton_4.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.num8_pushbutton_4.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.num1_pushbutton_4.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.num0_pushbutton_4.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.background_8.setText("")
        self.num7_pushbutton_5.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.consoletext_10.setText(QCoreApplication.translate("MainWindow", u"CONSOLE", None))
        self.enigmatext_9.setText(QCoreApplication.translate("MainWindow", u"ENIGMA", None))
        self.num9_pushbutton_5.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.num2_pushbutton_5.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.control1_pushbutton_7.setText("")
        self.del_pushbutton_5.setText(QCoreApplication.translate("MainWindow", u"DEL", None))
        self.num4_pushbutton_5.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.num6_pushbutton_5.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.num1_pushbutton_5.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.num8_pushbutton_5.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.num0_pushbutton_5.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.num3_pushbutton_5.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.control1_pushbutton_8.setText("")
        self.num5_pushbutton_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.ent_pushbutton_5.setText(QCoreApplication.translate("MainWindow", u"ENT", None))
        self.background_9.setText("")
        self.create_password_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Confirm Password", None))
        self.control2_pushbutton_5.setText("")
        self.security_text_2.setText(QCoreApplication.translate("MainWindow", u"Here is your security code:", None))
        self.finish_text_2.setText(QCoreApplication.translate("MainWindow", u"WELL DONE!", None))
        self.continue_button_2.setText("")
        self.enigmatext_10.setText(QCoreApplication.translate("MainWindow", u"ENIGMA", None))
        self.background_10.setText("")
        self.info_text_2.setText(QCoreApplication.translate("MainWindow", u"Don't forget to save and keep this code aside. When you forget your password, <strong>you can reset your password using this code.</strong>", None))
        self.securit_code_label_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Security Code Here", None))
        self.consoletext_11.setText(QCoreApplication.translate("MainWindow", u"CONSOLE", None))
        self.security_text_3.setText(QCoreApplication.translate("MainWindow", u"The password successfully changed.", None))
        self.enigmatext_11.setText(QCoreApplication.translate("MainWindow", u"ENIGMA", None))
        self.create_password_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Security Code", None))
        self.num5_pushbutton_6.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.del_pushbutton_6.setText(QCoreApplication.translate("MainWindow", u"DEL", None))
        self.control2_pushbutton_6.setText("")
        self.control1_pushbutton_9.setText("")
        self.control1_pushbutton_10.setText("")
        self.consoletext_12.setText(QCoreApplication.translate("MainWindow", u"CONSOLE", None))
        self.num3_pushbutton_6.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.num7_pushbutton_6.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.num4_pushbutton_6.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.num9_pushbutton_6.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.ent_pushbutton_6.setText(QCoreApplication.translate("MainWindow", u"ENT", None))
        self.num2_pushbutton_6.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.num6_pushbutton_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.num1_pushbutton_6.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.num8_pushbutton_6.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.num0_pushbutton_6.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.background_11.setText("")
        self.num7_pushbutton_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.consoletext_13.setText(QCoreApplication.translate("MainWindow", u"CONSOLE", None))
        self.enigmatext_12.setText(QCoreApplication.translate("MainWindow", u"ENIGMA", None))
        self.num9_pushbutton_7.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.num2_pushbutton_7.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.control1_pushbutton_11.setText("")
        self.del_pushbutton_7.setText(QCoreApplication.translate("MainWindow", u"DEL", None))
        self.num4_pushbutton_7.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.num6_pushbutton_7.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.num1_pushbutton_7.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.num8_pushbutton_7.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.num0_pushbutton_7.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.num3_pushbutton_7.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.control1_pushbutton_12.setText("")
        self.num5_pushbutton_7.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.ent_pushbutton_7.setText(QCoreApplication.translate("MainWindow", u"ENT", None))
        self.background_12.setText("")
        self.create_password_8.setPlaceholderText(QCoreApplication.translate("MainWindow", u"New Password", None))
        self.control2_pushbutton_7.setText("")
        self.control1_pushbutton_13.setText("")
        self.control2_pushbutton_8.setText("")
        self.control1_pushbutton_14.setText("")
        self.num9_pushbutton_8.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.num8_pushbutton_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.num0_pushbutton_8.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.num4_pushbutton_8.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.num5_pushbutton_8.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.num3_pushbutton_8.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.ent_pushbutton_8.setText(QCoreApplication.translate("MainWindow", u"ENT", None))
        self.num7_pushbutton_8.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.num6_pushbutton_8.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.del_pushbutton_8.setText(QCoreApplication.translate("MainWindow", u"DEL", None))
        self.num2_pushbutton_8.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.consoletext_14.setText(QCoreApplication.translate("MainWindow", u"CONSOLE", None))
        self.num1_pushbutton_8.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.create_password_9.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Confirm Password", None))
        self.enigmatext_13.setText(QCoreApplication.translate("MainWindow", u"ENIGMA", None))
        self.background_13.setText("")
    # retranslateUi

