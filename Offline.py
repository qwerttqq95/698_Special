import UI_Check, UI_MessageCompose, os
from PyQt5.QtWidgets import QDialog, QHeaderView, QMessageBox, QTableWidgetItem
from PyQt5.QtCore import pyqtSignal

class check(QDialog):  # 自定义测试方案

    def __init__(self):
        QDialog.__init__(self)
        self.ui = UI_Check.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.op)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.ui.pushButton_3.clicked.connect(self.del_mission)
        self.refresh()


    def op(self):
        self.compose = compose()
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
        name = self.ui.tableWidget.item(row,0).text()
        os.remove('.\\Data\\check\\{}'.format(name))
        self.ui.tableWidget.removeRow(row)

        self.refresh()

class compose(QDialog):  # 添加方案
    def __init__(self):
        QDialog.__init__(self)
        self.ui = UI_MessageCompose.Ui_Form()
        self.ui.setupUi(self)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.ui.pushButton_2.clicked.connect(self.inset_line)
        self.ui.pushButton_3.clicked.connect(self.delLine)
        self.ui.pushButton_4.clicked.connect(self.done_save)
        self.ui.pushButton_5.clicked.connect(self.add_line)
        self.check = check()

    def done_save(self):
        name = self.ui.lineEdit.text()
        if name == '':
            QMessageBox.question(self, '提示', '方案名称不能为空!', QMessageBox.Ok)
            return 0

        find_diff = os.listdir('.\\Data\\check\\')
        for x in find_diff:
            if name == x:
                QMessageBox.question(self, '提示', '方案名称不能重复!', QMessageBox.Ok)
                return 0

        file = open('.\\Data\\check\\{}'.format(name), 'w+', encoding='utf-8')
        rowCount = self.ui.tableWidget.rowCount()
        for row in range(rowCount):
            decribes = self.ui.tableWidget.item(row, 0).text()
            APDU = self.ui.tableWidget.item(row, 1).text()
            file.write(decribes + '#' + APDU + '\n')

        self.check.refresh()
        self.close()

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
