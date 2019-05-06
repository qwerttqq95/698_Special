from PyQt5.QtWidgets import QProgressDialog
import pymysql

class Progress(object):
    def setup(self,QProgressDialog):
        self.bar = QProgressDialog()
        self.bar.setRange(0, 0)
        self.bar.setModal(1)
        self.bar.show()
        self.start_()

    def start_(self):

        self.db = pymysql.connect("172.18.51.79", "Meter698", "qwerttqq", "data")
        self.bar.setValue(10)
        self.cursor = self.db.cursor()
        self.bar.setValue(20)


        # self.cursor.execute("SELECT VERSION()")
        # self.data = cursor.fetchone()
