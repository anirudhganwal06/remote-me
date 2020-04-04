import struct
import pickle
import socket
import mss
import numpy as np
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from controller import startController
from user import startUser

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setGeometry(100, 100, 800, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.smsBtn_2 = QtWidgets.QPushButton(self.page)
        self.smsBtn_2.setMinimumSize(QtCore.QSize(400, 50))
        self.smsBtn_2.setObjectName("smsBtn_2")
        self.smsBtn_2.clicked.connect(self.goToUserScreen)
        self.verticalLayout_4.addWidget(self.smsBtn_2)
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.wosBtn_2 = QtWidgets.QPushButton(self.page)
        self.wosBtn_2.setMinimumSize(QtCore.QSize(400, 50))
        self.wosBtn_2.setObjectName("wosBtn_2")
        self.wosBtn_2.clicked.connect(self.goToControllerScreen)
        self.verticalLayout_4.addWidget(self.wosBtn_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem4, 2, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout_4.addWidget(self.stackedWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.smsBtn_2.setText(_translate("MainWindow", "SHARE MY SCREEN"))
        self.wosBtn_2.setText(_translate(
            "MainWindow", "WATCH OTHER\'S SCREEN"))
        self.label.setText(_translate("MainWindow", "Second page"))

    def goToUserScreen(self):
        self.stackedWidget.setCurrentIndex(1)
        print(self.stackedWidget.currentIndex())
        print("index set")
        startUser()

    def goToControllerScreen(self):
        print(args)
        self.stackedWidget.setCurrentIndex(2)
        # startController()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
