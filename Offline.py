import UI_Check, UI_MessageCompose, os, threading, Main, configparser
from PyQt5.QtWidgets import QDialog, QLabel, QApplication, QHeaderView, QTableView, QMessageBox, QTableWidgetItem, \
    QTableWidget
from PyQt5.QtCore import pyqtSignal, Qt, QModelIndex, QMimeData, QPoint
from PyQt5.QtGui import QIcon, QDrag, QStandardItem


class check(QDialog, QTableView):  # 自定义测试方案

    def __init__(self, q, port):
        self.q = q
        self.port = port
        QDialog.__init__(self)
        QTableView.__init__(self)
        self.ui = UI_Check.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.op)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.ui.pushButton_3.clicked.connect(self.del_mission)
        self.ui.pushButton_5.clicked.connect(self.refresh)
        self.ui.pushButton_4.clicked.connect(self.lookinto)
        self.ui.pushButton.clicked.connect(self.distributes)
        self.setWindowIcon(QIcon('engineering.ico'))
        # self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.ui.tableWidget.itemDoubleClicked.connect(self.lookinto)
        self.ui.pushButton_6.clicked.connect(lambda: self.port.mesasge.emit())
        self.load_ini()

        self.ui.tableWidget.acceptDrops()

        self.mModel = None
        self.mRowHeight = 30
        self.mValidPress = False
        self.mRowFrom = 0
        self.mRowTo = 0

    def load_ini(self):
        self.conf = configparser.ConfigParser()
        try:
            if os.path.exists('config.ini'):
                self.conf.read('config.ini', encoding='utf-8')
                if self.conf.has_section('scheme') is True:
                    self.refresh()
                else:
                    self.ini()
            else:
                self.ini()
        except:
            pass

    def ini(self):
        ini = open('config.ini', 'w', encoding='utf-8')
        self.conf.add_section('scheme')
        plan_order = ''
        name = os.listdir('.\\Data\\check\\')
        for x in name:
            plan_order = plan_order + ',' + x
        self.conf.set('scheme', 'plan_order', plan_order)
        self.conf.write(ini)
        ini.close()
        self.refresh()

    def closeEvent(self, QCloseEvent):
        ini = open('config.ini', 'w', encoding='utf-8')
        count = self.ui.tableWidget.rowCount()
        plan_order = ''
        for x in range(count):
            a = self.ui.tableWidget.item(x, 0).text()
            plan_order = plan_order + ',' + a
        self.conf.set('scheme', 'plan_order', plan_order)
        self.conf.write(ini)
        ini.close()

    def distributes(self):
        list_ = self.ui.tableWidget.selectedItems()
        for item in list_:
            row = item.row()
            # row = self.ui.tableWidget.currentRow()
            name = self.ui.tableWidget.item(row, 0).text()
            print('下发文件名:', name)
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
        ini = open('config.ini', 'r', encoding='utf-8')
        plan_order = self.conf.get('scheme', 'plan_order')[1:].split(',')
        name = os.listdir('.\\Data\\check\\')
        line = 0
        for x in plan_order:
            row = self.ui.tableWidget.rowCount()
            if row != len(name):
                self.ui.tableWidget.insertRow(row)
            self.ui.tableWidget.setItem(line, 0, QTableWidgetItem(x))
            line += 1
        if len(name) > len(plan_order):
            diff = set(name) ^ set(plan_order)
            for x in diff:
                self.ui.tableWidget.insertRow(line)
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

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            index = self.indexAt(e.pos())
            if index.isValid():
                self.mValidPress = True
                self.mDragPoint = e.pos()
                self.mDragText = self.mModel.item(index.row(), 1).text()
                self.mDragPointAtItem = self.mDragPoint - QPoint(0, index.row() * self.mRowHeight)
                self.mRowFrom = index.row()
        QTableView.mousePressEvent(e)

    def mouseMoveEvent(self, e):
        if not self.mValidPress:
            return
        if e.buttons() & Qt.LeftButton:
            return
        if (e.pos() - self.mDragPoint).manhattanLength() < QApplication.startDragDistance():
            return
        self.mLabel.show()
        self.DoDrag()
        self.mLabel.hide()
        self.mValidPress = False

    def dragEnterEvent(self, e):
        if e.mimeData().hasText():
            e.acceptProposedAction()
        else:
            e.ignore()
            QTableView.dragEnterEvent(e)

    def dragMoveEvent(self, e):
        if e.mimeData().hasText():
            nCurRow = 0
            index = self.indexAt(e.pos())
            if index.isValid():
                if (e.pos().y() - index.row() * self.mRowHeight >= self.mRowHeight / 2):
                    nCurRow = index.row() + 1
                else:
                    nCurRow = index.row()
            else:
                nCurRow = self.mModel.rowCount()
            if nCurRow != self.mRowFrom:
                mRowTo = self.nCurRow
                self.mLabel.setGeometry(1, mRowTo * self.mRowHeight, self.width() - 2, 2)
            e.acceptProposedAction()
            return
        e.ignore()
        QTableView.dragMoveEvent(e)

    def dropEvent(self, e):
        if e.mimeData().hasText():
            if self.mRowTo != self.mRowFrom:
                self.MoveRow(self.mRowFrom, self.mRowTo)
            e.acceptProposedAction()
            return
        e.ignore()
        QTableView.dropEvent(e)

    def DoDrag(self):
        drag = QDrag()
        mimeData = QMimeData()
        mimeData.setText(self.mDragText)
        drag.setMimeData(mimeData)

        drag.setHotSpot(self.mDragPointAtItem)
        if drag.exec(Qt.MoveAction) == Qt.MoveAction:
            pass

    def ResetOrder(self):
        i = 0
        while 1:
            if i < self.mModel.rowCount():
                self.mModel.item(i, 0).setText(i + 1)
                i += 1
            else:
                break

    def MoveRow(self, from_, to_):
        if from_ == to_:
            return
        item = self.mModel.item(from_, 1)
        if item:
            strText = item.text()
            items = []
            item0 =  QStandardItem("")
            item1 =  QStandardItem(strText)
            items.append(item0)
            items.append(item1)
            item0.setTextAlignment(Qt.AlignCenter)
            self.mModel.insertRow(to_, items)
            if from_ < to_:
                self.mModel.removeRow(from_)
                self.selectRow(to_ - 1)
            else:
                self.mModel.removeRow(from_+1)
                self.selectRow(to_)
            self.ResetOrder()
            self.emit.sigRowChange(self.mRowFrom, self.mRowTo)


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
        # self.setWindowFlags(Qt.WindowStaysOnTopHint)

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
