import UI_Check, UI_MessageCompose, os, threading, Main
from PyQt5.QtWidgets import QDialog, QHeaderView, QMessageBox, QTableWidgetItem,QTableWidget
from PyQt5.QtCore import pyqtSignal,Qt
from PyQt5.QtGui import QIcon


class check(QDialog,QTableWidget):  # 自定义测试方案

    def __init__(self, q):
        self.q = q
        QDialog.__init__(self)
        QTableWidget.__init__(self)
        self.ui = UI_Check.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.op)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.ui.pushButton_3.clicked.connect(self.del_mission)
        self.ui.pushButton_5.clicked.connect(self.refresh)
        self.ui.pushButton_4.clicked.connect(self.lookinto)
        self.ui.pushButton.clicked.connect(self.distributes)
        self.refresh()
        self.setWindowIcon(QIcon('engineering.ico'))
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.ui.tableWidget.itemDoubleClicked.connect(self.lookinto)

    def distributes(self):
        row = self.ui.tableWidget.currentRow()
        name = self.ui.tableWidget.item(row, 0).text()
        print('distributes:', name)
        file = open('.\\Data\\check\\{}'.format(name), 'r', encoding='utf-8')
        dic = {}
        while 1:
            text = file.readline()[:-1]
            if text == '':
                break
            else:
                text = text.split('#')
                dic[text[0]] = text[1]
        file.close()
        print('dic', dic.items())
        Main.receive(self.q, dic)

    def op(self):
        self.compose = compose()
        self.compose.qwe.connect(self.refresh)
        self.compose.show()

    def refresh(self):
        name = os.listdir('.\\Data\\check\\')
        line = 0
        for x in name:
            row = self.ui.tableWidget.rowCount()
            if row != len(name):
                self.ui.tableWidget.insertRow(row)
            self.ui.tableWidget.setItem(line, 0, QTableWidgetItem(x))
            line += 1

    def del_mission(self):
        row = self.ui.tableWidget.currentRow()
        name = self.ui.tableWidget.item(row, 0).text()
        os.remove('.\\Data\\check\\{}'.format(name))
        self.ui.tableWidget.removeRow(row)
        self.refresh()

    def lookinto(self):
        current = self.ui.tableWidget.currentRow()
        name = self.ui.tableWidget.item(current, 0).text()
        self.compose = compose()
        self.compose.ui.lineEdit.setText(name)
        file = open('.\\Data\\check\\{}'.format(name), 'r', encoding='utf-8')
        line = 0
        while 1:
            text = file.readline()[:-1]
            if text == '':
                break
            else:
                text = text.split('#')
                self.compose.ui.tableWidget.insertRow(line)
                self.compose.ui.tableWidget.setItem(line, 0, QTableWidgetItem(text[0]))
                self.compose.ui.tableWidget.setItem(line, 1, QTableWidgetItem(text[1]))

            line += 1
        self.compose.show()
        file.close()


class compose(QDialog):  # 添加方案
    qwe = pyqtSignal()

    def __init__(self):
        QDialog.__init__(self)
        self.ui = UI_MessageCompose.Ui_Form()
        self.ui.setupUi(self)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.ui.pushButton_2.clicked.connect(self.inset_line)
        self.ui.pushButton_3.clicked.connect(self.delLine)
        self.ui.pushButton_4.clicked.connect(self.done_save)
        self.ui.pushButton_5.clicked.connect(self.add_line)
        self.ui.pushButton.clicked.connect(self.add_delay)
        self.ui.pushButton_7.clicked.connect(self.para_init)
        self.ui.pushButton_6.clicked.connect(self.data_init)
        self.ui.pushButton_8.clicked.connect(self.compare)
        self.setWindowIcon(QIcon('engineering.ico'))
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

    def done_save(self):
        name = self.ui.lineEdit.text()
        if name == '':
            QMessageBox.question(self, '提示', '方案名称不能为空!', QMessageBox.Ok)
            return 0

        find_diff = os.listdir('.\\Data\\check\\')
        for x in find_diff:
            if name == x:
                a = QMessageBox.question(self, '提示', '方案名称已存在,要覆盖吗?', QMessageBox.Yes, QMessageBox.No)
                if a == QMessageBox.Yes:
                    pass
                else:
                    return 0

        rowCount = self.ui.tableWidget.rowCount()
        for row in range(rowCount):
            try:
                decribes = self.ui.tableWidget.item(row, 0).text()
                APDU = self.ui.tableWidget.item(row, 1).text()
            except:
                QMessageBox.question(self, '提示', '列表内容不能为空值!', QMessageBox.Ok)
                return 0

        file = open('.\\Data\\check\\{}'.format(name), 'w+', encoding='utf-8')
        rowCount = self.ui.tableWidget.rowCount()
        times = 1
        for row in range(rowCount):
            decribes = self.ui.tableWidget.item(row, 0).text()
            APDU = self.ui.tableWidget.item(row, 1).text()
            if decribes[0] == str(times)[0]:
                file.write(decribes + '#' + APDU + '\n')
            else:
                file.write(str(times) + ' ' + decribes + '#' + APDU + '\n')
            times += 1
        file.close()
        self.close()
        self.qwe.emit()

    def add_line(self):
        rowCount = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(rowCount)

    def inset_line(self):
        rowCount = self.ui.tableWidget.currentRow()
        if rowCount < 0:
            rowCount = 0
        self.ui.tableWidget.insertRow(rowCount)

    def delLine(self):
        posite = self.ui.tableWidget.currentRow()
        self.ui.tableWidget.removeRow(posite)

    def add_delay(self):
        rowCount = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(rowCount)
        self.ui.tableWidget.setItem(rowCount, 0, QTableWidgetItem('延时(s)'))
        self.ui.tableWidget.setItem(rowCount, 1, QTableWidgetItem('60'))

    def data_init(self):
        rowCount = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(rowCount)
        self.ui.tableWidget.setItem(rowCount, 0, QTableWidgetItem('数据初始化'))
        self.ui.tableWidget.setItem(rowCount, 1, QTableWidgetItem('07 01 0a 43 00 03 00 00 00'))

    def para_init(self):
        rowCount = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(rowCount)
        self.ui.tableWidget.setItem(rowCount, 0, QTableWidgetItem('参数初始化'))
        self.ui.tableWidget.setItem(rowCount, 1, QTableWidgetItem('07 01 0a 43 00 04 00 00 00'))

    def compare(self):
        rowCount = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(rowCount)
        self.ui.tableWidget.setItem(rowCount, 0, QTableWidgetItem('比较'))
