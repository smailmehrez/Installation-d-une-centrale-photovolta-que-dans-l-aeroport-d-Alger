# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'programe.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

import csv
import os



from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import random
import math
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCan
import warnings
warnings.filterwarnings("ignore")

class Ui_progr(object):
    def setupUi(self, progr):
        progr.setObjectName("progr")
        progr.resize(1500, 1100)
        progr.setStyleSheet("#progr {\n"
"    background-color: #F2F4F4;\n"
"\n"
"}\n"
"#widget  {\n"
"    border-radius: 10px;\n"
"}\n"
"#widget_2 {\n"
"    border: 2px solid #F2F4F4; \n"
"    border-radius: 10px;\n"
"}\n"
"#widget_3 {\n"
"     background-color: #E5E8E8;\n"
"    border: 2px solid #F2F4F4; \n"
"    border-radius: 10px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(progr)
        self.centralwidget.setObjectName("centralwidget")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(290, 200, 1200, 840))
        self.widget_3.setStyleSheet("\n"
"#widget {\n"
"    background-color: #E5E8E8;\n"
"\n"
"}\n"
"#frame  {\n"
"   \n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"#frame_2  {\n"
"   \n"
"    border-radius: 20px;\n"
"}\n"
"#frame_3  {\n"
"   \n"
"    border-radius: 20px;\n"
"}\n"
"#frame_4  {\n"
"   \n"
"    border-radius: 20px;\n"
"}\n"
"#frame_5  {\n"
"   \n"
"    border-radius: 20px;\n"
"}\n"
"#frame_6  {\n"
"   \n"
"    border-radius: 20px;\n"
"}")
        self.widget_3.setObjectName("widget_3")
        self.frame = QtWidgets.QFrame(self.widget_3)
        self.frame.setGeometry(QtCore.QRect(680, 380, 500, 410))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.widget_3)
        self.frame_2.setGeometry(QtCore.QRect(680, 0, 500, 410))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.textEdit = QtWidgets.QTextEdit(self.widget_3)
        self.textEdit.setGeometry(QtCore.QRect(50, 140, 591, 381))
        self.textEdit.setStyleSheet("QTextEdit{\n"
"    background: #E5E8E8;\n"
"   background-color:#E5E8E8;\n"
"    border: 2px solid #E5E8E8; \n"
"    border-radius: 10px; \n"
"    font-family: Constantia;\n"
"    font-size:20px;\n"
"    color: #19060f;\n"
"\n"
"}\n"
"")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.widget_3)
        self.textEdit_2.setGeometry(QtCore.QRect(410, 580, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(-1)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setStyleSheet("QTextEdit{\n"
"    background: #E5E8E8;\n"
"   background-color:#E5E8E8;\n"
"    border: 2px solid #E5E8E8; \n"
"    border-radius: 10px; \n"
"    font-family: Constantia;\n"
"    font-size:20px;\n"
"    color: #19060f;\n"
"\n"
"}\n"
"")
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.widget_3)
        self.pushButton.setGeometry(QtCore.QRect(300, 710, 151, 41))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background: #FFFFFF;\n"
"    background-color:#CCD1D1;\n"
"    font: 25 11pt \"URW Bookman\";\n"
"    border: 2px solid #000000; \n"
"    border-radius: 10px; \n"
"    font-size:20px;\n"
"    color: #19060f;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"     border: 2px solid #E5E8E8; \n"
"     background: #FFFFFF;\n"
"      background-color:#424949;\n"
"      color: #ffffff;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.ok)
        self.textEdit_4 = QtWidgets.QTextEdit(self.widget_3)
        self.textEdit_4.setGeometry(QtCore.QRect(50, 580, 341, 41))
        self.textEdit_4.setStyleSheet("QTextEdit{\n"
"    background: #E5E8E8;\n"
"   background-color:#E5E8E8;\n"
"    border: 2px solid #E5E8E8; \n"
"    border-radius: 10px; \n"
"    font-family: Constantia;\n"
"    font-size:20px;\n"
"    color: #19060f;\n"
"\n"
"}\n"
"")
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_5 = QtWidgets.QTextEdit(self.widget_3)
        self.textEdit_5.setGeometry(QtCore.QRect(50, 80, 591, 41))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(-1)
        self.textEdit_5.setFont(font)
        self.textEdit_5.setStyleSheet("QTextEdit{\n"
"    background: #E5E8E8;\n"
"   background-color:#E5E8E8;\n"
"    border: 2px solid #E5E8E8; \n"
"    border-radius: 10px; \n"
"    font-family: Constantia;\n"
"    font-size:20px;\n"
"    color: #19060f;\n"
"\n"
"}\n"
"")
        self.textEdit_5.setObjectName("textEdit_5")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(10, 200, 271, 841))
        self.widget_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget_2.setStyleSheet("background-color: #E5E8E8;\n"
"\n"
"\n"
"\n"
"\n"
"    ")
        self.widget_2.setObjectName("widget_2")
        self.widget = QtWidgets.QWidget(self.widget_2)
        self.widget.setGeometry(QtCore.QRect(20, 20, 230, 401))
        self.widget.setStyleSheet("#widget{\n"
"\n"
"    border: 2px solid #999f9f; \n"
"    border-radius: 10px; \n"
"}")
        self.widget.setObjectName("widget")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(50, 30, 130, 31))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(19)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.radioButton = QtWidgets.QRadioButton(self.widget)
        self.radioButton.setGeometry(QtCore.QRect(40, 80, 150, 41))
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.radioButton.setFont(font)
        self.radioButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.radioButton.setStyleSheet("QRadioButton{\n"
"    \n"
"    background: #9972e3;\n"
"    background-color:#E5E8E8;\n"
"    font: 25 11pt \"URW Bookman\";\n"
"    border: 2px solid #999f9f; \n"
"    border-radius: 10px; \n"
"    font-size:20px;\n"
"    color: #000000;\n"
"\n"
"}\n"
"QRadioButton:hover{\n"
"     border: 2px solid rgb(153, 193, 241);\n"
"     background: #e375a7;\n"
"     background-color: rgb(153, 193, 241);\n"
"      color: #ffffff;\n"
"}")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_2.setGeometry(QtCore.QRect(40, 140, 150, 41))
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.radioButton_2.setStyleSheet("QRadioButton{\n"
"    \n"
"    background: #9972e3;\n"
"    background-color:#E5E8E8;\n"
"    font: 25 11pt \"URW Bookman\";\n"
"    border: 2px solid #999f9f; \n"
"    border-radius: 10px; \n"
"    font-size:20px;\n"
"    color: #000000;\n"
"\n"
"}\n"
"QRadioButton:hover{\n"
"     border: 2px solid rgb(153, 193, 241);\n"
"     background: #e375a7;\n"
"     background-color: rgb(153, 193, 241);\n"
"      color: #ffffff;\n"
"}")
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(40, 210, 141, 30))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(19)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.radioButton_3 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_3.setGeometry(QtCore.QRect(40, 260, 150, 41))
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.radioButton_3.setStyleSheet("QRadioButton{\n"
"    \n"
"    background: #9972e3;\n"
"    background-color:#E5E8E8;\n"
"    font: 25 11pt \"URW Bookman\";\n"
"    border: 2px solid #999f9f; \n"
"    border-radius: 10px; \n"
"    font-size:20px;\n"
"    color: #000000;\n"
"\n"
"}\n"
"QRadioButton:hover{\n"
"     border: 2px solid rgb(153, 193, 241);\n"
"     background: #e375a7;\n"
"     background-color: rgb(153, 193, 241);\n"
"      color: #ffffff;\n"
"}")
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_4.setGeometry(QtCore.QRect(40, 320, 150, 41))
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.radioButton_4.setStyleSheet("QRadioButton{\n"
"    \n"
"    background: #9972e3;\n"
"    background-color:#E5E8E8;\n"
"    font: 25 11pt \"URW Bookman\";\n"
"    border: 2px solid #999f9f; \n"
"    border-radius: 10px; \n"
"    font-size:20px;\n"
"    color: #000000;\n"
"\n"
"}\n"
"QRadioButton:hover{\n"
"     border: 2px solid rgb(153, 193, 241);\n"
"     background: #e375a7;\n"
"     background-color: rgb(153, 193, 241);\n"
"      color: #ffffff;\n"
"}")
        self.radioButton_4.setObjectName("radioButton_4")
        self.widget_7 = QtWidgets.QWidget(self.widget_2)
        self.widget_7.setGeometry(QtCore.QRect(20, 440, 231, 331))
        self.widget_7.setStyleSheet("#widget_7{\n"
"\n"
"    border: 2px solid #999f9f; \n"
"    border-radius: 10px; \n"
"}")
        self.widget_7.setObjectName("widget_7")
        self.label_5 = QtWidgets.QLabel(self.widget_7)
        self.label_5.setGeometry(QtCore.QRect(30, 40, 60, 20))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(self.widget_7)
        self.lineEdit.setGeometry(QtCore.QRect(90, 40, 113, 25))
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"    background: #FFFFFF;\n"
"   background-color:#FFFFFF;\n"
"    border: 2px solid #000000; \n"
"    border-radius: 10px; \n"
"    font-family: ubuntu;\n"
"    font-size:20px;\n"
"    color: #19060f;\n"
"\n"
"}\n"
"QLineEdit:hover{\n"
"     border: 2px solid #9c9c9c; \n"
"     background: #FFFFFF;\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.label_8 = QtWidgets.QLabel(self.widget_7)
        self.label_8.setGeometry(QtCore.QRect(30, 90, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.widget_7)
        self.label_9.setGeometry(QtCore.QRect(30, 140, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.widget_7)
        self.label_10.setGeometry(QtCore.QRect(30, 190, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(16)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.widget_7)
        self.label_11.setGeometry(QtCore.QRect(30, 240, 31, 20))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(16)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.widget_7)
        self.label_12.setGeometry(QtCore.QRect(30, 290, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(16)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget_7)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 87, 113, 25))
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
"    background: #FFFFFF;\n"
"   background-color:#FFFFFF;\n"
"    border: 2px solid #000000; \n"
"    border-radius: 10px; \n"
"    font-family: ubuntu;\n"
"    font-size:20px;\n"
"    color: #19060f;\n"
"\n"
"}\n"
"QLineEdit:hover{\n"
"     border: 2px solid #9c9c9c; \n"
"     background: #FFFFFF;\n"
"}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget_7)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 137, 113, 25))
        self.lineEdit_3.setStyleSheet("QLineEdit{\n"
"    background: #FFFFFF;\n"
"   background-color:#FFFFFF;\n"
"    border: 2px solid #000000; \n"
"    border-radius: 10px; \n"
"    font-family: ubuntu;\n"
"    font-size:20px;\n"
"    color: #19060f;\n"
"\n"
"}\n"
"QLineEdit:hover{\n"
"     border: 2px solid #9c9c9c; \n"
"     background: #FFFFFF;\n"
"}")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget_7)
        self.lineEdit_4.setGeometry(QtCore.QRect(90, 187, 113, 25))
        self.lineEdit_4.setStyleSheet("QLineEdit{\n"
"    background: #FFFFFF;\n"
"   background-color:#FFFFFF;\n"
"    border: 2px solid #000000; \n"
"    border-radius: 10px; \n"
"    font-family: ubuntu;\n"
"    font-size:20px;\n"
"    color: #19060f;\n"
"\n"
"}\n"
"QLineEdit:hover{\n"
"     border: 2px solid #9c9c9c; \n"
"     background: #FFFFFF;\n"
"}")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget_7)
        self.lineEdit_5.setGeometry(QtCore.QRect(90, 237, 113, 25))
        self.lineEdit_5.setStyleSheet("QLineEdit{\n"
"    background: #FFFFFF;\n"
"   background-color:#FFFFFF;\n"
"    border: 2px solid #000000; \n"
"    border-radius: 10px; \n"
"    font-family: ubuntu;\n"
"    font-size:20px;\n"
"    color: #19060f;\n"
"\n"
"}\n"
"QLineEdit:hover{\n"
"     border: 2px solid #9c9c9c; \n"
"     background: #FFFFFF;\n"
"}")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget_7)
        self.lineEdit_6.setGeometry(QtCore.QRect(90, 287, 113, 25))
        self.lineEdit_6.setStyleSheet("QLineEdit{\n"
"    background: #FFFFFF;\n"
"   background-color:#FFFFFF;\n"
"    border: 2px solid #000000; \n"
"    border-radius: 10px; \n"
"    font-family: ubuntu;\n"
"    font-size:20px;\n"
"    color: #19060f;\n"
"\n"
"}\n"
"QLineEdit:hover{\n"
"     border: 2px solid #9c9c9c; \n"
"     background: #FFFFFF;\n"
"}")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        self.widget_4.setGeometry(QtCore.QRect(10, 10, 1480, 180))
        self.widget_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget_4.setStyleSheet("background-color: #E5E8E8;\n"
"\n"
"\n"
"\n"
"\n"
"    ")
        self.widget_4.setObjectName("widget_4")
        self.label = QtWidgets.QLabel(self.widget_4)
        self.label.setGeometry(QtCore.QRect(415, 10, 651, 50))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(24)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget_4)
        self.label_2.setGeometry(QtCore.QRect(455, 60, 610, 50))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(24)
        font.setStrikeOut(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget_4)
        self.label_3.setGeometry(QtCore.QRect(600, 110, 320, 50))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(24)
        font.setStrikeOut(False)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        progr.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(progr)
        self.statusbar.setObjectName("statusbar")
        progr.setStatusBar(self.statusbar)

        # oooooooooooooooooooooooooooooooooooooooooooooooooooooo
        self.horizontalLayout_11 = QtWidgets.QVBoxLayout(self.frame)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.figure = plt.figure()
        self.canvas = FigureCan(self.figure)
        self.horizontalLayout_11.addWidget(self.canvas)
        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
        self.horizontalLayout_12 = QtWidgets.QVBoxLayout(self.frame_2)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.canvas2 = FigureCan(self.figure)
        self.horizontalLayout_12.addWidget(self.canvas2)

        self.retranslateUi(progr)
        QtCore.QMetaObject.connectSlotsByName(progr)

    def retranslateUi(self, progr):
        _translate = QtCore.QCoreApplication.translate
        progr.setWindowTitle(_translate("progr", "Programe"))
        self.pushButton.setText(_translate("progr", "OK"))
        self.label_4.setText(_translate("progr", "Probleme 1 :"))
        self.radioButton.setText(_translate("progr", "Genitique 1"))
        self.radioButton_2.setText(_translate("progr", "Genitique 2"))
        self.label_7.setText(_translate("progr", "Probleme 2 :"))
        self.radioButton_3.setText(_translate("progr", "RECUIT 1"))
        self.radioButton_4.setText(_translate("progr", "RECUIT 2"))
        self.label_5.setText(_translate("progr", "Type :"))
        self.label_8.setText(_translate("progr", "N   :"))
        self.label_9.setText(_translate("progr", "E   :"))
        self.label_10.setText(_translate("progr", "F   :"))
        self.label_11.setText(_translate("progr", "W :"))
        self.label_12.setText(_translate("progr", "D  : "))
        self.label.setText(_translate("progr", "Optimisation de l\'investissement Dans le Projet  "))
        self.label_2.setText(_translate("progr", "d\'installation d\'une centrale photovoltaïque "))
        self.label_3.setText(_translate("progr", "dans l\'aeroport d\'Alger"))


    def ok(self):
            self.figure.clear()
            if (self.radioButton.isChecked() == True):
                    self.radioButton_2.setChecked(False)
                    self.radioButton_3.setChecked(False)
                    self.radioButton_4.setChecked(False)
                    self.H1()
            if (self.radioButton_2.isChecked() == True):
                    self.radioButton.setChecked(False)
                    self.radioButton_3.setChecked(False)
                    self.radioButton_4.setChecked(False)
                    self.H2()
            if (self.radioButton_3.isChecked() == True):
                    self.radioButton.setChecked(False)
                    self.radioButton_2.setChecked(False)
                    self.radioButton_4.setChecked(False)
                    self.H3()
            if (self.radioButton_4.isChecked() == True):
                    self.radioButton.setChecked(False)
                    self.radioButton_2.setChecked(False)
                    self.radioButton_3.setChecked(False)
                    self.H4()

    def H1(self):
            # Load the Excel file

            df = pd.read_excel("gener_donnes.xlsx", sheet_name="Sheet")

            cotes = df["Côté"].values.tolist()

            couts = df["Coût"].tolist()
            longueurs = df["Longueur"].tolist()
            puissance = df["Puissance"].tolist()
            N = int(self.lineEdit_2.text())
            M = len(longueurs)  # nombre des plaques
            E = int(self.lineEdit_3.text())  # les supports
            F = int(self.lineEdit_4.text())  # les cotes
            typ = int(self.lineEdit.text())  # les types
            # Création de la liste des côtés uniques
            cotes_uniques = list(set(cotes))
            # Tri des côtés dans l'ordre numérique
            cotes_uniques.sort()
            # Création du tableau 'puis' avec les dimensions appropriées
            puis = np.zeros((typ, N, E, len(cotes_uniques)))

            # Remplissage du tableau 'puis' avec les valeurs de puissance appropriées
            for i in range(typ):
                    for j in range(N):
                            for l in range(E):
                                    for k in range(len(cotes_uniques)):
                                            cote = cotes_uniques[k]
                                            if cote in cotes[
                                                       i * N * E * len(cotes_uniques) + j * E * len(
                                                               cotes_uniques) + l * len(cotes_uniques): (
                                                                                                                i + 1) * N * E * len(
                                                               cotes_uniques) + j * E * len(cotes_uniques) + (
                                                                                                                l + 1) * len(
                                                               cotes_uniques)]:
                                                    puis[i][j][l][k] = puissance[
                                                            i * N * E * len(cotes_uniques) + j * E * len(
                                                                    cotes_uniques) + l * len(
                                                                    cotes_uniques) + cotes.index(cote)]

            # Création de la matrice 'lon' avec les dimensions appropriées
            lon = np.zeros((typ, N))
            for i in range(typ):
                    for j in range(N):
                            lon[i][j] = longueurs[j]

            print(lon)
            # print(lon)
            # Création de la matrice 'c' avec les dimensions appropriées
            c = np.zeros((typ, N))
            for i in range(typ):
                    for j in range(N):
                            c[i][j] = couts[j]
            # print(c)

            L = [1000, 1003, 426, 3242, 2342, 324, 2423, 2423, 2342]
            e = 50
            D = 20000000
            mutation_proba = 0.1

            # Génération d'une population initiale de chromosomes aléatoires
            def G_population():
                    mat_sol = []
                    for i in range(typ):
                            plaque = []
                            for j in range(N):
                                    dim = []
                                    for l in range(E):
                                            support = []
                                            for k in range(F):
                                                    support.append(random.choice([0, 1]))
                                            dim.append(support)
                                    plaque.append(dim)
                            mat_sol.append(plaque)
                    return mat_sol

            # print(G_population())
            # fonction qui verifier la longeur
            x = G_population()

            def longeur(lon, e, L, x):
                    y = 0
                    for i in range(typ):
                            for j in range(N):
                                    for l in range(E):
                                            for k in range(F):
                                                    if x[i][j][l][k] != 0:
                                                            y += lon[i][j]
                                                            if y + e > L[l] + e:
                                                                    return False
                    return True

            # print(longeur(lon,e,L,x))
            # faction qui verifier la puissance
            x = G_population()

            # print(x)
            def puissance(puis, x):
                    a = np.array(puis)
                    b = np.array(x)
                    s = a[:, np.newaxis, np.newaxis] * b
                    c = np.sum(s)
                    # print(c)
                    bool = False
                    if c >= D:
                            bool = True

                    return bool

            # print(puissance(puis,x))

            x = G_population()
            # print(x)
            puiss = puissance(puis, x)
            long = longeur(lon, e, L, x)

            def attrib(x, puiss, long):
                    puiss = puissance(puis, x)
                    long = longeur(lon, e, L, x)
                    while puiss == False and long == False:
                            for i in range(typ):
                                    # print(x)
                                    for j in range(N):
                                            for l in range(E):
                                                    for k in range(F):
                                                            if x[i][j][l][k] != 0:
                                                                    x[i][j][l][k] = x[i][j][l][k] + 1
                            puiss = puissance(puis, x)
                            long = longeur(lon, e, L, x)

                    return x

            # print(attrib(x,puiss,long))

            x = G_population()
            v = attrib(x, puiss, long)

            def selection(v):
                    puiss = puissance(puis, v)
                    long = longeur(lon, e, L, v)
                    slt_parents = []
                    for k in range(2):
                            fitness_parents = random.uniform(0, 1)
                            while fitness_parents < 0.5:
                                    fitness_parents = random.uniform(0, 1)
                                    # print(fitness_parents)
                            for typ in v:
                                    for i in typ:
                                            for j in i:
                                                    if fitness_parents >= 0.5 and len(slt_parents) < 4:
                                                            slt_parents.append(typ)

                    return slt_parents

            parents = selection(v)
            # print(parents)
            v = attrib(x, puiss, long)

            # print(v)
            # print(np.shape(v))

            def croisement_un_point(parents, v):
                    # if len(parents) < 4:
                    # raise ValueError("La liste des parents ne contient pas suffisamment d'éléments.")

                    parent1, parent2 = parents[0], parents[1]  # Sélection des deux premiers parents

                    # Vérification du type des parents
                    # if not isinstance(parent1, list) or not isinstance(parent2, list):
                    # raise TypeError("Les parents doivent être des listes contenant les informations des parents.")

                    # Sélection d'un point de croisement aléatoire
                    point_croisement = len(v)
                    # print(point_croisement)

                    child1 = parent1[:point_croisement] + parent2[point_croisement:]
                    # print(child1)
                    child2 = parent2[:point_croisement] + parent1[point_croisement:]

                    return child1, child2

            # print(croisement_un_point(parents,v))
            # print("-------------------------fils------------------")

            # print("child 1:",child1)
            # print("-------------------------------------------------------")
            # print("child 2:", child2)

            x = G_population()
            v = attrib(x, puiss, long)
            parents = selection(v)

            def cout(c, x):
                    a = np.array(c)
                    # print(a)
                    b = np.array(x)
                    w = a[:, :, np.newaxis, np.newaxis] * b[:, :, np.newaxis, np.newaxis]
                    q = np.sum(w)
                    # print(q)
                    return q

            new_mat_sol1 = []
            new_mat_sol2 = []
            x = G_population()
            v = attrib(x, puiss, long)
            child1 = croisement_un_point(parents, v)
            child2 = croisement_un_point(parents, v)
            puiss1 = puissance(puis, child1)
            puiss2 = puissance(puis, child2)
            long1 = longeur(lon, e, L, child1)
            long2 = longeur(lon, e, L, child2)

            def correctrice(v, puiss1, puiss2, long1, long2):
                    new_mat_sol1 = v.copy()
                    new_mat_sol2 = v.copy()
                    for i in range(typ):
                            for j in range(N):
                                    for l in range(E):
                                            for k in range(F):
                                                    if puiss1 == False:
                                                            if child1[i][j][l][k] == 0 and long1 == False:
                                                                    child1[i][j][l][k] = child1[i][j][l][k] + 1
                                                    if puiss2 == False:
                                                            if child2[i][j][l][k] == 0 and long2 == False:
                                                                    child2[i][j][l][k] = child2[i][j][l][k] + 1

                    if cout(c, v) <= cout(c, child1):
                            new_mat_sol1 = v
                    else:
                            new_mat_sol1 = child1

                    if cout(c, v) <= cout(c, child2):
                            new_mat_sol2 = v
                    else:
                            new_mat_sol2 = child2

                    return new_mat_sol1, new_mat_sol2

            # print(new_mat_sol1,new_mat_sol2)

            # print("--------------------------correction------------------")

            # print("child 1:",new_mat_sol1)
            # print("-------------------------------------------------------")
            # print("child 2:", new_mat_sol2)

            # print(correctrice(v, puiss1,puiss2,long1,long2))
            new_mat_sol1, new_mat_sol2 = correctrice(v, puiss1, puiss2, long1, long2)

            # size=np.sum(random_values < mutation_proba),.tolist()
            def mutation(new_mat_sol1, new_mat_sol2):
                    for i in range(typ):
                            for j in range(N):
                                    for l in range(E):
                                            for k in range(F):
                                                    if random.random() < mutation_proba:
                                                            new_mat_sol1[i][j][l][k] = random.choice([0, 1])
                                                            new_mat_sol2[i][j][l][k] = random.choice([0, 1])

                    return new_mat_sol1, new_mat_sol2

            child_1, child_2 = mutation(new_mat_sol1, new_mat_sol2)
            # print("Résultat de mutation :", child_1)
            # print("Résultat de mutation :", child_2)
            # Fonction génétique
            puiss1 = puissance(puis, child1)
            puiss2 = puissance(puis, child2)
            long1 = longeur(lon, e, L, child1)
            long2 = longeur(lon, e, L, child2)

            def genetic_algorithm():
                    x = G_population()
                    puiss = puissance(puis, x)
                    long = longeur(lon, e, L, x)
                    v = attrib(x, puiss, long)
                    parents = selection(v)
                    for generation in range(10):
                            new_population = []
                            for i in range(M // 2):
                                    child1 = croisement_un_point(parents, v)
                                    child2 = croisement_un_point([parents[1], parents[0]], v)
                                    # print(child1)
                                    puiss1 = puissance(puis, child1)
                                    puiss2 = puissance(puis, child2)
                                    long1 = longeur(lon, e, L, child1)
                                    long2 = longeur(lon, e, L, child2)
                                    parents = selection(v)
                                    new_mat_sol1, new_mat_sol2 = correctrice(v, puiss1, puiss2, long1, long2)
                                    f1_fit = attrib(new_mat_sol1, puiss, long)
                                    f2_fit = attrib(new_mat_sol2, puiss, long)
                                    # print(f1_fit)
                                    child_1, child_2 = mutation(new_mat_sol1, new_mat_sol2)
                                    # print(child_1)
                                    # print(child_2)
                                    new_population.append(child_1)
                                    new_population.append(child_2)
                            x = new_population
                    best_chromosome = max(x, key=lambda x: attrib(x, puiss, long))
                    best_fitness = cout(c, best_chromosome)
                    return best_chromosome, best_fitness

            ## exécution de l'algorithme génétique
            best_chromosome, best_fitness = genetic_algorithm()
            # print("La  generation de population est:", x)
            # print("------------------------------------------------------------------------")
            # print("la selection des parents :",parents)
            # print("----------------------------------------------------------------------")
            # print("le croisement des child ",child1,child2)
            # print("-----------------------------------------------------")
            # print("")
            mil="Meilleur chromosome :"
            self.textEdit_5.setText(str( mil))
            datatest = "Meilleur_chromosome.csv"
            header = ["Meilleur_chromosome"]
            with open(datatest, "w", newline="") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(header)
                    for i in range (len(best_chromosome)):
                            for j in range (len(best_chromosome[0])):
                                    for k in range (len(best_chromosome[0][0])):
                                            writer.writerow([best_chromosome[i][j][k]])
            pd.set_option('display.max_rows', None)
            pd.set_option('display.max_columns', None)
            dk = pd.read_csv("Meilleur_chromosome.csv")
            self.textEdit.setText(str(dk["Meilleur_chromosome"]))





            #print("Meilleur chromosome:", best_chromosome)
            #self.textEdit.setText(str(best_chromosome))
            #print("Fitness du meilleur chromosome:", best_fitness)
            mil="best_fitness  :"
            self.textEdit_4.setText(str(mil))
            self.textEdit_2.setText(str(best_fitness))

    def H2(self):
            # Load the Excel file

            df = pd.read_excel("gener_donnes.xlsx", sheet_name="Sheet")

            cotes = df["Côté"].values.tolist()

            couts = df["Coût"].tolist()
            longueurs = df["Longueur"].tolist()
            puissance = df["Puissance"].tolist()
            N = int(self.lineEdit_2.text())
            M = len(longueurs)  # nombre des plaques
            E = int(self.lineEdit_3.text()) # les supports
            F = int(self.lineEdit_4.text())  # les cotes
            typ = int(self.lineEdit.text())  # les types
            # Création de la liste des côtés uniques
            cotes_uniques = list(set(cotes))
            # Tri des côtés dans l'ordre numérique
            cotes_uniques.sort()
            # Création du tableau 'puis' avec les dimensions appropriées
            puis = np.zeros((typ, N, E, len(cotes_uniques)))

            # Remplissage du tableau 'puis' avec les valeurs de puissance appropriées
            for i in range(typ):
                    for j in range(N):
                            for l in range(E):
                                    for k in range(len(cotes_uniques)):
                                            cote = cotes_uniques[k]
                                            if cote in cotes[
                                                       i * N * E * len(cotes_uniques) + j * E * len(
                                                               cotes_uniques) + l * len(cotes_uniques): (
                                                                                                                i + 1) * N * E * len(
                                                               cotes_uniques) + j * E * len(cotes_uniques) + (
                                                                                                                l + 1) * len(
                                                               cotes_uniques)]:
                                                    puis[i][j][l][k] = puissance[
                                                            i * N * E * len(cotes_uniques) + j * E * len(
                                                                    cotes_uniques) + l * len(
                                                                    cotes_uniques) + cotes.index(cote)]

            # Création de la matrice 'lon' avec les dimensions appropriées
            lon = np.zeros((typ, N))
            for i in range(typ):
                    for j in range(N):
                            lon[i][j] = longueurs[j]

            # print(lon)
            # print(lon)
            # Création de la matrice 'c' avec les dimensions appropriées
            c = np.zeros((typ, N))
            for i in range(typ):
                    for j in range(N):
                            c[i][j] = couts[j]
            # print(c)

            L = [10000, 10903, 4926, 3242, 2342, 324, 2423, 2423, 2342]
            e = 50
            D = 20000000
            mutation_proba = 0.1

            # Génération d'une population initiale de chromosomes aléatoires
            # Fonction pour attribuer les plaques en fonction de la puissance et de la longueur
            # Fonction pour attribuer les plaques en fonction de la puissance et de la longueur
            def heuristic_plaque_assignment():
                    mat_sol = []
                    for i in range(typ):
                            plaque = []
                            for j in range(N):
                                    dim = []
                                    for l in range(E):
                                            support = []
                                            for k in range(F):
                                                    if k < 2:
                                                            # Attribuer aléatoirement des plaques en fonction de la puissance et de la longueur
                                                            if puis[i][j][l][k] <= D and lon[i][j] + e <= L[l] + e:
                                                                    support.append(1)
                                                            else:
                                                                    support.append(0)
                                                    else:
                                                            support.append(0)
                                            dim.append(support)
                                    plaque.append(dim)
                            mat_sol.append(plaque)
                    return mat_sol

            x = heuristic_plaque_assignment()

            # print(x)

            def longeur(lon, e, L, x):
                    y = np.zeros((E, F))
                    a = np.array(lon)
                    b = np.array(x)
                    c = a[:, :, np.newaxis, np.newaxis] * b
                    # print(c)
                    for i in range(typ):
                            for j in range(N):
                                    for l in range(E):
                                            for k in range(F):
                                                    y[l][k] += c[i][j][l][k]
                                                    # print(y[i][j])
                                                    if y[l][k] + e > L[l] + e:
                                                            y[l][k] = False
                                                            break

                    return y.astype(bool)

            v = longeur(lon, e, L, x)

            # print(longeur(lon,e,L,x))
            # faction qui verifier la puissance
            x = heuristic_plaque_assignment()

            def puissance(puis, x):
                    a = np.array(puis)
                    b = np.array(x)
                    s = a * b[:, :, np.newaxis, np.newaxis]
                    c = np.sum(s)
                    bool = False
                    if c >= D:
                            bool = True

                    return bool

            # print(puissance(puis,x))

            puiss = puissance(puis, x)
            # print(puiss)
            long = longeur(lon, e, L, x)

            # print(long)

            def attrib(x, puiss, long):
                    while puiss == False:
                            for i in range(typ):
                                    # print(x)
                                    for j in range(N):
                                            for l in range(E):
                                                    for k in range(F):
                                                            if long[l][k] == False:
                                                                    if x[i][j][l][k] == 0:
                                                                            x[i][j][l][k] = x[i][j][l][k] + 1


                                                            else:
                                                                    if x[i][j][l][k] != 0:
                                                                            x[i][j][l][k] = x[i][j][l][k] + 1

                            puiss = puissance(puis, x)
                            long = longeur(lon, e, L, x)
                            break

                    return x

            # print(attrib(x,puiss,long))

            x = heuristic_plaque_assignment()
            v = attrib(x, puiss, long)

            # print(v)

            def selection(v):
                    puiss = puissance(puis, v)
                    long = longeur(lon, e, L, v)
                    slt_parents = []
                    for k in range(2):
                            fitness_parents = random.uniform(0, 1)
                            while fitness_parents < 0.5:
                                    fitness_parents = random.uniform(0, 1)
                                    # print(fitness_parents)
                            for typ in v:
                                    for i in typ:
                                            for j in i:
                                                    if fitness_parents >= 0.5 and len(slt_parents) < 4:
                                                            slt_parents.append(typ)

                    return slt_parents

            parents = selection(v)
            # print(parents)
            v = attrib(x, puiss, long)

            # print(v)
            # print(np.shape(v))

            def croisement_un_point(parents, v):
                    # if len(parents) < 4:
                    # raise ValueError("La liste des parents ne contient pas suffisamment d'éléments.")

                    parent1, parent2 = parents[0], parents[1]  # Sélection des deux premiers parents

                    # Vérification du type des parents
                    # if not isinstance(parent1, list) or not isinstance(parent2, list):
                    # raise TypeError("Les parents doivent être des listes contenant les informations des parents.")

                    # Sélection d'un point de croisement aléatoire
                    point_croisement = len(v)
                    # print(point_croisement)

                    child1 = parent1[:point_croisement] + parent2[point_croisement:]
                    # print(child1)
                    child2 = parent2[:point_croisement] + parent1[point_croisement:]

                    return child1, child2

            # print(croisement_un_point(parents,v))
            # print("-------------------------fils------------------")

            # print("child 1:",child1)
            # print("-------------------------------------------------------")
            # print("child 2:", child2)

            x = heuristic_plaque_assignment()
            v = attrib(x, puiss, long)
            parents = selection(v)

            def cout(c, x):
                    a = np.array(c)
                    # print(a)
                    b = np.array(x)
                    w = a[:, :, np.newaxis, np.newaxis] * b[:, :, np.newaxis, np.newaxis]
                    q = np.sum(w)
                    # print(q)
                    return q

            new_mat_sol1 = []
            new_mat_sol2 = []
            x = heuristic_plaque_assignment()
            v = attrib(x, puiss, long)
            child1 = croisement_un_point(parents, v)
            child2 = croisement_un_point(parents, v)
            puiss1 = puissance(puis, child1)
            puiss2 = puissance(puis, child2)
            long1 = longeur(lon, e, L, child1)
            long2 = longeur(lon, e, L, child2)

            def correctrice(v, puiss1, puiss2, long1, long2):
                    new_mat_sol1 = v.copy()
                    new_mat_sol2 = v.copy()
                    for i in range(typ):
                            for j in range(N):
                                    for l in range(E):
                                            for k in range(F):
                                                    if puiss1 == False:
                                                            if child1[i][j][l][k] == 0 and long1[l][k] == False:
                                                                    child1[i][j][l][k] = child1[i][j][l][k] + 1
                                                    if puiss2 == False:
                                                            if child2[i][j][l][k] == 0 and long2[l][k] == False:
                                                                    child2[i][j][l][k] = child2[i][j][l][k] + 1

                    if cout(c, v) <= cout(c, child1):
                            new_mat_sol1 = v
                    else:
                            new_mat_sol1 = child1

                    if cout(c, v) <= cout(c, child2):
                            new_mat_sol2 = v
                    else:
                            new_mat_sol2 = child2

                    return new_mat_sol1, new_mat_sol2

            # print(new_mat_sol1,new_mat_sol2)

            # print("--------------------------correction------------------")

            # print("child 1:",new_mat_sol1)
            # print("-------------------------------------------------------")
            # print("child 2:", new_mat_sol2)

            # print(correctrice(v, puiss1,puiss2,long1,long2))
            new_mat_sol1, new_mat_sol2 = correctrice(v, puiss1, puiss2, long1, long2)

            # size=np.sum(random_values < mutation_proba),.tolist()
            def mutation(new_mat_sol1, new_mat_sol2):
                    for i in range(typ):
                            for j in range(N):
                                    for l in range(E):
                                            for k in range(F):
                                                    if random.random() < mutation_proba:
                                                            new_mat_sol1[i][j][l][k] = random.choice([0, 1])
                                                            new_mat_sol2[i][j][l][k] = random.choice([0, 1])

                    return new_mat_sol1, new_mat_sol2

            child_1, child_2 = mutation(new_mat_sol1, new_mat_sol2)
            # print("Résultat de mutation :", child_1)
            # print("Résultat de mutation :", child_2)
            # Fonction génétique
            puiss1 = puissance(puis, child1)
            puiss2 = puissance(puis, child2)
            long1 = longeur(lon, e, L, child1)
            long2 = longeur(lon, e, L, child2)

            def genetic_algorithm():
                    x = heuristic_plaque_assignment()
                    puiss = puissance(puis, x)
                    long = longeur(lon, e, L, x)
                    v = attrib(x, puiss, long)
                    parents = selection(v)
                    for generation in range(10):
                            new_population = []
                            for i in range(M // 2):
                                    child1 = croisement_un_point(parents, v)
                                    child2 = croisement_un_point([parents[1], parents[0]], v)
                                    # print(child1)
                                    puiss1 = puissance(puis, child1)
                                    puiss2 = puissance(puis, child2)
                                    long1 = longeur(lon, e, L, child1)
                                    long2 = longeur(lon, e, L, child2)
                                    parents = selection(v)
                                    new_mat_sol1, new_mat_sol2 = correctrice(v, puiss1, puiss2, long1, long2)
                                    f1_fit = attrib(new_mat_sol1, puiss, long)
                                    f2_fit = attrib(new_mat_sol2, puiss, long)
                                    # print(f1_fit)
                                    child_1, child_2 = mutation(new_mat_sol1, new_mat_sol2)
                                    # print(child_1)
                                    # print(child_2)
                                    new_population.append(child_1)
                                    new_population.append(child_2)
                            x = new_population
                    best_chromosome = max(x, key=lambda x: attrib(x, puiss, long))
                    best_fitness = cout(c, best_chromosome)
                    return best_chromosome, best_fitness

            ## exécution de l'algorithme génétique
            best_chromosome, best_fitness = genetic_algorithm()
            # print("La  generation de population est:", x)
            # print("------------------------------------------------------------------------")
            # print("la selection des parents :",parents)
            # print("----------------------------------------------------------------------")
            # print("le croisement des child ",child1,child2)
            # print("-----------------------------------------------------")
            # print("")
           # print("Meilleur chromosome:", best_chromosome)
            #print("Fitness du meilleur chromosome:", best_fitness)



            mil = "Meilleur chromosome :"
            self.textEdit_5.setText(str(mil))
            # print("Meilleur chromosome:", best_chromosome)
            #self.textEdit.setText(str(best_chromosome))
            datatest = "Meilleur_chromosome.csv"
            header = ["Meilleur_chromosome"]
            with open(datatest, "w", newline="") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(header)
                    for i in range(len(best_chromosome)):
                            for j in range(len(best_chromosome[0])):
                                    for k in range(len(best_chromosome[0][0])):
                                            writer.writerow([best_chromosome[i][j][k]])
            pd.set_option('display.max_rows', None)
            pd.set_option('display.max_columns', None)
            dk = pd.read_csv("Meilleur_chromosome.csv")
            self.textEdit.setText(str(dk["Meilleur_chromosome"]))
            # print("Fitness du meilleur chromosome:", best_fitness)
            mil = "best_fitness  :"
            self.textEdit_4.setText(str(mil))
            self.textEdit_2.setText(str(best_fitness))

    def H3(self):
            # Lecture des données des plaques à partir du fichier Excel
            data_plaques = pd.read_excel("gener_donnes.xlsx", sheet_name="Sheet")

            # Lecture des données des onduleurs à partir du fichier Excel
            data_onduleurs = pd.read_excel("gener_donnes.xlsx", sheet_name="Onduleurs")

            # Extraction des données de plaques
            resultat = data_plaques["Puissance"].values.tolist()

            co = data_onduleurs["Coût unitaire (€)"].values.tolist()

            cap = data_onduleurs["Capacité (Kw)"].values.tolist()  # Capacités restantes des onduleur

            cap_onduleur = cap.copy()  # Capacités restantes des onduleurs
            M = len(cap_onduleur)  # Nombre d'onduleurs

            liste_plq_onduleur = [[] for _ in range(M)]  # Liste des plaques affectées à chaque onduleur

            def count_used_onduleur(liste_plq_onduleur):
                    used_onduleur = []
                    for onduleur in liste_plq_onduleur:
                            if len(onduleur) > 0:
                                    used_onduleur.append(1)
                            else:
                                    used_onduleur.append(0)
                    return used_onduleur

            def fitness(x, co):
                    f = 0
                    used_onduleur = count_used_onduleur(x)

                    for j in range(M):
                            f += used_onduleur[j] * co[j]

                    return f

            def generer_solution_consecutive():
                    random.shuffle(resultat)  # Mélanger la liste des plaques non affectées pour une sélection aléatoire

                    for t in range(len(resultat)):
                            plaque = resultat[t]  # Plaque en cours d'affectation
                            onduleur_index = 0  # Indice de l'onduleur en cours d'affectation
                            while onduleur_index < M:
                                    if plaque <= cap_onduleur[onduleur_index]:
                                            liste_plq_onduleur[onduleur_index].append(
                                                    plaque)  # Ajouter la plaque à la liste des plaques affectées à l'onduleur
                                            cap_onduleur[
                                                    onduleur_index] -= plaque  # Mettre à jour la capacité restante de l'onduleur
                                            break
                                    onduleur_index += 1
                            if onduleur_index == M:
                                    liste_plq_onduleur.append(
                                            [plaque])  # Ajouter un nouvel onduleur avec la plaque affectée
                                    cap_onduleur.append(cap[0])  # Ajouter la capacité de l'onduleur par défaut

                    cout = fitness(liste_plq_onduleur, co)
                    # Affichage des résultats
                    used_onduleur = count_used_onduleur(liste_plq_onduleur)
                    # for i, plaques in enumerate(liste_plq_onduleur):
                    # print(f"Onduleur {i}: {plaques}, Utilisé: {used_onduleur[i]} fois")

                    # print("le cout total est : f=", cout)

                    return resultat, cap_onduleur, liste_plq_onduleur, cout

            resultat, cap_onduleur, liste_plq_onduleur, cout = generer_solution_consecutive()

            # Fonction pour générer un voisin en échangeant deux plaques entre deux onduleurs
            def generer_voisin(liste_plq_onduleur):
                    i = random.randint(0, len(liste_plq_onduleur) - 1)  # Sélectionner un onduleur aléatoire

                    # Vérifier si l'onduleur sélectionné a des plaques affectées
                    while len(liste_plq_onduleur[i]) == 0:
                            i = random.randint(0, len(liste_plq_onduleur) - 1)

                    j = random.randint(0, len(
                            liste_plq_onduleur[i]) - 1)  # Sélectionner une plaque aléatoire dans l'onduleur i

                    # Sélectionner un autre onduleur différent de i
                    k = random.randint(0, len(liste_plq_onduleur) - 1)
                    while k == i or len(liste_plq_onduleur[k]) == 0:
                            k = random.randint(0, len(liste_plq_onduleur) - 1)

                    # Échanger les deux plaques entre les onduleurs i et k
                    plaque_i = liste_plq_onduleur[i].pop(j)
                    plaque_k = random.choice(liste_plq_onduleur[k])
                    liste_plq_onduleur[k].remove(plaque_k)
                    liste_plq_onduleur[i].append(plaque_k)
                    liste_plq_onduleur[k].append(plaque_i)

                    return liste_plq_onduleur

            t = generer_voisin(liste_plq_onduleur)

            # Fonction pour calculer la température
            def temperature(init_temp, iteration):
                    return init_temp * math.exp(-0.01 * iteration)

            # Fonction pour évaluer la qualité d'une solution en utilisant la fonction fitness
            def evaluer(solution, co):
                    return fitness(solution, co)

            # Fonction principale pour l'algorithme du recuit simulé

            # Fonction principale pour l'algorithme du recuit simulé
            def recuit_simule(init_solution, co, init_temp, temp_min, max_iter):
                    meilleure_solution = init_solution.copy()
                    meilleure_cout = evaluer(meilleure_solution, co)
                    solution_actuelle = init_solution.copy()
                    cout_actuel = evaluer(solution_actuelle, co)

                    temperature_history = []  # Liste pour stocker l'historique des températures
                    cout_diff_history = []  # Liste pour stocker l'évolution de la différence de coût

                    iteration = 0
                    while init_temp > temp_min and iteration < max_iter:
                            T = temperature(init_temp, iteration)
                            temperature_history.append(T)

                            voisin = generer_voisin(solution_actuelle)
                            cout_voisin = evaluer(voisin, co)

                            delta_cout = cout_voisin - cout_actuel

                            if delta_cout < 0 or random.uniform(0, 1) < math.exp(-delta_cout / T):
                                    solution_actuelle = voisin
                                    cout_actuel = cout_voisin

                                    if cout_actuel < meilleure_cout:
                                            meilleure_solution = solution_actuelle.copy()
                                            meilleure_cout = cout_actuel

                            cout_diff = meilleure_cout - cout_actuel
                            cout_diff_history.append(cout_diff)  # Ajouter la différence de coût à l'historique

                            init_temp = temperature(init_temp, iteration)
                            iteration += 1

                    return meilleure_solution, meilleure_cout, cout_diff_history, temperature_history

            # Utilisation de l'algorithme du recuit simulé pour améliorer la solution
            solution_initiale = liste_plq_onduleur.copy()
            temperature_initiale = 60000.0
            temperature_minimale = 0.01
            nombre_iterations = 1000

            meilleure_solution, meilleure_cout, cout_diff_history, temperature_history = recuit_simule(
                    solution_initiale, co, temperature_initiale, temperature_minimale, nombre_iterations)

            #print("Meilleure solution trouvée:")
            used_onduleur = count_used_onduleur(meilleure_solution)
            datatest = "meilleure_solut.csv"
            header = ["meilleure_solution"]
            with open(datatest, "w", newline="") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(header)
                    for i, plaques in enumerate(meilleure_solution):
                            writer.writerow([f"Onduleur {i}: {plaques}, Utilisé: {used_onduleur[i]} fois"])
               #self.textEdit.setText(str(f"Onduleur {i}: {plaques}, Utilisé: {used_onduleur[i]} fois"))

            pd.set_option('display.max_rows', None)
            pd.set_option('display.max_columns', None)

            dv=pd.read_csv("meilleure_solut.csv")
            self.textEdit.setText(str(dv.to_string(index=False)))

            #print("Meilleur coût:", meilleure_cout)
            #self.textEdit.setText(str(best_chromosome))
            self.textEdit_2.setText(str(meilleure_cout))

            # Tracer l'évolution de la différence de coût en fonction de l'itération
            iterations = range(1, len(cout_diff_history) + 1)

            mil = " Meilleure solution trouvée :"
            self.textEdit_5.setText(str(mil))
            # print("Meilleur chromosome:", best_chromosome)
            #self.textEdit.setText(str(meilleure_solution))
            # print("Fitness du meilleur chromosome:", best_fitness)
            mil = "Meilleur coût  :"
            self.textEdit_4.setText(str(mil))

            self.figure.clear()
            plt.plot(iterations, cout_diff_history)
            plt.xlabel("Itération")
            plt.ylabel("Différence de coût")
            plt.title("Évolution de la différence de coût entre la meilleure solution et la solution actuelle")
            self.canvas2.draw()
            self.figure.clear()
            plt.plot(temperature_history)
            plt.xlabel('Iteration')
            plt.ylabel('Température')
            plt.title('Recuit simulé - Évolution de la température')
            self.canvas.draw()

    def H4(self):
            # Lecture des données des plaques à partir du fichier Excel
            data_plaques = pd.read_excel("gener_donnes.xlsx", sheet_name="Sheet")

            # Lecture des données des onduleurs à partir du fichier Excel
            data_onduleurs = pd.read_excel("gener_donnes.xlsx", sheet_name="Onduleurs")

            # Extraction des données de plaques
            puis = data_plaques["Puissance"].values.tolist()

            co = data_onduleurs["Coût unitaire (€)"].values.tolist()

            cap = data_onduleurs["Capacité (Kw)"].values.tolist()  # Capacités restantes des onduleurs

            M = len(cap)  # Nombre d'onduleurs

            liste_plq_onduleur = [[] for _ in range(M)]  # Liste des plaques affectées à chaque onduleur

            def count_used_onduleur(liste_plq_onduleur):
                    used_onduleur = []
                    for onduleur in liste_plq_onduleur:
                            if len(onduleur) > 0:
                                    used_onduleur.append(1)
                            else:
                                    used_onduleur.append(0)
                    return used_onduleur

            def fitness(x, co):
                    f = 0
                    used_onduleur = count_used_onduleur(x)
                    for j in range(M):
                            f += used_onduleur[j] * co[j]
                    return f

            def generer_solution_consecutive():
                    # Initialiser les listes
                    cap_onduleur = [0] * M  # capacité restante pour chaque onduleur
                    matrice_plaque_nonaff = puis.copy()  # liste des plaques non affectées à l'onduleur
                    liste_plq_onduleur = [[] for _ in range(M)]  # Initialiser une liste vide pour chaque onduleur
                    solution = []  # Initialiser la solution finale

                    # Tri des plaques en ordre décroissant de puissance
                    matrice_plaque_nonaff.sort(reverse=True)

                    # Affecter les onduleurs
                    for i in range(M):
                            cap_onduleur[i] = cap[i]  # Capacité initiale de l'onduleur

                            while cap_onduleur[i] > 0 and len(matrice_plaque_nonaff) > 0:
                                    plaque = matrice_plaque_nonaff[
                                            0]  # Prendre la plaque la plus puissante non affectée

                                    if plaque <= cap_onduleur[i]:
                                            liste_plq_onduleur[i].append(plaque)  # Affecter la plaque à l'onduleur i
                                            cap_onduleur[
                                                    i] -= plaque  # Mettre à jour la capacité restante de l'onduleur i
                                            matrice_plaque_nonaff.pop(
                                                    0)  # Supprimer la plaque de la liste des plaques non affectées
                                    else:
                                            break  # Si la plaque ne peut pas être affectée à l'onduleur i, passer à l'onduleur suivant

                    # Ajouter les plaques affectées à chaque onduleur à la solution finale
                    solution = liste_plq_onduleur.copy()
                    cout = fitness(liste_plq_onduleur, co)

                    return solution, cap_onduleur, matrice_plaque_nonaff, cout

            # Tester la fonction generer_solution_consecutive()
            solution, cap_onduleur, matrice_plaque_nonaff, cout = generer_solution_consecutive()

            # Reste du code...

            # Fonction pour générer un voisin en échangeant deux plaques entre deux onduleurs
            def generer_voisin(liste_plq_onduleur):
                    i = random.randint(0, len(liste_plq_onduleur) - 1)  # Sélectionner un onduleur aléatoire

                    # Vérifier si l'onduleur sélectionné a des plaques affectées
                    while len(liste_plq_onduleur[i]) == 0:
                            i = random.randint(0, len(liste_plq_onduleur) - 1)

                    j = random.randint(0, len(
                            liste_plq_onduleur[i]) - 1)  # Sélectionner une plaque aléatoire dans l'onduleur i

                    # Sélectionner un autre onduleur différent de i
                    k = random.randint(0, len(liste_plq_onduleur) - 1)
                    while k == i or len(liste_plq_onduleur[k]) == 0:
                            k = random.randint(0, len(liste_plq_onduleur) - 1)

                    # Échanger les deux plaques entre les onduleurs i et k
                    plaque_i = liste_plq_onduleur[i].pop(j)
                    plaque_k = random.choice(liste_plq_onduleur[k])
                    liste_plq_onduleur[k].remove(plaque_k)
                    liste_plq_onduleur[i].append(plaque_k)
                    liste_plq_onduleur[k].append(plaque_i)

                    return liste_plq_onduleur

            # Fonction pour calculer la température
            def temperature(init_temp, iteration):
                    return init_temp * math.exp(-0.01 * iteration)

            # Fonction pour évaluer la qualité d'une solution en utilisant la fonction fitness
            def evaluer(solution, co):
                    return fitness(solution, co)

            # Fonction principale pour l'algorithme du recuit simulé
            def recuit_simule(init_solution, co, init_temp, max_iter):
                    meilleure_solution = init_solution.copy()
                    meilleure_cout = evaluer(meilleure_solution, co)
                    solution_actuelle = init_solution.copy()
                    cout_actuel = evaluer(solution_actuelle, co)

                    for iteration in range(max_iter):
                            T = temperature(init_temp, iteration)

                            # Générer un voisin
                            voisin = generer_voisin(solution_actuelle)
                            cout_voisin = evaluer(voisin, co)

                            # Calculer la différence de coût entre le voisin et la solution actuelle
                            delta_cout = cout_voisin - cout_actuel

                            # Accepter le voisin avec une certaine probabilité
                            if delta_cout < 0 or random.uniform(0, 1) < math.exp(-delta_cout / T):
                                    solution_actuelle = voisin
                                    cout_actuel = cout_voisin

                            # Mettre à jour la meilleure solution trouvée
                            if cout_actuel < meilleure_cout:
                                    meilleure_solution = solution_actuelle.copy()
                                    meilleure_cout = cout_actuel

                    return meilleure_solution, meilleure_cout

            # Utilisation de l'algorithme du recuit simulé pour améliorer la solution
            solution_initiale = solution.copy()
            init_temp = 100.0
            max_iter = 1000

            meilleure_solution, meilleur_cout = recuit_simule(solution_initiale, co, init_temp, max_iter)

            # Afficher les résultats
            used_onduleur = count_used_onduleur(meilleure_solution)
            #for i, plaques in enumerate(meilleure_solution):
                    #print(f"Onduleur {i}: {plaques}, Utilisé: {used_onduleur[i]} fois")

            #print("Coût de la meilleure solution trouvée :", meilleur_cout)
            mil = "solution trouvée :"
            self.textEdit_5.setText(str(mil))
            datatest = "meilleure_solut.csv"
            header = ["meilleure_solution"]
            with open(datatest, "w", newline="") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(header)
                    for i, plaques in enumerate(meilleure_solution):
                            writer.writerow([f"Onduleur {i}: {plaques}, Utilisé: {used_onduleur[i]} fois"])


            pd.set_option('display.max_rows', None)
            pd.set_option('display.max_columns', None)

            dv = pd.read_csv("meilleure_solut.csv")
            self.textEdit.setText(str(dv.to_string(index=False)))

            mil = "Coût de la meilleure solution trouvée :"
            self.textEdit_4.setText(str(mil))
            self.textEdit_2.setText(str(meilleur_cout))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    progr = QtWidgets.QMainWindow()
    ui = Ui_progr()
    ui.setupUi(progr)
    progr.show()
    sys.exit(app.exec_())
