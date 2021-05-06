# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainKQlkEg.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2 import QtWidgets
from PySide2 import QtCore
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from features import boost

import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        MainWindow.resize(342, 160)
        MainWindow.setStyleSheet(u"background-color: rgb(44, 49, 60);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.topBar = QFrame(self.centralwidget)
        self.topBar.setObjectName(u"topBar")
        self.topBar.setGeometry(QRect(0, 0, 351, 31))
        self.topBar.setStyleSheet(u"background-color: rgb(37, 41, 50);")
        self.topBar.setFrameShape(QFrame.StyledPanel)
        self.topBar.setFrameShadow(QFrame.Raised)
        self.closeBtn = QPushButton(self.topBar)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setGeometry(QRect(310, 9, 16, 16))
        self.closeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeBtn.setStyleSheet(u"QPushButton {\n"
"	image: url(:/16/cil-x.png);\n"
"	border-radius: 8px;\n"
"	border: no-border;\n"
"}\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(255, 53, 39);\n"
"}")
        self.footer = QFrame(self.centralwidget)
        self.footer.setObjectName(u"footer")
        self.footer.setGeometry(QRect(0, 140, 341, 20))
        self.footer.setStyleSheet(u"background-color: rgb(37, 41, 50);")
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.footer)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, -2, 81, 21))
        self.label.setStyleSheet(u"QLabel {\n"
"\n"
"color: rgb(0, 120, 120);\n"
"background-color: rgb(37, 41, 50);\n"
"}\n"
"QLabel:hover {\n"
"	\n"
"	color: rgb(0, 255, 255);\n"
"}")
        self.label.setAlignment(Qt.AlignCenter)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(80, 50, 181, 61))
        self.pushButton.setStyleSheet(u"image-position: right;\n"
"color: rgb(0, 255, 255);\n"
"background-color: rgb(37, 41, 50);\n"
"border-radius: 8px;\n"
"font: 87 10pt \"Arial Black\";")
        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton.clicked.connect(lambda: boost.Boost())
        self.closeBtn.clicked.connect(lambda: MainWindow.close())
        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.closeBtn.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"@thefakeflowd", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"BOOST", None))
    # retranslateUi

if __name__ in "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
