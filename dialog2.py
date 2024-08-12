# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog2.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

class Ui_dialoginscr(object):
    def setupUi(self, dialoginscr):
        dialoginscr.setObjectName("dialoginscr")
        dialoginscr.resize(821, 236)
        self.centralwidget = QtWidgets.QWidget(dialoginscr)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 60, 411, 51))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(670, 160, 89, 25))
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
        self.pushButton.clicked.connect(self.connect)
        dialoginscr.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(dialoginscr)
        self.statusbar.setObjectName("statusbar")
        dialoginscr.setStatusBar(self.statusbar)

        self.retranslateUi(dialoginscr)
        QtCore.QMetaObject.connectSlotsByName(dialoginscr)



    def connect(self):
        from projett import Ui_MainWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()




    def retranslateUi(self, dialoginscr):
        _translate = QtCore.QCoreApplication.translate
        dialoginscr.setWindowTitle(_translate("dialoginscr", "OK"))
        self.label.setText(_translate("dialoginscr", "Vous etes maintenant inscrit connect toi !"))
        self.pushButton.setText(_translate("dialoginscr", "OK"))


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    dialoginscr = QtWidgets.QMainWindow()
    ui = Ui_dialoginscr()
    ui.setupUi(dialoginscr)
    dialoginscr.show()
    sys.exit(app.exec_())
