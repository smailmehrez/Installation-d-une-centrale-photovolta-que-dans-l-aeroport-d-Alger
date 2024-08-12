# -*- coding: utf-8 -*-
import csv
import os

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtWidgets import QApplication, QMainWindow
from dialog2 import Ui_dialoginscr
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import warnings

class Ui_inscrip(object):
    def setupUi(self, inscrip):
        inscrip.setObjectName("inscrip")
        inscrip.resize(1202, 800)
        inscrip.setStyleSheet("#inscrip {\n"
"   background-image: url(Sans titre.png);\n"
"   background-repeat:no-repeat;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(inscrip)
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
        self.pushButton.clicked.connect(self.insc)


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
        inscrip.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(inscrip)
        self.statusbar.setObjectName("statusbar")
        inscrip.setStatusBar(self.statusbar)

        self.retranslateUi(inscrip)
        QtCore.QMetaObject.connectSlotsByName(inscrip)

    def retranslateUi(self, inscrip):
        _translate = QtCore.QCoreApplication.translate
        inscrip.setWindowTitle(_translate("inscrip", "Sign in"))
        self.lineEdit.setText(_translate("inscrip", "Email"))
        self.lineEdit_2.setText(_translate("inscrip", "Password"))
        self.pushButton.setText(_translate("inscrip", "Sign in"))

        self.label_2.setText(_translate("inscrip", "Sign in"))
        self.label_3.setText(_translate("MainWindow", "Optimisation de l\'investissement Dans le Projet  "))
        self.label_4.setText(_translate("MainWindow", "d\'installation d\'une centrale photovoltaïque "))
        self.label_5.setText(_translate("MainWindow", "dans l\'aeroport d\'Alger"))



    def dialoge(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_dialoginscr()
        self.ui.setupUi(self.window)
        self.window.show()





    def insc(self):
        path = 'login.csv'
        # VérifieMainWindowr si le fichier existe ou non
        if os.path.exists(path):
            print("")
        else:
            datatest = "login.csv"
            header = ["Email", "Passw"]

            with open(datatest, "a", newline="") as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(header)
        datatest = "login.csv"
        with open(datatest, "a", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([self.lineEdit.text(), self.lineEdit_2.text()])
        self.dialoge()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    inscripw= QtWidgets.QMainWindow()
    ui = Ui_inscrip()
    ui.setupUi(inscripw)
    inscripw.show()
    sys.exit(app.exec_())
