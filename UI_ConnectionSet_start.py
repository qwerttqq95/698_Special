from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
import sys, UI_ConnectionSet
import serial
import serial.tools.list_ports


def GetSerialNumber():
    SerialNumber = []
    port_list = list(serial.tools.list_ports.comports())
    if len(port_list) <= 0:
        print("The Serial port can't find!")

    else:
        for i in list(port_list):
            print(i[0])
            SerialNumber.append(i[0])
        return SerialNumber


class UI_ConnectionSet_Main(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = UI_ConnectionSet.Ui_Dialog()
        self.ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        addItem = GetSerialNumber()
        addItem.sort()
        for self.addItem in addItem:
            self.ui.comboBox.addItem(self.addItem)
            self.ui.comboBox_5.addItem(self.addItem)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    UI_ConnectionSet_Main = UI_ConnectionSet_Main()
    UI_ConnectionSet_Main.show()
    sys.exit(app.exec_())
