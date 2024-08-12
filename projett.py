# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!

from inscrip import Ui_inscrip
from PyQt5.QtWidgets import QApplication, QMainWindow
from programeue import Ui_progr
from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1202, 800)
        MainWindow.setStyleSheet("#MainWindow {\n"
"   background-image: url(Sans titre.png);\n"
"   background-repeat:no-repeat;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(860, 140, 160, 160))
        self.widget.setStyleSheet("background-image: url(pro.png);")
        self.widget.setObjectName("widget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(830, 390, 231, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(830, 450, 231, 31))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 190, 601, 50))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(22)
        font.setStrikeOut(False)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(130, 240, 541, 50))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(22)
        font.setStrikeOut(False)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(260, 290, 281, 50))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(22)
        font.setStrikeOut(False)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(900, 510, 101, 31))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background: #9972e3;\n"
"    background-color:#9972e3;\n"
"    font: 25 11pt \"URW Bookman\";\n"
"    border: 2px solid #9972e3; \n"
"    border-radius: 10px; \n"
"    font-size:20px;\n"
"    color: #ffffff;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"     border: 2px solid #e375a7; \n"
"     background: #e375a7;\n"
"      background-color:#e375a7;\n"
"      color: #ffffff;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.login)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1050, 658, 89, 25))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    background: #ffffff;\n"
"    background-color:#ffffff;\n"
"    font:  11pt \"Ubuntu\";\n"
"    border: 0px solid #ffffff; \n"
"    border-radius: 10px; \n"
"    font-size:14px;\n"
"    color: #4a5ffa;\n"
"\n"
"}\n"
"")
        self.pushButton_2.setAutoRepeatInterval(99)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.inscr)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(900, 660, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(910, 330, 67, 17))
        font = QtGui.QFont()
        font.setFamily("Abyssinica SIL")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(780, 340, 118, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(990, 340, 118, 3))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.lineEdit.setText(_translate("MainWindow", "Email"))
        self.lineEdit_2.setText(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "Login"))
        self.pushButton_2.setText(_translate("MainWindow", "Sign up"))
        self.label.setText(_translate("MainWindow", "Don\'t have in account?"))
        self.label_2.setText(_translate("MainWindow", "Sign in"))
        self.label_3.setText(_translate("MainWindow", "Optimisation de l\'investissement Dans le Projet  "))
        self.label_4.setText(_translate("MainWindow", "d\'installation d\'une centrale photovoltaïque "))
        self.label_5.setText(_translate("MainWindow", "dans l\'aeroport d\'Alger"))

    def login(self):
        Db=pd.read_csv("login.csv")
        mail=self.lineEdit.text()
        pas=self.lineEdit_2.text()
        for j in Db["Email"]:
            if j==mail :
                for h in Db["Passw"]:
                    if h==pas:
                        self.pro()

                    else:
                        print("hhh")
                        self.inscr()
    def inscr(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_inscrip()
        self.ui.setupUi(self.window)
        self.window.show()



    def pro(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_progr()
        self.ui.setupUi(self.window)
        self.window.show()







if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
