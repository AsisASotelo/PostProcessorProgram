# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mrm_shopfloor.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets


def loadSpecs(file):
    try:
        mrm_specs_df = pd.read_excel(file, header=1)
        return mrm_specs_df
    except:
        print("Could not load file")


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        # Setup Main Window
        MainWindow.setObjectName("MRM SHOPFLOOR")
        MainWindow.resize(1189, 765)

        # Setup Central Widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # ~LEFT SECTION WHERE THE MACHINE INFORMATION IS ~

        # Place a frame inside of the Central Widget
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 301, 691))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        # Setup a GroupBox inside of the left frame
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(10, 120, 281, 161))
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 30, 261, 121))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        # Assign the label objects to the grid layout inside of the first groupbox
        self.mach_Num = QtWidgets.QLabel(self.gridLayoutWidget)
        self.mach_Num.setObjectName("mach_Num")
        self.gridLayout.addWidget(self.mach_Num, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 3, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 1, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 2, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 3, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 4, 1, 1, 1)

        # Second Grid Layout to hold the machine identification information.
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 290, 271, 241))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 30, 251, 204))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 2, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 4, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 1, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 3, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_18.setObjectName("label_18")
        self.gridLayout_2.addWidget(self.label_18, 1, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_19.setObjectName("label_19")
        self.gridLayout_2.addWidget(self.label_19, 2, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_20.setObjectName("label_20")
        self.gridLayout_2.addWidget(self.label_20, 3, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_21.setObjectName("label_21")
        self.gridLayout_2.addWidget(self.label_21, 4, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.frame)
        self.label_22.setGeometry(QtCore.QRect(90, 40, 125, 17))
        self.label_22.setText("")
        self.label_22.setObjectName("label_22")

        # Table widget to hold the available G-Codes on this machine.
        self.tableView = QtWidgets.QTableView(self.frame)
        self.tableView.setGeometry(QtCore.QRect(40, 550, 221, 121))
        self.tableView.setObjectName("tableView")

        # MRM Logo Definition
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(70, 20, 141, 91))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("MRM_IMAGE copy.jpeg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        # ~ SECTION FOR MACHINE SHOP LAYOUT ~

        # SETUP THE SECOND FRAME
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(320, 10, 861, 691))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        # SETUP for the tab widget to hold the seperate building locations.
        self.tabWidget = QtWidgets.QTabWidget(self.frame_2)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 841, 681))
        self.tabWidget.setObjectName("tabWidget")

        # TAB 1 -> BUILDING 1
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")

        self.machine224 = QtWidgets.QPushButton(self.tab1)
        self.machine224.setStyleSheet("background-color:blue")
        self.machine224.setGeometry(QtCore.QRect(40, 10, 71, 41))
        self.machine224.setObjectName("machine224")
        self.machine224.clicked.connect(self.setMachineNum)

        self.machine110 = QtWidgets.QPushButton(self.tab1)
        self.machine110.setGeometry(QtCore.QRect(0, 50, 51, 51))
        self.machine110.setObjectName("machine110")
        self.machine110.clicked.connect(self.setMachineNum)

        self.machine223 = QtWidgets.QPushButton(self.tab1)
        self.machine223.setGeometry(QtCore.QRect(60, 60, 61, 51))
        self.machine223.setObjectName("machine223")
        self.machine223.clicked.connect(self.setMachineNum)

        self.machine109 = QtWidgets.QPushButton(self.tab1)
        self.machine109.setGeometry(QtCore.QRect(10, 120, 101, 51))
        self.machine109.setObjectName("machine109")
        self.machine109.clicked.connect(self.setMachineNum)

        self.machine108 = QtWidgets.QPushButton(self.tab1)
        self.machine108.setGeometry(QtCore.QRect(10, 170, 101, 51))
        self.machine108.setObjectName("machine108")
        self.machine108.clicked.connect(self.setMachineNum)

        self.machine107 = QtWidgets.QPushButton(self.tab1)
        self.machine107.setGeometry(QtCore.QRect(10, 220, 101, 51))
        self.machine107.setObjectName("machine107")
        self.machine107.clicked.connect(self.setMachineNum)

        self.machine106 = QtWidgets.QPushButton(self.tab1)
        self.machine106.setGeometry(QtCore.QRect(10, 280, 51, 61))
        self.machine106.setObjectName("machine106")
        self.machine106.clicked.connect(self.setMachineNum)

        self.machine105 = QtWidgets.QPushButton(self.tab1)
        self.machine105.setGeometry(QtCore.QRect(70, 280, 51, 61))
        self.machine105.setObjectName("machine105")
        self.machine105.clicked.connect(self.setMachineNum)

        self.machine104 = QtWidgets.QPushButton(self.tab1)
        self.machine104.setGeometry(QtCore.QRect(20, 350, 101, 51))
        self.machine104.setObjectName("machine104")
        self.machine104.clicked.connect(self.setMachineNum)

        self.machine102 = QtWidgets.QPushButton(self.tab1)
        self.machine102.setGeometry(QtCore.QRect(10, 410, 61, 61))
        self.machine102.setObjectName("machine102")
        self.machine102.clicked.connect(self.setMachineNum)

        self.machine103 = QtWidgets.QPushButton(self.tab1)
        self.machine103.setGeometry(QtCore.QRect(80, 410, 61, 61))
        self.machine103.setObjectName("machine103")
        self.machine103.clicked.connect(self.setMachineNum)

        self.machine101 = QtWidgets.QPushButton(self.tab1)
        self.machine101.setGeometry(QtCore.QRect(30, 480, 91, 61))
        self.machine101.setObjectName("machine101")
        self.machine101.clicked.connect(self.setMachineNum)

        self.machine232 = QtWidgets.QPushButton(self.tab1)
        self.machine232.setGeometry(QtCore.QRect(10, 560, 151, 91))
        self.machine232.setObjectName("machine232")
        self.machine232.clicked.connect(self.setMachineNum)

        self.machine112 = QtWidgets.QPushButton(self.tab1)
        self.machine112.setGeometry(QtCore.QRect(200, 10, 91, 51))
        self.machine112.setObjectName("machine112")
        self.machine112.clicked.connect(self.setMachineNum)

        self.machine226 = QtWidgets.QPushButton(self.tab1)
        self.machine226.setGeometry(QtCore.QRect(300, 10, 91, 51))
        self.machine226.setObjectName("machine226")
        self.machine226.clicked.connect(self.setMachineNum)

        self.machine227 = QtWidgets.QPushButton(self.tab1)
        self.machine227.setGeometry(QtCore.QRect(400, 10, 91, 51))
        self.machine227.setObjectName("machine227")
        self.machine227.clicked.connect(self.setMachineNum)

        self.machine228 = QtWidgets.QPushButton(self.tab1)
        self.machine228.setGeometry(QtCore.QRect(500, 10, 91, 51))
        self.machine228.setObjectName("machine228")
        self.machine228.clicked.connect(self.setMachineNum)

        self.machine229 = QtWidgets.QPushButton(self.tab1)
        self.machine229.setGeometry(QtCore.QRect(720, 40, 91, 101))
        self.machine229.setObjectName("machine229")
        self.machine229.clicked.connect(self.setMachineNum)

        self.machine230 = QtWidgets.QPushButton(self.tab1)
        self.machine230.setGeometry(QtCore.QRect(720, 170, 91, 101))
        self.machine230.setObjectName("machine230")
        self.machine230.clicked.connect(self.setMachineNum)

        self.machine231 = QtWidgets.QPushButton(self.tab1)
        self.machine231.setGeometry(QtCore.QRect(720, 290, 91, 101))
        self.machine231.setObjectName("machine231")
        self.machine231.clicked.connect(self.setMachineNum)

        self.machine211 = QtWidgets.QPushButton(self.tab1)
        self.machine211.setGeometry(QtCore.QRect(230, 110, 191, 71))
        self.machine211.setObjectName("machine211")
        self.machine211.clicked.connect(self.setMachineNum)

        self.machine212 = QtWidgets.QPushButton(self.tab1)
        self.machine212.setGeometry(QtCore.QRect(240, 190, 71, 71))
        self.machine212.setObjectName("machine212")
        self.machine212.clicked.connect(self.setMachineNum)

        self.machine213 = QtWidgets.QPushButton(self.tab1)
        self.machine213.setGeometry(QtCore.QRect(240, 260, 71, 71))
        self.machine213.setObjectName("machine213")
        self.machine213.clicked.connect(self.setMachineNum)

        self.machine214 = QtWidgets.QPushButton(self.tab1)
        self.machine214.setGeometry(QtCore.QRect(240, 340, 71, 71))
        self.machine214.setObjectName("machine214")
        self.machine214.clicked.connect(self.setMachineNum)

        self.machine219 = QtWidgets.QPushButton(self.tab1)
        self.machine219.setGeometry(QtCore.QRect(340, 210, 71, 71))
        self.machine219.setObjectName("machine219")
        self.machine219.clicked.connect(self.setMachineNum)

        self.machine218 = QtWidgets.QPushButton(self.tab1)
        self.machine218.setGeometry(QtCore.QRect(340, 300, 71, 71))
        self.machine218.setObjectName("machine218")
        self.machine218.clicked.connect(self.setMachineNum)

        self.machine225 = QtWidgets.QPushButton(self.tab1)
        self.machine225.setGeometry(QtCore.QRect(460, 110, 111, 71))
        self.machine225.setObjectName("machine225")
        self.machine225.clicked.connect(self.setMachineNum)

        self.machine233 = QtWidgets.QPushButton(self.tab1)
        self.machine233.setGeometry(QtCore.QRect(540, 200, 113, 211))
        self.machine233.setObjectName("machine233")
        self.machine233.clicked.connect(self.setMachineNum)

        self.machine220 = QtWidgets.QPushButton(self.tab1)
        self.machine220.setGeometry(QtCore.QRect(460, 190, 81, 61))
        self.machine220.setObjectName("machine220")
        self.machine220.clicked.connect(self.setMachineNum)

        self.machine221 = QtWidgets.QPushButton(self.tab1)
        self.machine221.setGeometry(QtCore.QRect(470, 310, 71, 101))
        self.machine221.setObjectName("machine221")
        self.machine221.clicked.connect(self.setMachineNum)

        self.machine215 = QtWidgets.QPushButton(self.tab1)
        self.machine215.setGeometry(QtCore.QRect(240, 440, 81, 121))
        self.machine215.setObjectName("machine215")
        self.machine215.clicked.connect(self.setMachineNum)

        self.machine217 = QtWidgets.QPushButton(self.tab1)
        self.machine217.setGeometry(QtCore.QRect(320, 440, 61, 61))
        self.machine217.setObjectName("machine217")
        self.machine217.clicked.connect(self.setMachineNum)

        self.machine216 = QtWidgets.QPushButton(self.tab1)
        self.machine216.setGeometry(QtCore.QRect(320, 500, 61, 61))
        self.machine216.setObjectName("machine216")
        self.machine216.clicked.connect(self.setMachineNum)

        self.machine222 = QtWidgets.QPushButton(self.tab1)
        self.machine222.setGeometry(QtCore.QRect(420, 440, 71, 101))
        self.machine222.setObjectName("machine222")
        self.machine222.clicked.connect(self.setMachineNum)

        self.tabWidget.addTab(self.tab1, "")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")

        self.machine333 = QtWidgets.QPushButton(self.tab2)
        self.machine333.setGeometry(QtCore.QRect(270, 20, 161, 241))
        self.machine333.setObjectName("machine333")
        self.machine333.clicked.connect(self.setMachineNum)

        self.machine332 = QtWidgets.QPushButton(self.tab2)
        self.machine332.setGeometry(QtCore.QRect(60, 10, 71, 101))
        self.machine332.setToolTipDuration(100000)
        self.machine332.setObjectName("machine332")
        self.machine332.clicked.connect(self.setMachineNum)

        self.machine331 = QtWidgets.QPushButton(self.tab2)
        self.machine331.setGeometry(QtCore.QRect(50, 130, 101, 141))
        self.machine331.setObjectName("machine331")
        self.machine331.clicked.connect(self.setMachineNum)

        self.machine330 = QtWidgets.QPushButton(self.tab2)
        self.machine330.setGeometry(QtCore.QRect(50, 290, 121, 151))
        self.machine330.setObjectName("machine330")
        self.machine330.clicked.connect(self.setMachineNum)

        self.machine334 = QtWidgets.QPushButton(self.tab2)
        self.machine334.setGeometry(QtCore.QRect(320, 260, 101, 71))
        self.machine334.setObjectName("machine334")
        self.machine334.clicked.connect(self.setMachineNum)

        self.machine335 = QtWidgets.QPushButton(self.tab2)
        self.machine335.setGeometry(QtCore.QRect(320, 340, 101, 71))
        self.machine335.setObjectName("machine335")
        self.machine335.clicked.connect(self.setMachineNum)

        self.machine338 = QtWidgets.QPushButton(self.tab2)
        self.machine338.setGeometry(QtCore.QRect(440, 190, 171, 281))
        self.machine338.setObjectName("machine338")
        self.machine338.clicked.connect(self.setMachineNum)

        self.machine336 = QtWidgets.QPushButton(self.tab2)
        self.machine336.setGeometry(QtCore.QRect(240, 420, 171, 111))
        self.machine336.setObjectName("machine336")
        self.machine336.clicked.connect(self.setMachineNum)

        self.machine337 = QtWidgets.QPushButton(self.tab2)
        self.machine337.setGeometry(QtCore.QRect(690, 440, 131, 201))
        self.machine337.setObjectName("machine337")
        self.machine337.clicked.connect(self.setMachineNum)

        self.machine340 = QtWidgets.QPushButton(self.tab2)
        self.machine340.setGeometry(QtCore.QRect(680, 200, 141, 151))
        self.machine340.setObjectName("machine340")
        self.machine340.clicked.connect(self.setMachineNum)

        self.machine341 = QtWidgets.QPushButton(self.tab2)
        self.machine341.setGeometry(QtCore.QRect(690, 90, 101, 71))
        self.machine341.setObjectName("machine341")
        self.machine341.clicked.connect(self.setMachineNum)

        self.machine339 = QtWidgets.QPushButton(self.tab2)
        self.machine339.setGeometry(QtCore.QRect(460, 100, 101, 71))
        self.machine339.setObjectName("machine339")
        self.machine339.clicked.connect(self.setMachineNum)

        self.tabWidget.addTab(self.tab2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1189, 24))
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MRM SHOP FLOOR"))
        self.groupBox.setTitle(_translate("MainWindow", "IDENTIFICATION"))
        self.mach_Num.setText(_translate("MainWindow", ""))
        self.label_6.setText(_translate("MainWindow", "Zone"))
        self.label_2.setText(_translate("MainWindow", "Model"))
        self.label_4.setText(_translate("MainWindow", "Machine #"))
        self.label_3.setText(_translate("MainWindow", "Manufacturer"))
        self.label_10.setText(_translate("MainWindow", "Serial #"))
        self.label_14.setText(_translate("MainWindow", ""))
        self.label_15.setText(_translate("MainWindow", ""))
        self.label_16.setText(_translate("MainWindow", ""))
        self.label_17.setText(_translate("MainWindow", ""))
        self.groupBox_2.setTitle(_translate(
            "MainWindow", "Machine Specification"))
        self.label_8.setText(_translate("MainWindow", "Available Axis"))
        self.label_7.setText(_translate("MainWindow", ""))
        self.label_11.setText(_translate("MainWindow", "Rotary Travel"))
        self.label_13.setText(_translate("MainWindow", ""))
        self.label_9.setText(_translate("MainWindow", "XxYxZ Travel"))
        self.label_12.setText(_translate("MainWindow", "Controller"))
        self.label_18.setText(_translate("MainWindow", ""))
        self.label_19.setText(_translate("MainWindow", ""))
        self.label_20.setText(_translate("MainWindow", ""))
        self.label_21.setText(_translate("MainWindow", ""))
        self.machine224.setText(_translate("MainWindow", "224"))
        self.machine110.setText(_translate("MainWindow", "110"))
        self.machine223.setText(_translate("MainWindow", "223"))
        self.machine109.setText(_translate("MainWindow", "109"))
        self.machine108.setText(_translate("MainWindow", "108"))
        self.machine107.setText(_translate("MainWindow", "107"))
        self.machine106.setText(_translate("MainWindow", "106"))
        self.machine105.setText(_translate("MainWindow", "105"))
        self.machine104.setText(_translate("MainWindow", "104"))
        self.machine102.setText(_translate("MainWindow", "102"))
        self.machine103.setText(_translate("MainWindow", "103"))
        self.machine101.setText(_translate("MainWindow", "101"))
        self.machine232.setText(_translate("MainWindow", "232"))
        self.machine112.setText(_translate("MainWindow", "112"))
        self.machine226.setText(_translate("MainWindow", "226"))
        self.machine227.setText(_translate("MainWindow", "227"))
        self.machine228.setText(_translate("MainWindow", "228"))
        self.machine229.setText(_translate("MainWindow", "229"))
        self.machine230.setText(_translate("MainWindow", "230"))
        self.machine231.setText(_translate("MainWindow", "231"))
        self.machine211.setText(_translate("MainWindow", "211"))
        self.machine212.setText(_translate("MainWindow", "212"))
        self.machine213.setText(_translate("MainWindow", "213"))
        self.machine214.setText(_translate("MainWindow", "214"))
        self.machine219.setText(_translate("MainWindow", "219"))
        self.machine218.setText(_translate("MainWindow", "218"))
        self.machine225.setText(_translate("MainWindow", "225"))
        self.machine233.setText(_translate("MainWindow", "233"))
        self.machine220.setText(_translate("MainWindow", "220"))
        self.machine221.setText(_translate("MainWindow", "221"))
        self.machine215.setText(_translate("MainWindow", "215"))
        self.machine217.setText(_translate("MainWindow", "217"))
        self.machine216.setText(_translate("MainWindow", "216"))
        self.machine222.setText(_translate("MainWindow", "222"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab1), _translate("MainWindow", "Building 1"))
        self.machine333.setText(_translate("MainWindow", "333"))
        self.machine332.setToolTip(_translate("MainWindow", "there"))
        self.machine332.setStatusTip(_translate("MainWindow", "hello"))
        self.machine332.setText(_translate("MainWindow", "332"))
        self.machine331.setText(_translate("MainWindow", "331"))
        self.machine330.setText(_translate("MainWindow", "330"))
        self.machine334.setText(_translate("MainWindow", "334"))
        self.machine335.setText(_translate("MainWindow", "335"))
        self.machine338.setText(_translate("MainWindow", "338"))
        self.machine336.setText(_translate("MainWindow", "336"))
        self.machine337.setText(_translate("MainWindow", "337"))
        self.machine340.setText(_translate("MainWindow", "340"))
        self.machine341.setText(_translate("MainWindow", "341"))
        self.machine339.setText(_translate("MainWindow", "339"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab2), _translate("MainWindow", "Building 2"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))

    # Function for the Machine Number label defintion
    def setMachineNum(self):
        '''
        If button inside of machine layout is pressed, machineNum level is set 
        to corresponding machine number.
        '''
        sender = self.tab1.sender()
        self.mach_Num.setText(sender.text())

        machine_specs = machine_specs_df.loc[machine_specs_df['MachineNumber'] == float(
            sender.text())]
        self.label_14.setText(machine_specs['Model'].item())
        self.label_15.setText(machine_specs['Manufacturer'].item())
        self.label_16.setText(str(machine_specs['ID #'].item()))
        self.label_7.setText(str(machine_specs['Axis'].item()))
        self.label_18.setText(str(machine_specs['Travel(XxYxZ)'].item()))
        self.label_17.setText(str(int(machine_specs['Zone'].item())))
        self.label_20.setText(str(machine_specs['CNC Controls'].item()))
        self.label_19.setText(str(machine_specs['Rotary Travel'].item()))


if __name__ == "__main__":
    import sys

    machine_specs_df = loadSpecs("WORK_CENTERS_UPDATE.xlsx")
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
