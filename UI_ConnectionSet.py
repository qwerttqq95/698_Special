# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_ConnectionSet.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(351, 402)
        Dialog.setLayoutDirection(QtCore.Qt.LeftToRight)
        Dialog.setAutoFillBackground(False)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(True)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 20, 291, 321))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_3 = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox_3.setTitle("通讯串口")
        self.groupBox_3.setObjectName("groupBox_3")
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 20, 271, 71))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget1)
        self.comboBox.setEditable(False)
        self.comboBox.setCurrentText("")
        self.comboBox.setModelColumn(0)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.comboBox_3 = QtWidgets.QComboBox(self.layoutWidget1)
        self.comboBox_3.setEditable(False)
        self.comboBox_3.setModelColumn(0)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox_3)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboBox_2 = QtWidgets.QComboBox(self.layoutWidget1)
        self.comboBox_2.setEditable(True)
        self.comboBox_2.setModelColumn(0)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.comboBox_4 = QtWidgets.QComboBox(self.layoutWidget1)
        self.comboBox_4.setEditable(True)
        self.comboBox_4.setModelColumn(0)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_4)
        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox_2 = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.layoutWidget_4 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget_4.setGeometry(QtCore.QRect(10, 20, 271, 71))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget_4)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_5.setEnabled(False)
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.comboBox_5 = QtWidgets.QComboBox(self.layoutWidget_4)
        self.comboBox_5.setEnabled(False)
        self.comboBox_5.setEditable(False)
        self.comboBox_5.setCurrentText("")
        self.comboBox_5.setModelColumn(0)
        self.comboBox_5.setObjectName("comboBox_5")
        self.horizontalLayout_5.addWidget(self.comboBox_5)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_6.setEnabled(False)
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.comboBox_6 = QtWidgets.QComboBox(self.layoutWidget_4)
        self.comboBox_6.setEnabled(False)
        self.comboBox_6.setEditable(False)
        self.comboBox_6.setModelColumn(0)
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.horizontalLayout_6.addWidget(self.comboBox_6)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 0, 1, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_7.setEnabled(False)
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.comboBox_7 = QtWidgets.QComboBox(self.layoutWidget_4)
        self.comboBox_7.setEnabled(False)
        self.comboBox_7.setEditable(True)
        self.comboBox_7.setModelColumn(0)
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.horizontalLayout_7.addWidget(self.comboBox_7)
        self.gridLayout_2.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_8.setEnabled(False)
        self.label_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.comboBox_8 = QtWidgets.QComboBox(self.layoutWidget_4)
        self.comboBox_8.setEnabled(False)
        self.comboBox_8.setEditable(True)
        self.comboBox_8.setModelColumn(0)
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.horizontalLayout_8.addWidget(self.comboBox_8)
        self.gridLayout_2.addLayout(self.horizontalLayout_8, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget2 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget2.setGeometry(QtCore.QRect(90, 40, 91, 22))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_10.addWidget(self.label_10)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit.setMaxLength(5)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit.setCursorPosition(4)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_10.addWidget(self.lineEdit)
        self.verticalLayout.addWidget(self.groupBox)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(60, 360, 239, 25))
        self.widget.setObjectName("widget")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.widget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_9.addWidget(self.buttonBox)
        self.label.setBuddy(self.comboBox)
        self.label_3.setBuddy(self.comboBox_3)
        self.label_2.setBuddy(self.comboBox_2)
        self.label_4.setBuddy(self.comboBox_4)
        self.label_5.setBuddy(self.comboBox_5)
        self.label_6.setBuddy(self.comboBox_6)
        self.label_7.setBuddy(self.comboBox_7)
        self.label_8.setBuddy(self.comboBox_8)
        self.label_10.setBuddy(self.lineEdit)

        self.retranslateUi(Dialog)
        self.comboBox.setCurrentIndex(-1)
        self.comboBox_3.setCurrentIndex(0)
        self.comboBox_2.setCurrentIndex(1)
        self.comboBox_4.setCurrentIndex(0)
        self.comboBox_5.setCurrentIndex(-1)
        self.comboBox_6.setCurrentIndex(1)
        self.comboBox_7.setCurrentIndex(0)
        self.comboBox_8.setCurrentIndex(0)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "通讯配置"))
        self.label.setText(_translate("Dialog", "串口号:"))
        self.label_3.setText(_translate("Dialog", "校验位:"))
        self.comboBox_3.setCurrentText(_translate("Dialog", "E"))
        self.comboBox_3.setItemText(0, _translate("Dialog", "E"))
        self.comboBox_3.setItemText(1, _translate("Dialog", "O"))
        self.label_2.setText(_translate("Dialog", "波特率:"))
        self.comboBox_2.setCurrentText(_translate("Dialog", "9600"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "2400"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "9600"))
        self.label_4.setText(_translate("Dialog", "停止位:"))
        self.comboBox_4.setCurrentText(_translate("Dialog", "1"))
        self.comboBox_4.setItemText(0, _translate("Dialog", "1"))
        self.comboBox_4.setItemText(1, _translate("Dialog", "1.5"))
        self.groupBox_2.setTitle(_translate("Dialog", "抄表串口"))
        self.label_5.setText(_translate("Dialog", "串口号:"))
        self.label_6.setText(_translate("Dialog", "校验位:"))
        self.comboBox_6.setCurrentText(_translate("Dialog", "偶"))
        self.comboBox_6.setItemText(0, _translate("Dialog", "奇"))
        self.comboBox_6.setItemText(1, _translate("Dialog", "偶"))
        self.label_7.setText(_translate("Dialog", "波特率:"))
        self.comboBox_7.setCurrentText(_translate("Dialog", "2400"))
        self.comboBox_7.setItemText(0, _translate("Dialog", "2400"))
        self.comboBox_7.setItemText(1, _translate("Dialog", "9600"))
        self.label_8.setText(_translate("Dialog", "停止位:"))
        self.comboBox_8.setCurrentText(_translate("Dialog", "1"))
        self.comboBox_8.setItemText(0, _translate("Dialog", "1"))
        self.comboBox_8.setItemText(1, _translate("Dialog", "1.5"))
        self.groupBox.setTitle(_translate("Dialog", "以太网"))
        self.label_10.setText(_translate("Dialog", "端口号:"))
        self.lineEdit.setText(_translate("Dialog", "8888"))

