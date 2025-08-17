import sys, os, glob, json, random, bcrypt, platform, serial, cgitb
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import *
from uuid import  *
from subprocess import *
try:
    import RPi.GPIO as GPIO
except:
    pass
class Ui(QMainWindow):
    def __init__(self, parent=None):
        super(Ui, self).__init__(parent)
        self.system_type = platform.system()
        self.params()
        self.errorflag = False
        self.islogin = False
        self.control_count = 0
        self.control11=1
        if self.system_type=="Linux":
            font_path1 = "/home/ferhatberbercan/.fonts/static/Montserrat-Black.ttf"
            font_path2 = "/home/ferhatberbercan/.fonts/static/Montserrat-Medium.ttf"
            font_path3 = "/home/ferhatberbercan/.fonts/static/Montserrat-Light.ttf"
            font_path4 = "/home/ferhatberbercan/.fonts/static/Montserrat-SemiBold.ttf"
            font_path5 = "/home/ferhatberbercan/.fonts/static/Montserrat-ExtraBold.ttf"
            font = QtGui.QFont()
            QtGui.QFontDatabase.addApplicationFont(font_path1)
            QtGui.QFontDatabase.addApplicationFont(font_path2)
            QtGui.QFontDatabase.addApplicationFont(font_path3)
            QtGui.QFontDatabase.addApplicationFont(font_path4)
            QtGui.QFontDatabase.addApplicationFont(font_path5)
            font.setFamily("Montserrat-Black")
            font.setFamily("Montserrat-Medium")
            font.setFamily("Montserrat-Light")
            font.setFamily("Montserrat-SemiBold")
            font.setFamily("Montserrat-ExtraBold")
            self.shutdown_count = 0
            self.MAINS_INPUT = 25
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            GPIO.setup(self.MAINS_INPUT, GPIO.IN, GPIO.PUD_UP)
            self.uart = serial.Serial()
            self.uart.baudrate = 9600
            self.uart.timeout = 1
            self.uart.stopbit = 1
            self.uart.port = '/dev/ttyS0'
            self.uart.open()
            os.system("sudo wmctrl -c \"VNC Server\"")
        self.timer          = QTimer()
        self.timer          .setInterval(100)
        self.timer          .timeout.connect(self.control)
        self.timer          .start()
        loadUi(self.path+'enigma-gui.ui', self)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowTitle("Enigma GUI")
        self.setWindowIcon(QIcon(self.path+os.sep+"Transperent-Logo.ico"))
        if self.workingmode=="0" or self.workingmode=="":
            self.change_password_label.setText("Create Password")
            self.change_condition_lable.setText("Password OFF")
        else:
            self.change_password_label.setText("Change Password")
            self.change_condition_lable.setText("Password ON") 
        self.item_settings()
        self.label.setText(self.devicekey1)
        self.label_2.setText(self.devicekey2)
        self.show()
        self.setFixedSize(self.size())
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def modify_integer(self, input_integer):
        str_input = str(input_integer)
        modified_list = [str(int(char) + 9) for char in str_input]
        for i in range(len(modified_list)):
            if int(modified_list[i]) > 9:
                carry, remainder = divmod(int(modified_list[i]), 10)
                modified_list[i] = str(remainder)
                if i + 1 < len(modified_list):
                    modified_list[i + 1] = str(int(modified_list[i + 1]) + carry)
                else:
                    modified_list.append(str(carry))
        result_string = ''.join(modified_list)
        return result_string

    def params(self):
        self.devicekey1 = str(getnode()).zfill(16)
        try:
            self.devicekey2 = str(int(check_output(['cat', '/proc/cpuinfo']).decode().split('\n')[-3].split(" ")[-1],16)>>12).zfill(16)
