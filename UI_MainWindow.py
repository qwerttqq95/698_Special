# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(670, 509)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_2.sizePolicy().hasHeightForWidth())
        self.textEdit_2.setSizePolicy(sizePolicy)
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setOverwriteMode(False)
        self.textEdit_2.setCursorWidth(1)
        self.textEdit_2.setObjectName("textEdit_2")
        self.horizontalLayout.addWidget(self.textEdit_2)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.textEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 670, 23))
        self.menubar.setObjectName("menubar")
        self.menuOpen = QtWidgets.QMenu(self.menubar)
        self.menuOpen.setObjectName("menuOpen")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_8 = QtWidgets.QMenu(self.menu_2)
        self.menu_8.setObjectName("menu_8")
        self.menu_6 = QtWidgets.QMenu(self.menu_2)
        self.menu_6.setObjectName("menu_6")
        self.menu_7 = QtWidgets.QMenu(self.menu_6)
        self.menu_7.setObjectName("menu_7")
        self.menu_3 = QtWidgets.QMenu(self.menu_6)
        self.menu_3.setObjectName("menu_3")
        self.menu_9 = QtWidgets.QMenu(self.menu_2)
        self.menu_9.setObjectName("menu_9")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        self.menu_5 = QtWidgets.QMenu(self.menubar)
        self.menu_5.setObjectName("menu_5")
        self.menu_10 = QtWidgets.QMenu(self.menubar)
        self.menu_10.setObjectName("menu_10")
        self.menu_11 = QtWidgets.QMenu(self.menu_10)
        self.menu_11.setObjectName("menu_11")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setIconText("Exit")
        self.action.setObjectName("action")
        self.actionSd = QtWidgets.QAction(MainWindow)
        self.actionSd.setIconText("通讯配置")
        self.actionSd.setIconVisibleInMenu(False)
        self.actionSd.setObjectName("actionSd")
        self.actionA = QtWidgets.QAction(MainWindow)
        self.actionA.setObjectName("actionA")
        self.actionX = QtWidgets.QAction(MainWindow)
        self.actionX.setObjectName("actionX")
        self.actionSdf = QtWidgets.QAction(MainWindow)
        self.actionSdf.setObjectName("actionSdf")
        self.actionC = QtWidgets.QAction(MainWindow)
        self.actionC.setEnabled(False)
        self.actionC.setObjectName("actionC")
        self.actionG = QtWidgets.QAction(MainWindow)
        self.actionG.setObjectName("actionG")
        self.actionMore = QtWidgets.QAction(MainWindow)
        self.actionMore.setObjectName("actionMore")
        self.action0200 = QtWidgets.QAction(MainWindow)
        self.action0200.setObjectName("action0200")
        self.action0200_2 = QtWidgets.QAction(MainWindow)
        self.action0200_2.setObjectName("action0200_2")
        self.action0201 = QtWidgets.QAction(MainWindow)
        self.action0201.setObjectName("action0201")
        self.action0200_3 = QtWidgets.QAction(MainWindow)
        self.action0200_3.setObjectName("action0200_3")
        self.action0201_2 = QtWidgets.QAction(MainWindow)
        self.action0201_2.setObjectName("action0201_2")
        self.actionSh = QtWidgets.QAction(MainWindow)
        self.actionSh.setObjectName("actionSh")
        self.actionRi = QtWidgets.QAction(MainWindow)
        self.actionRi.setObjectName("actionRi")
        self.actionQu = QtWidgets.QAction(MainWindow)
        self.actionQu.setObjectName("actionQu")
        self.actionRi_2 = QtWidgets.QAction(MainWindow)
        self.actionRi_2.setObjectName("actionRi_2")
        self.action0020l = QtWidgets.QAction(MainWindow)
        self.action0020l.setObjectName("action0020l")
        self.action0201l = QtWidgets.QAction(MainWindow)
        self.action0201l.setObjectName("action0201l")
        self.actionS = QtWidgets.QAction(MainWindow)
        self.actionS.setObjectName("actionS")
        self.action_a = QtWidgets.QAction(MainWindow)
        self.action_a.setObjectName("action_a")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")
        self.action_6 = QtWidgets.QAction(MainWindow)
        self.action_6.setObjectName("action_6")
        self.action_7 = QtWidgets.QAction(MainWindow)
        self.action_7.setObjectName("action_7")
        self.action_8 = QtWidgets.QAction(MainWindow)
        self.action_8.setObjectName("action_8")
        self.action_9 = QtWidgets.QAction(MainWindow)
        self.action_9.setObjectName("action_9")
        self.action_10 = QtWidgets.QAction(MainWindow)
        self.action_10.setObjectName("action_10")
        self.action_11 = QtWidgets.QAction(MainWindow)
        self.action_11.setObjectName("action_11")
        self.action_12 = QtWidgets.QAction(MainWindow)
        self.action_12.setObjectName("action_12")
        self.action_13 = QtWidgets.QAction(MainWindow)
        self.action_13.setObjectName("action_13")
        self.action_14 = QtWidgets.QAction(MainWindow)
        self.action_14.setObjectName("action_14")
        self.action_15 = QtWidgets.QAction(MainWindow)
        self.action_15.setObjectName("action_15")
        self.action_16 = QtWidgets.QAction(MainWindow)
        self.action_16.setObjectName("action_16")
        self.action_17 = QtWidgets.QAction(MainWindow)
        self.action_17.setObjectName("action_17")
        self.action_18 = QtWidgets.QAction(MainWindow)
        self.action_18.setObjectName("action_18")
        self.actionZ = QtWidgets.QAction(MainWindow)
        self.actionZ.setObjectName("actionZ")
        self.actionD = QtWidgets.QAction(MainWindow)
        self.actionD.setObjectName("actionD")
        self.actionShuju = QtWidgets.QAction(MainWindow)
        self.actionShuju.setObjectName("actionShuju")
        self.actionCanshu = QtWidgets.QAction(MainWindow)
        self.actionCanshu.setObjectName("actionCanshu")
        self.actionDf = QtWidgets.QAction(MainWindow)
        self.actionDf.setEnabled(False)
        self.actionDf.setObjectName("actionDf")
        self.action_dongjie = QtWidgets.QAction(MainWindow)
        self.action_dongjie.setObjectName("action_dongjie")
        self.actionX_2 = QtWidgets.QAction(MainWindow)
        self.actionX_2.setObjectName("actionX_2")
        self.action_20 = QtWidgets.QAction(MainWindow)
        self.action_20.setObjectName("action_20")
        self.action_19 = QtWidgets.QAction(MainWindow)
        self.action_19.setObjectName("action_19")
        self.action_21 = QtWidgets.QAction(MainWindow)
        self.action_21.setObjectName("action_21")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_22 = QtWidgets.QAction(MainWindow)
        self.action_22.setObjectName("action_22")
        self.actionAPDUzu = QtWidgets.QAction(MainWindow)
        self.actionAPDUzu.setObjectName("actionAPDUzu")
        self.action_23 = QtWidgets.QAction(MainWindow)
        self.action_23.setObjectName("action_23")
        self.menuOpen.addAction(self.actionSd)
        self.menuOpen.addAction(self.action)
        self.menu.addAction(self.actionA)
        self.menu_8.addAction(self.actionSh)
        self.menu_8.addAction(self.actionRi)
        self.menu_8.addAction(self.actionQu)
        self.menu_7.addAction(self.action0200_3)
        self.menu_7.addAction(self.action0201_2)
        self.menu_3.addAction(self.action0020l)
        self.menu_3.addAction(self.action0201l)
        self.menu_6.addAction(self.menu_7.menuAction())
        self.menu_6.addAction(self.actionRi_2)
        self.menu_6.addAction(self.menu_3.menuAction())
        self.menu_9.addAction(self.action_19)
        self.menu_9.addAction(self.action_21)
        self.menu_9.addSeparator()
        self.menu_9.addAction(self.actionX_2)
        self.menu_2.addAction(self.menu_8.menuAction())
        self.menu_2.addAction(self.menu_6.menuAction())
        self.menu_2.addAction(self.menu_9.menuAction())
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.actionG)
        self.menu_2.addAction(self.actionSdf)
        self.menu_4.addAction(self.actionC)
        self.menu_4.addAction(self.actionDf)
        self.menu_4.addAction(self.actionAPDUzu)
        self.menu_5.addAction(self.actionShuju)
        self.menu_5.addAction(self.actionCanshu)
        self.menu_11.addAction(self.action_15)
        self.menu_11.addAction(self.action_16)
        self.menu_11.addAction(self.action_23)
        self.menu_11.addAction(self.actionZ)
        self.menu_10.addAction(self.menu_11.menuAction())
        self.menu_10.addAction(self.actionS)
        self.menu_10.addAction(self.action_a)
        self.menu_10.addAction(self.action_22)
        self.menu_10.addAction(self.action_2)
        self.menu_10.addAction(self.action_3)
        self.menu_10.addAction(self.action_4)
        self.menu_10.addAction(self.action_5)
        self.menu_10.addAction(self.action_6)
        self.menu_10.addAction(self.action_7)
        self.menu_10.addAction(self.action_8)
        self.menu_10.addAction(self.action_9)
        self.menu_10.addAction(self.action_10)
        self.menu_10.addAction(self.action_11)
        self.menu_10.addAction(self.action_12)
        self.menu_10.addAction(self.action_13)
        self.menu_10.addAction(self.action_14)
        self.menu_10.addAction(self.action_17)
        self.menu_10.addAction(self.action_18)
        self.menubar.addAction(self.menuOpen.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu_10.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.action.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "698 Special"))
        self.menuOpen.setTitle(_translate("MainWindow", "文件"))
        self.menu.setTitle(_translate("MainWindow", "帮助"))
        self.menu_2.setTitle(_translate("MainWindow", "测试"))
        self.menu_8.setTitle(_translate("MainWindow", "默认测试方案"))
        self.menu_6.setTitle(_translate("MainWindow", "浙江支持数据"))
        self.menu_7.setTitle(_translate("MainWindow", "实时数据"))
        self.menu_3.setTitle(_translate("MainWindow", "冻结曲线数据"))
        self.menu_9.setTitle(_translate("MainWindow", "数据读取"))
        self.menu_4.setTitle(_translate("MainWindow", "工具"))
        self.menu_5.setTitle(_translate("MainWindow", "复位"))
        self.menu_10.setTitle(_translate("MainWindow", "控制"))
        self.menu_11.setTitle(_translate("MainWindow", "遥控"))
        self.action.setText(_translate("MainWindow", "Exit"))
        self.actionSd.setText(_translate("MainWindow", "通讯配置"))
        self.actionA.setText(_translate("MainWindow", "关于"))
        self.actionX.setText(_translate("MainWindow", "自定义参数配置"))
        self.actionSdf.setText(_translate("MainWindow", "以太网快速配置(串口)"))
        self.actionC.setText(_translate("MainWindow", "报文解析"))
        self.actionG.setText(_translate("MainWindow", "广播读地址"))
        self.actionMore.setText(_translate("MainWindow", "默认方案"))
        self.action0200.setText(_translate("MainWindow", "0200"))
        self.action0200_2.setText(_translate("MainWindow", "0200类"))
        self.action0201.setText(_translate("MainWindow", "0201类"))
        self.action0200_3.setText(_translate("MainWindow", "0200类"))
        self.action0201_2.setText(_translate("MainWindow", "0201类"))
        self.actionSh.setText(_translate("MainWindow", "实时数据(多项)"))
        self.actionRi.setText(_translate("MainWindow", "日冻结数据"))
        self.actionQu.setText(_translate("MainWindow", "冻结曲线数据"))
        self.actionRi_2.setText(_translate("MainWindow", "日冻结数据"))
        self.action0020l.setText(_translate("MainWindow", "0200类"))
        self.action0201l.setText(_translate("MainWindow", "0201类"))
        self.actionS.setText(_translate("MainWindow", "时段功控投入"))
        self.action_a.setText(_translate("MainWindow", "时段功控解除"))
        self.action_3.setText(_translate("MainWindow", "厂休功控投入"))
        self.action_4.setText(_translate("MainWindow", "厂休功控解除"))
        self.action_5.setText(_translate("MainWindow", "营业报停功控投入"))
        self.action_6.setText(_translate("MainWindow", "营业报停功控解除"))
        self.action_7.setText(_translate("MainWindow", "月电控投入"))
        self.action_8.setText(_translate("MainWindow", "月电控解除"))
        self.action_9.setText(_translate("MainWindow", "购电控投入"))
        self.action_10.setText(_translate("MainWindow", "购电控解除"))
        self.action_11.setText(_translate("MainWindow", "催费告警投入"))
        self.action_12.setText(_translate("MainWindow", "催费告警解除"))
        self.action_13.setText(_translate("MainWindow", "保电投入"))
        self.action_14.setText(_translate("MainWindow", "保电解除"))
        self.action_15.setText(_translate("MainWindow", "单地址跳闸(第1轮)"))
        self.action_15.setToolTip(_translate("MainWindow", "单地址跳闸"))
        self.action_16.setText(_translate("MainWindow", "单地址合闸(第1轮)"))
        self.action_17.setText(_translate("MainWindow", "剔除投入"))
        self.action_18.setText(_translate("MainWindow", "剔除解除"))
        self.actionZ.setText(_translate("MainWindow", "组地址跳闸(第2轮)"))
        self.actionD.setText(_translate("MainWindow", "组地址合闸"))
        self.actionShuju.setText(_translate("MainWindow", "数据初始化"))
        self.actionCanshu.setText(_translate("MainWindow", "参数初始化"))
        self.actionDf.setText(_translate("MainWindow", "字符转换"))
        self.action_dongjie.setText(_translate("MainWindow", "自定义冻结数据"))
        self.actionX_2.setText(_translate("MainWindow", "自定义数据读取"))
        self.action_20.setText(_translate("MainWindow", "曲线数据"))
        self.action_19.setText(_translate("MainWindow", "默认实时数据"))
        self.action_21.setText(_translate("MainWindow", "默认日冻结数据"))
        self.action_2.setText(_translate("MainWindow", "当前功率下浮控解除"))
        self.action_22.setText(_translate("MainWindow", "当前功率下浮控投入"))
        self.actionAPDUzu.setText(_translate("MainWindow", "自定义报文发送"))
        self.action_23.setText(_translate("MainWindow", "单地址合闸(第2轮)"))