#            print(self.devicekey2)
        except Exception as e:
            self.devicekey2 = "0000000000000000".zfill(16)
        self.devicekey = abs(int(self.devicekey1)-int(self.devicekey2))
        self.devicekey_str = self.modify_integer(self.devicekey)
        
        self.pat = __file__.split(os.sep)
        self.path = ""
        for i in range(len(self.pat)-1):
            self.path += self.pat[i]+os.sep
        try:
            parameters = glob.glob(self.path+"*.json")
            self.parameters = json.loads(
                open(parameters[0], encoding="utf-8").read())
        except:
            self.parameters={}
            self.parameters["workingmode"] = "0"
            self.parameters["devicekey"] = ""
            self.parameters["secretkey"] = ""
            self.parameters["password"] = ""
            self.parameters["lastposition"]=""
            self.workingmode = "0"
            with open(self.path+"parameters.json", "w") as json_file:
                json.dump(self.parameters, json_file, indent=4)
            parameters = glob.glob(self.path+"*.json")
            self.parameters = json.loads(
                open(parameters[0], encoding="utf-8").read())
        self.password_hash = self.parameters["password"]
        self.secretkey_hash = self.parameters["secretkey"]
        if self.parameters["devicekey"] == "":
            self.devicekey_hash=str(bcrypt.hashpw(self.devicekey_str.encode(), bcrypt.gensalt(10)).decode())
            self.parameters["devicekey"]=self.devicekey_hash
        else:
            self.devicekey_hash = self.parameters["devicekey"]
        self.workingmode = self.parameters["workingmode"] 
        self.lastposition = self.parameters["lastposition"]

    def opengate(self):
        self.lastposition = "1"
        self.parameters["lastposition"] = self.lastposition
        with open(self.path+"parameters.json", "w") as json_file:
                json.dump(self.parameters, json_file, indent=4)
        if self.system_type=="Linux" and self.control11:
            self.uart.write(b"0,50,2000\n") # Acilma parametreleri
            self.control11=0

    def closegate(self):
        self.lastposition = "0"
        self.parameters["lastposition"] = self.lastposition
        with open(self.path+"parameters.json", "w") as json_file:
                json.dump(self.parameters, json_file, indent=4)
        if self.system_type=="Linux" and self.control11:
            self.uart.write(b"1,50,2000\n") # Kapanma parametreleri
            self.control11=0

    def find_page_number(self, page_name):
        for page_number, name in self.page_list:
            if name == page_name:
                return page_number
        return None

    def buttons(self):
        sender_buton = self.sender()
        # print("buttons:", sender_buton.objectName())
        if sender_buton.objectName() == "forgot_security_code_label":
            self.oldpage=self.curpage
            self.curpage=self.find_page_number("securitycode_change_pw")
            self.main_stacked.setCurrentIndex(self.curpage)
        if sender_buton.objectName() == "change_condition_lable":
            if sender_buton.text() == "Password ON":
                self.parameters["workingmode"] = "0"
                self.parameters["devicekey"] = ""
                self.parameters["secretkey"] = ""
                self.parameters["password"] = ""
                self.parameters["lastposition"]=""
                self.workingmode = "0"
                with open(self.path+"parameters.json", "w") as json_file:
                    json.dump(self.parameters, json_file, indent=4)
                self.oldpage = self.main_stacked.currentIndex()
                self.curpage = self.find_page_number("main_page")
                self.main_stacked.setCurrentIndex(self.curpage)
                self.change_password_label.setText("Create Password")
                self.change_condition_lable.setText("Password OFF")
                return
        if sender_buton.objectName() == "change_password_label":
            if sender_buton.text() == "Create Password":
                self.oldpage=self.curpage
                self.curpage=self.find_page_number("first_page")
                self.main_stacked.setCurrentIndex(self.curpage)
                return
            self.oldpage=self.curpage
            self.curpage=self.find_page_number("change_password_page")
            self.create_password_4.setText("")
            self.control1_pushbutton_4.setStyleSheet("QPushButton{\ncolor: white; border: 2px solid white;border-radius: 15px;background-color: transparent;padding: 5px;}")
            self.control1_pushbutton_3.setStyleSheet("QPushButton{\ncolor: white; border: 2px solid white;border-radius: 15px;background-color: transparent;padding: 5px;}")
            self.control2_pushbutton_3.setStyleSheet("QPushButton{\ncolor: white; border: 2px solid white;border-radius: 15px;background-color: transparent;padding: 5px;}")
            self.main_stacked.setCurrentIndex(self.curpage)
            return
        if sender_buton.objectName() == "back_button":
            self.oldpage = self.main_stacked.currentIndex()
            self.curpage = self.find_page_number("main_page")
            self.main_stacked.setCurrentIndex(self.curpage)
            return
        if sender_buton.objectName() == "settings_pushbutton":
            self.oldpage=self.curpage
            self.curpage=self.find_page_number("settings_page")
            self.main_stacked.setCurrentIndex(self.curpage)
            return
        if sender_buton.objectName() == "close_button" or sender_buton.objectName() == "open_button" :
            if self.workingmode=="0":
                if sender_buton.objectName() == "close_button":
                    if self.lastposition == "1":
                        self.closegate()
                        return
                else:
                    if self.lastposition == "" or self.lastposition == "0":
                        self.opengate()
                        return
                return
            elif self.workingmode=="1":
                if self.lastposition == "" or self.lastposition == "0":
                    if sender_buton.objectName() == "open_button":
                        self.oldpage = self.main_stacked.currentIndex()
                        self.curpage = self.find_page_number("password_open")
                        self.main_stacked.setCurrentIndex(self.curpage)
                        return
                else:
                    if sender_buton.objectName() == "close_button":
                        self.closegate()
                        return
            return
        if sender_buton.objectName() == "continue_button" or sender_buton.objectName() == "continue_button_2":
            self.parameters["secretkey"]=self.secretkey_hash
            self.parameters["password"]=self.password_hash
            self.parameters["workingmode"]="1"
            self.parameters["devicekey"]=self.devicekey_hash
            self.parameters["lastposition"]=""
            with open(self.path+"parameters.json", "w") as json_file:
                json.dump(self.parameters, json_file, indent=4)
            self.curpage = self.find_page_number("main_page")
            self.main_stacked.setCurrentIndex(self.curpage)
            self.oldpage=self.curpage
            self.change_password_label.setText("Change Password")
            self.change_condition_lable.setText("Password ON")
            return
        if sender_buton.objectName() == "without_pass_button":
            self.parameters["workingmode"] = "0"
            self.parameters["devicekey"] = ""
            self.parameters["secretkey"] = ""
            self.parameters["password"] = ""
            self.parameters["lastposition"]=""
            self.workingmode = "0"
            with open(self.path+"parameters.json", "w") as json_file:
                json.dump(self.parameters, json_file, indent=4)
            self.oldpage = self.main_stacked.currentIndex()
            self.curpage = self.find_page_number("main_page")
            self.main_stacked.setCurrentIndex(self.curpage)
            self.change_password_label.setText("Create Password")
            self.change_condition_lable.setText("Password OFF")
            return
        if "del" in sender_buton.objectName() or "ent" in sender_buton.objectName():
            butname = sender_buton.objectName()
            self.del_ent_but_control(butname)
            return 

    def del_ent_but_control(self,butname):
        if self.curpage == self.find_page_number("create_password_page1"):
            text = self.create_password_2.text()
            but = butname.split("_")
            if but[0] == "del" or but[0] == "ent":
                if but[0] == "del":
                    self.create_password_2.setText(text[:-1])
                    textc = self.create_password_2.text()
                    if len(textc) == 0:
                        self.main_stacked.setCurrentIndex(self.find_page_number("first_page"))
                        self.curpage = self.find_page_number("first_page")
                    elif len(textc)<6:
                        self.control1_pushbutton.setStyleSheet(
                            "QPushButton {\n color: white; \n border: 2px solid white;\n border-radius: 15px; \n background-color: #FF0000; \n padding: 5px; \n}")
                    else:
                        self.control1_pushbutton.setStyleSheet(
                            "QPushButton {\n color: white; \n border: 2px solid white;\n border-radius: 15px; \n background-color: #FFFF00; \n padding: 5px; \n}")
                    return
                else:
                    if len(text) > 5:
                        self.password1 = text
                        self.oldpage = self.main_stacked.currentIndex()
                        self.curpage = self.find_page_number(
                            "again_password_page")
                        self.main_stacked.setCurrentIndex(self.curpage)
                        self.control1_pushbutton.setStyleSheet(
                            "QPushButton {\n color: white; \n border: 2px solid white;\n border-radius: 15px; \n background-color: #FFFF00; \n padding: 5px; \n}")
                    else:
                        self.control1_pushbutton.setStyleSheet(
                            "QPushButton {\n color: white; \n border: 2px solid white;\n border-radius: 15px; \n background-color: #FF0000; \n padding: 5px; \n}")
            return
        if self.curpage == self.find_page_number("again_password_page"):
            text = self.confirm_password_button.text()
            but = butname.split("_")
            if but[0] == "del" or but[0] == "ent":
                if but[0] == "del":
                    self.confirm_password_button.setText(text[:-1])
                    textc = self.confirm_password_button.text()
                    if len(text) == 0:
                        self.main_stacked.setCurrentIndex(self.find_page_number("create_password_page1"))
                        self.curpage = self.find_page_number("create_password_page1")
                    elif textc != self.password1:
                        self.control2_pushbutton_2.setStyleSheet(
                            "QPushButton {\n color: white; \n border: 2px solid white;\n border-radius: 15px; \n background-color: #FF0000; \n padding: 5px; \n}")
                    else:
                        self.control2_pushbutton_2.setStyleSheet(
                            "QPushButton {\n color: white; \n border: 2px solid white;\n border-radius: 15px; \n background-color: #00FF00; \n padding: 5px; \n}")
                    return
                else:
                    if text != self.password1:
                        
                        self.control2_pushbutton_2.setStyleSheet(
                            "QPushButton {\n color: white; \n border: 2px solid white;\n border-radius: 15px; \n background-color: #FF0000; \n padding: 5px; \n}")
                    else:
                        self.control2_pushbutton_2.setStyleSheet(
                            "QPushButton {\n color: white; \n border: 2px solid white;\n border-radius: 15px; \n background-color: #00FF00; \n padding: 5px; \n}")
                        self.password2 = text
                        self.oldpage = self.main_stacked.currentIndex()
                        self.curpage = self.find_page_number(
                            "password_done_page")
                        self.main_stacked.setCurrentIndex(self.curpage)
                        self.secretkey = "".join([str(random.randint(0,9)) for _ in range(16)])
                        self.securit_code_label.setText(self.secretkey)
                        self.secretkey_hash  = str(bcrypt.hashpw(self.secretkey.encode(), bcrypt.gensalt(10)).decode())
                        self.password_hash   = str(bcrypt.hashpw(str(self.password1).encode(), bcrypt.gensalt(10)).decode())
            return
        if self.curpage == self.find_page_number("password_open"):
            text = self.open_password_button.text()
            but = butname.split("_")
            if but[0] == "del" or but[0] == "ent":
                if but[0] == "del":
                    self.open_password_button.setText(text[:-1])
                    if len(text) == 0:
                        self.main_stacked.setCurrentIndex(self.find_page_number("main_page"))
                        self.curpage = self.find_page_number("main_page")
                    elif text == "Wrong Password":
                        self.open_password_button.setEchoMode(QLineEdit.Password)
                        self.open_password_button.setStyleSheet("background-color:rgba(0, 0, 0, 0); border:none; border-bottom:3px solid rgba(237, 237, 237, 237); color:rgba(237, 237, 237, 237); padding-bottom:7px; background-color: rgba(0, 0, 0, 0);")
                        self.open_password_button.setText("")
                    return
                else:
                    control=self.password_check(text)
                    if control:
                        self.opengate()
                        self.open_password_button.setEchoMode(QLineEdit.Normal)
                        self.open_password_button.setStyleSheet("background-color:rgba(0, 0, 0, 0); border:none; border-bottom:3px solid rgba(237, 237, 237, 237); color:rgba(0, 255, 0, 255); padding-bottom:7px; background-color: rgba(0, 0, 0, 0);")
                        self.open_password_button.setText("Password Corrent")
                        QTimer.singleShot(500,self.mainpage_event)
                    else:
                        self.open_password_button.setEchoMode(QLineEdit.Normal)
                        self.open_password_button.setStyleSheet("background-color:rgba(0, 0, 0, 0); border:none; border-bottom:3px solid rgba(237, 237, 237, 237); color:rgba(255, 0, 0, 255); padding-bottom:7px; background-color: rgba(0, 0, 0, 0);")
                        self.open_password_button.setText("Wrong Password")
            return
        if self.curpage==self.find_page_number("change_password_page"):
            text = self.create_password_4.text()
            but = butname.split("_")
            if but[0] == "del" or but[0] == "ent":
                if but[0] == "del":
                    self.create_password_4.setText(text[:-1])
                    textc = self.create_password_4.text()
                    if len(textc) == 0:
                        self.main_stacked.setCurrentIndex(self.find_page_number("settings_page"))
                        self.curpage = self.find_page_number("settings_page")
                    elif text == "Wrong Password":
                        self.create_password_4.setEchoMode(QLineEdit.Password)
                        self.create_password_4.setStyleSheet("background-color:rgba(0, 0, 0, 0); border:none; border-bottom:3px solid rgba(237, 237, 237, 237); color:rgba(237, 237, 237, 237); padding-bottom:7px; background-color: rgba(0, 0, 0, 0);")
                        self.create_password_4.setText("")
                        return
                    elif len(textc)<6:
                        self.control1_pushbutton_4.setStyleSheet(
                            "QPushButton {\n color: white; \n border: 2px solid white;\n border-radius: 15px; \n background-color: #FF0000; \n padding: 5px; \n}")
                    else:
                        self.control1_pushbutton_4.setStyleSheet(
                            "QPushButton {\n color: white; \n border: 2px solid white;\n border-radius: 15px; \n background-color: #FFFF00; \n padding: 5px; \n}")
                    return
                else:
                    if len(text) > 5:
                        control = self.password_check(text)
                        if control:
                            self.control1_pushbutton_5.setStyleSheet("QPushButton{\ncolor: white; border: 2px solid white;border-radius: 15px;background-color: #00FF00;padding: 5px;}")
                            self.control1_pushbutton_6.setStyleSheet("QPushButton{\ncolor: white; border: 2px solid white;border-radius: 15px;background-color: transparent;padding: 5px;}")
                            self.control2_pushbutton_4.setStyleSheet("QPushButton{\ncolor: white; border: 2px solid white;border-radius: 15px;background-color: transparent;padding: 5px;}")
                            self.oldpage=self.curpage
                            self.curpage=self.find_page_number("change_pw_new_pw")
                            self.main_stacked.setCurrentIndex(self.curpage)
                        else:
                            self.create_password_4.setEchoMode(QLineEdit.Normal)
                            self.create_password_4.setStyleSheet("background-color:rgba(0, 0, 0, 0); border:none; border-bottom:3px solid rgba(237, 237, 237, 237); color:rgba(255, 0, 0, 255); padding-bottom:7px; background-color: rgba(0, 0, 0, 0);")
                            self.create_password_4.setText("Wrong Password")
                            self.control1_pushbutton_4.setStyleSheet("QPushButton{\ncolor: white; border: 2px solid white;border-radius: 15px;background-color: #FF0000;padding: 5px;}")
                            self.control1_pushbutton_3.setStyleSheet("QPushButton{\ncolor: white; border: 2px solid white;border-radius: 15px;background-color: transparent;padding: 5px;}")
                            self.control2_pushbutton_3.setStyleSheet("QPushButton{\ncolor: white; border: 2px solid white;border-radius: 15px;background-color: transparent;padding: 5px;}")
                    else:
                        self.control1_pushbutton_4.setStyleSheet("QPushButton{\ncolor: white; border: 2px solid white;border-radius: 15px;background-color: #FF0000;padding: 5px;}")         
            return
        if self.curpage == self.find_page_number("change_pw_new_pw"):
            text = self.create_password_5.text()
            but = butname.split("_")
            if but[0] == "del" or but[0] == "ent":
                if but[0] == "del":
                    self.create_password_5.setText(text[:-1])
                    textc = self.create_password_5.text()
                    if len(textc) == 0:
                        self.main_stacked.setCurrentIndex(self.find_page_number("change_password_page"))
                        self.curpage = self.find_page_number("change_password_page")
                    elif len(textc)<6:
                        self.control1_pushbutton_6.setStyleSheet(
                            "QPushButton {\n color: white; \n border: 2px solid white;\n border-radius: 15px; \n background-color: #FF0000; \n padding: 5px; \n}")
                    else:
                        self.control1_pushbutton_6.setStyleSheet(
                            "QPushButton {\n color: white; \n border: 2px solid white;\n border-radius: 15px; \n background-color: #FFFF00; \n padding: 5px; \n}")
                    return
                else:
                    if len(text) > 5:
                        self.password1 = text
                        self.oldpage = self.main_stacked.currentIndex()
                        self.curpage = self.find_page_number(
                            "new_pw_confirm_pw")
                        self.main_stacked.setCurrentIndex(self.curpage)
                        self.control1_pushbutton_6.setStyleSheet(
                            "QPushButton {\n color: white; \n border: 2px solid white;\n border-radius: 15px; \n background-color: #FFFF00; \n padding: 5px; \n}")
                    else:
                        self.control1_pushbutton_6.setStyleSheet(
                            "QPushButton {\n color: white; \n border: 2px solid white;\n border-radius: 15px; \n background-color: #FF0000; \n padding: 5px; \n}")
            return
        if self.curpage == self.find_page_number("new_pw_confirm_pw"):
            text = self.create_password_6.text()
            but = butname.split("_")
            if but[0] == "del" or but[0] == "ent":
                if but[0] == "del":
                    self.create_password_6.setText(text[:-1])
                    textc = self.create_password_6.text()
                    if len(text) == 0:
                        self.main_stacked.setCurrentIndex(self.find_page_number("change_pw_new_pw"))
                        self.curpage = self.find_page_number("change_pw_new_pw")
                    elif textc != self.password1:
                        self.control2_pushbutton_5.setStyleSheet(
                            "QPushButton {\n color: white; \n border: 2px solid white;\n border-radius: 15px; \n background-color: #FF0000; \n padding: 5px; \n}")
                    else:
                        self.control2_pushbutton_5.setStyleSheet(
                            "QPushButton {\n color: white; \n border: 2px solid white;\n border-radius: 15px; \n background-color: #00FF00; \n padding: 5px; \n}")
                    return
                else:
                    if text != self.password1:
                        
                        self.control2_pushbutton_5.setStyleSheet(
                            "QPushButton {\n color: white; \n border: 2px solid white;\n border-radius: 15px; \n background-color: #FF0000; \n padding: 5px; \n}")
                    else:
                        self.control2_pushbutton_5.setStyleSheet(
                            "QPushButton {\n color: white; \n border: 2px solid white;\n border-radius: 15px; \n background-color: #00FF00; \n padding: 5px; \n}")
                        self.password2 = text
                        self.oldpage = self.main_stacked.currentIndex()
                        self.curpage = self.find_page_number(
                            "new_pw_done_page")
                        self.main_stacked.setCurrentIndex(self.curpage)
                        self.secretkey = "".join([str(random.randint(0,9)) for _ in range(16)])
                        self.securit_code_label_2.setText(self.secretkey)
                        self.secretkey_hash  = str(bcrypt.hashpw(self.secretkey.encode(), bcrypt.gensalt(10)).decode())
                        self.password_hash   = str(bcrypt.hashpw(str(self.password1).encode(), bcrypt.gensalt(10)).decode())
            return
        if self.curpage == self.find_page_number("securitycode_change_pw"):
            text = self.create_password_7.text()
            but = butname.split("_")
            if but[0] == "del" or but[0] == "ent":
                if but[0] == "del":
                    self.create_password_7.setText(text[:-1])
                    if len(text) == 0:
                        self.main_stacked.setCurrentIndex(self.find_page_number("settings_page"))
                        self.curpage = self.find_page_number("settings_page")
                    elif text == "Wrong CODE":
                        self.create_password_7.setEchoMode(QLineEdit.Normal)
                        self.create_password_7.setStyleSheet("background-color:rgba(0, 0, 0, 0); border:none; border-bottom:3px solid rgba(237, 237, 237, 237); color:rgba(237, 237, 237, 237); padding-bottom:7px; background-color: rgba(0, 0, 0, 0);")
                        self.control1_pushbutton_10.setStyleSheet(
                    "QPushButton {\n color: white; \n border: 2px solid white;\n border-radius: 15px; \n background-color: #FF0000; \n padding: 5px; \n}")
                        self.create_password_7.setText("")
                    return
                else:
                    control=self.security_check(text)
                    if control:
                        self.create_password_7.setEchoMode(QLineEdit.Normal)
                        self.create_password_7.setStyleSheet("background-color:rgba(0, 0, 0, 0); border:none; border-bottom:3px solid rgba(237, 237, 237, 237); color:rgba(0, 255, 0, 255); padding-bottom:7px; background-color: rgba(0, 0, 0, 0);")
                        self.create_password_7.setText("CODE Corrent")
                        self.control1_pushbutton_10.setStyleSheet(
                    "QPushButton {\n color: white; \n border: 2px solid white;\n border-radius: 15px; \n background-color: #00FF00; \n padding: 5px; \n}")
                        QTimer.singleShot(2000,self.reset_)
                    else:
                        self.create_password_7.setEchoMode(QLineEdit.Normal)
                        self.create_password_7.setStyleSheet("background-color:rgba(0, 0, 0, 0); border:none; border-bottom:3px solid rgba(237, 237, 237, 237); color:rgba(255, 0, 0, 255); padding-bottom:7px; background-color: rgba(0, 0, 0, 0);")
                        self.create_password_7.setText("Wrong CODE")
                        self.control1_pushbutton_10.setStyleSheet(
                    "QPushButton {\n color: white; \n border: 2px solid white;\n border-radius: 15px; \n background-color: #FF0000; \n padding: 5px; \n}")
            return

    def reset_(self):
        self.parameters["workingmode"] = "0"
        self.parameters["devicekey"] = ""
        self.parameters["secretkey"] = ""
        self.parameters["password"] = ""
        self.parameters["lastposition"]=""
        self.workingmode = "0"
        with open(self.path+"parameters.json", "w") as json_file:
            json.dump(self.parameters, json_file, indent=4)
        self.oldpage = self.main_stacked.currentIndex()
        self.curpage = self.find_page_number("first_page")
        self.main_stacked.setCurrentIndex(self.curpage)
        self.change_password_label.setText("Create Password")
        self.change_condition_lable.setText("Password OFF")
        self.open_password_button.setEchoMode(QLineEdit.Password)
        self.open_password_button.setStyleSheet("background-color:rgba(0, 0, 0, 0); border:none; border-bottom:3px solid rgba(237, 237, 237, 237); color:rgba(237, 237, 237, 237); padding-bottom:7px; background-color: rgba(0, 0, 0, 0);")
        self.open_password_button.setText("")
        self.create_password_7.setText("")
        self.control1_pushbutton_10.setStyleSheet(
                    "QPushButton {\n color: white; \n border: 2px solid white;\n border-radius: 15px; \n background-color: transparent; \n padding: 5px; \n}")
        self.securit_code_label_2.setText("")
        self.securit_code_label.setText("")
        self.create_password_7.setStyleSheet("background-color:rgba(0, 0, 0, 0); border:none; border-bottom:3px solid rgba(237, 237, 237, 237); color:rgba(237, 237, 237, 237); padding-bottom:7px; background-color: rgba(0, 0, 0, 0);")

    def mainpage_event(self):
        self.lastposition = "1"
        self.parameters["lastposition"]=self.lastposition
        with open(self.path+"parameters.json", "w") as json_file:
                json.dump(self.parameters, json_file, indent=4)
        self.curpage = self.find_page_number("main_page")
        self.oldpage = self.curpage
        self.main_stacked.setCurrentIndex(self.curpage)
        self.open_password_button.setEchoMode(QLineEdit.Password)
        self.open_password_button.setStyleSheet("background-color:rgba(0, 0, 0, 0); border:none; border-bottom:3px solid rgba(237, 237, 237, 237); color:rgba(237, 237, 237, 237); padding-bottom:7px; background-color: rgba(0, 0, 0, 0);")
        self.open_password_button.setText("")

    def security_check(self,passwordc):
        return (bcrypt.checkpw(str(passwordc).encode(),self.secretkey_hash.encode()) or bcrypt.checkpw(str(passwordc).encode(),self.devicekey_hash.encode()))

    def password_check(self,passwordc):
        return bcrypt.checkpw(str(passwordc).encode(),self.password_hash.encode())

    def numbers(self):
        sender_buton = self.sender()
        # print("numbers:", sender_buton.objectName())
        butname = sender_buton.objectName()
        if self.curpage == self.find_page_number("securitycode_change_pw"):
            if self.create_password_7.text() == "Wrong CODE":
                self.create_password_7.setEchoMode(QLineEdit.Normal)
                self.create_password_7.setStyleSheet("background-color:rgba(0, 0, 0, 0); border:none; border-bottom:3px solid rgba(237, 237, 237, 237); color:rgba(237, 237, 237, 237); padding-bottom:7px; background-color: rgba(0, 0, 0, 0);")
                self.create_password_7.setText("")
            text = self.create_password_7.text()
            but = butname.split("_")
            num = but[0][-1]
            self.create_password_7.setText(text+num)
            if  len(text)<10:
                self.control1_pushbutton_10.setStyleSheet(
                    "QPushButton {\n color: white; \n border: 2px solid white;\n border-radius: 15px; \n background-color: #FF0000; \n padding: 5px; \n}")
            else:
                self.control1_pushbutton_10.setStyleSheet(
                    "QPushButton {\n color: white; \n border: 2px solid white;\n border-radius: 15px; \n background-color: #FFFF00; \n padding: 5px; \n}")
            return
        if self.curpage == self.find_page_number("new_pw_confirm_pw"):
            if self.create_password_6.text() == "Wrong Password":
                self.create_password_6.setEchoMode(QLineEdit.Password)
                self.create_password_6.setStyleSheet("background-color:rgba(0, 0, 0, 0); border:none; border-bottom:3px solid rgba(237, 237, 237, 237); color:rgba(237, 237, 237, 237); padding-bottom:7px; background-color: rgba(0, 0, 0, 0);")
                self.create_password_6.setText("")
            text = self.create_password_6.text()
            but = butname.split("_")
            num = but[0][-1]
            self.create_password_6.setText(text+num)
            if  len(text)<5:
                self.control2_pushbutton_5.setStyleSheet(
                    "QPushButton {\n color: white; \n border: 2px solid white;\n border-radius: 15px; \n background-color: #FF0000; \n padding: 5px; \n}")
            else:
                self.control2_pushbutton_5.setStyleSheet(
                    "QPushButton {\n color: white; \n border: 2px solid white;\n border-radius: 15px; \n background-color: #FFFF00; \n padding: 5px; \n}")
            return
        if self.curpage == self.find_page_number("change_pw_new_pw"):
            text = self.create_password_5.text()
            but = butname.split("_")
            num = but[0][-1]
            self.create_password_5.setText(text+num)
            if  len(text)<5:
                self.control1_pushbutton_6.setStyleSheet(
                    "QPushButton {\n color: white; \n border: 2px solid white;\n border-radius: 15px; \n background-color: #FF0000; \n padding: 5px; \n}")
            else:
                self.control1_pushbutton_6.setStyleSheet(
                    "QPushButton {\n color: white; \n border: 2px solid white;\n border-radius: 15px; \n background-color: #FFFF00; \n padding: 5px; \n}")
            return
        if self.curpage == self.find_page_number("change_password_page"):
            if self.create_password_4.text() == "Wrong Password":
                self.create_password_4.setEchoMode(QLineEdit.Password)
                self.create_password_4.setStyleSheet("background-color:rgba(0, 0, 0, 0); border:none; border-bottom:3px solid rgba(237, 237, 237, 237); color:rgba(237, 237, 237, 237); padding-bottom:7px; background-color: rgba(0, 0, 0, 0);")
                self.create_password_4.setText("")
            text = self.create_password_4.text()
            but = butname.split("_")
            num = but[0][-1]
            self.create_password_4.setText(text+num)
            if  len(text)<5:
                self.control1_pushbutton_4.setStyleSheet(
                    "QPushButton {\n color: white; \n border: 2px solid white;\n border-radius: 15px; \n background-color: #FF0000; \n padding: 5px; \n}")
            else:
                self.control1_pushbutton_4.setStyleSheet(
                    "QPushButton {\n color: white; \n border: 2px solid white;\n border-radius: 15px; \n background-color: #FFFF00; \n padding: 5px; \n}")
            return
        if self.curpage == self.find_page_number("create_password_page1"):
            text = self.create_password_2.text()
            but = butname.split("_")
            num = but[0][-1]
            self.create_password_2.setText(text+num)
            if  len(text)<5:
                self.control1_pushbutton.setStyleSheet(
                    "QPushButton {\n color: white; \n border: 2px solid white;\n border-radius: 15px; \n background-color: #FF0000; \n padding: 5px; \n}")
            else:
                self.control1_pushbutton.setStyleSheet(
                    "QPushButton {\n color: white; \n border: 2px solid white;\n border-radius: 15px; \n background-color: #FFFF00; \n padding: 5px; \n}")
            return
        if self.curpage == self.find_page_number("again_password_page"):
            if self.confirm_password_button.text() == "Wrong Password":
                self.confirm_password_button.setEchoMode(QLineEdit.Password)
                self.confirm_password_button.setStyleSheet("background-color:rgba(0, 0, 0, 0); border:none; border-bottom:3px solid rgba(237, 237, 237, 237); color:rgba(237, 237, 237, 237); padding-bottom:7px; background-color: rgba(0, 0, 0, 0);")
                self.confirm_password_button.setText("")
            text = self.confirm_password_button.text()
            but = butname.split("_")
            num = but[0][-1]
            self.confirm_password_button.setText(text+num)
            textc = self.confirm_password_button.text()
            if  textc == self.password1:
                self.control2_pushbutton_2.setStyleSheet(
                    "QPushButton {\n color: white; \n border: 2px solid white;\n border-radius: 15px; \n background-color: #FFFF00; \n padding: 5px; \n}")
            else:
                self.control2_pushbutton_2.setStyleSheet(
                    "QPushButton {\n color: white; \n border: 2px solid white;\n border-radius: 15px; \n background-color: #FF0000; \n padding: 5px; \n}")
            return
        if self.curpage == self.find_page_number("password_open"):
            if self.open_password_button.text() == "Wrong Password":
                self.open_password_button.setEchoMode(QLineEdit.Password)
                self.open_password_button.setStyleSheet("background-color:rgba(0, 0, 0, 0); border:none; border-bottom:3px solid rgba(237, 237, 237, 237); color:rgba(237, 237, 237, 237); padding-bottom:7px; background-color: rgba(0, 0, 0, 0);")
                self.open_password_button.setText("")
            text = self.open_password_button.text()
            but = butname.split("_")
            num = but[0][-1]
            self.open_password_button.setText(text+num)
            textc = self.open_password_button.text()
            return

    def lines(self, item, item_type):
        # print("lines:", item.objectName())
        if item.objectName() == "create_pass_label":
            self.oldpage = self.main_stacked.currentIndex()
            self.curpage = self.find_page_number("create_password_page1")
            self.main_stacked.setCurrentIndex(self.curpage)

    def item_settings(self):
        self.main_stacked = self.centralwidget.findChildren(
            QtWidgets.QStackedWidget)
        self.main_stacked = self.main_stacked[0]
        self.page_list = []
        for indis in range(self.main_stacked.count()):
            PageName = self.main_stacked.widget(indis).objectName()
            self.page_list.append([indis, PageName])
        if self.workingmode == "" or self.workingmode == "0":
            self.curpage = self.find_page_number("first_page")
            self.oldpage = self.curpage
            self.main_stacked.setCurrentIndex(self.curpage)
        else:
            if self.password_hash != "":
                self.curpage = self.find_page_number("main_page")
                self.oldpage = self.curpage
                self.main_stacked.setCurrentIndex(self.curpage)
            else:
                self.curpage = self.find_page_number("first_page")
                self.oldpage = self.curpage
                self.main_stacked.setCurrentIndex(self.curpage)
        self.all_labels = self.centralwidget.findChildren(QtWidgets.QLabel)
        self.all_pushbuttons = self.centralwidget.findChildren(
            QtWidgets.QPushButton)
        for ite in self.all_pushbuttons:
            if "num" not in ite.objectName():
                ite.clicked.connect(self.buttons)
            else:
                ite.clicked.connect(self.numbers)

        self.all_lineedits = self.centralwidget.findChildren(
            QtWidgets.QLineEdit)
        for ite in self.all_lineedits:
            ite.installEventFilter(self)

    def control(self):
        if self.system_type=="Linux":
            self.shutdown_control()
            if self.uart.in_waiting >= 1:
                re_mes = self.serial_receive()
                if re_mes == "close":
                    self.lastposition="0"
                elif re_mes == "open":
                    self.lastposition="1"
                else:
                    print(re_mes)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.MouseButtonPress:
            self.lines(obj, type(obj).__name__)
        return super().eventFilter(obj, event)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Quit', 'Are you sure you want to quit?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def shutdown_control(self):
        shutdown_time = 75 # 0.1s x 75 = 7.5s
        if GPIO.input(self.MAINS_INPUT) == 0: # gercek kaynak baglandiginda import RPi.GPIO as GPIO
            self.shutdown_count += 1
            if self.shutdown_count == shutdown_time:
                os.system("sudo shutdown now")
        else:
            self.shutdown_count = 0
        
    def serial_receive(self):
        try:
            serial_line = self.uart.readline().decode('latin-1')
            self.control11=1
        except serial.SerialException:
          pass  
        return serial_line

def main():
    # cgitb.enable(format='text')
    app = QApplication(sys.argv)
    window = Ui()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
