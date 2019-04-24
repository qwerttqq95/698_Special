from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
import sys, UI_MainWindow, UI_ConnectionSet, UI_Customize, UI_MessageParsing_start, UI_Convert, binascii, serial, time, \
    Comm, datetime, threading, re, traceback, serial.tools.list_ports, UI_APDU
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt, QThread
from PyQt5.QtGui import QTextCursor


class ReadAddress(QThread):
    def __init__(self):
        super(ReadAddress, self).__init__()

    def run(self):
        self.strInput = "68 17 00 43 45 AA AA AA AA AA AA 10 DA 5F 05 01 03 40 01 02 00 00 90 0F 16"
        Ports().Prsend(self.strInput)
        self.SA = Comm.SA_add
        if self.SA == '':
            MainWindow.showText('R', ['读地址超时'])
        else:
            print('SA地址', self.SA)
            add = ''
            for i in self.SA:
                add = add + i
            MainWindow.showText('R', ['终端地址为:', add])
            self.add = add
            Comm.SetSA(self.SA)


class Ethernet_configuration(QThread):
    def __init__(self):
        super(Ethernet_configuration, self).__init__()

    def run(self):
        self.strInput_1 = ['06 01 04 45 10 03 00 01 01 02 02 09 04 C0 A8 01 FD 12 22 B8 00',
                           '06 01 13 45 10 04 00 02 06 16 01 09 04 C0 A8 01 09 09 04 FF FF FF 00 09 04 7F 00 00 01 0A 01 30 0A 01 30 00']
        if Comm.SA_add == '':
            MainWindow.PrReadAdd()
        time.sleep(2)
        if Comm.SA_add == '':
            pass
        else:
            for i in self.strInput_1:
                reValue = Comm.BuildMessage(i.replace(' ', ''), Comm.SA_add, 'dan')
                print('reValue', reValue)
                if reValue == '0':
                    break
                else:
                    Ports().Prsend(reValue)


class Real_time_data_testing_serial_port(QThread):
    def __init__(self):
        super(Real_time_data_testing_serial_port, self).__init__()

    def run(self):
        if Comm.SA_add == '':
            MainWindow.PrReadAdd()
        time.sleep(2)
        if Comm.SA_add == '':
            pass
        else:
            GetAPDU('Default', 'Real')
        MainWindow.ui.statusBar.showMessage('下发完成...', 0)


class Real_time_data_testing_serial_port_read(QThread):
    def __init__(self):
        super(Real_time_data_testing_serial_port_read, self).__init__()

    def run(self):
        if Comm.SA_add == '':
            MainWindow.PrReadAdd()
        time.sleep(2)
        if Comm.SA_add == '':
            pass
        else:
            GetAPDU('Default', 'Real读取报文')
        MainWindow.ui.statusBar.showMessage('下发完成...', 0)


class Default_Day(QThread):
    def __init__(self):
        super(Default_Day, self).__init__()

    def run(self):
        if Comm.SA_add == '':
            MainWindow.PrReadAdd()
        time.sleep(2)
        if Comm.SA_add == '':
            pass
        else:
            GetAPDU('Default', 'Day')
        MainWindow.ui.statusBar.showMessage('下发完成...', 0)


class Default_Day_read(QThread):
    def __init__(self):
        super(Default_Day_read, self).__init__()

    def run(self):
        if Comm.SA_add == '':
            MainWindow.PrReadAdd()
        time.sleep(2)
        if Comm.SA_add == '':
            pass
        else:
            GetAPDU('Default', 'Day读取报文')
        MainWindow.ui.statusBar.showMessage('下发完成...', 0)


class Default_Curve(QThread):
    def __init__(self):
        super(Default_Curve, self).__init__()

    def run(self):
        if Comm.SA_add == '':
            MainWindow.PrReadAdd()
        time.sleep(2)
        if Comm.SA_add == '':
            pass
        else:
            GetAPDU('Default', 'Curve')
        MainWindow.ui.statusBar.showMessage('下发完成...', 0)


class zhejiangREAL0200(QThread):
    def __init__(self):
        super(zhejiangREAL0200, self).__init__()

    def run(self):
        if Comm.SA_add == '':
            MainWindow.PrReadAdd()
        time.sleep(2)
        if Comm.SA_add == '':
            pass
        else:
            GetAPDU('Zhejiang', '0200')
        MainWindow.ui.statusBar.showMessage('下发完成...', 0)


class zhejiangREAL0201(QThread):
    def __init__(self):
        super(zhejiangREAL0201, self).__init__()

    def run(self):
        if Comm.SA_add == '':
            MainWindow.PrReadAdd()
        time.sleep(2)
        if Comm.SA_add == '':
            pass
        else:
            GetAPDU('Zhejiang', '0201')
        MainWindow.ui.statusBar.showMessage('下发完成...', 0)


class zhejiangCurve0200(QThread):
    def __init__(self):
        super(zhejiangCurve0200, self).__init__()

    def run(self):
        if Comm.SA_add == '':
            MainWindow.PrReadAdd()
        time.sleep(2)
        if Comm.SA_add == '':
            pass
        else:
            GetAPDU('Zhejiang', 'Curve0201')
        MainWindow.ui.statusBar.showMessage('下发完成...', 0)


class zhejiangCurve0201(QThread):
    def __init__(self):
        super(zhejiangCurve0201, self).__init__()

    def run(self):
        if Comm.SA_add == '':
            MainWindow.PrReadAdd()
        time.sleep(2)
        if Comm.SA_add == '':
            pass
        else:
            GetAPDU('Zhejiang', 'Curve0201')
        MainWindow.ui.statusBar.showMessage('下发完成...', 0)


class Time_Control(QThread):
    def __init__(self):
        super(Time_Control, self).__init__()

    def run(self):
        if Comm.SA_add == '':
            MainWindow.PrReadAdd()
        time.sleep(2)
        if Comm.SA_add == '':
            pass
        else:
            GetAPDU('Default', '时段功控投入')

        MainWindow.ui.statusBar.showMessage('下发完成...', 0)


class Time_Control_f(QThread):
    def __init__(self):
        super(Time_Control_f, self).__init__()

    def run(self):
        if Comm.SA_add == '':
            MainWindow.PrReadAdd()
        time.sleep(2)
        if Comm.SA_add == '':
            pass
        else:
            GetAPDU('Default', '时段功控解除')
        MainWindow.ui.statusBar.showMessage('下发完成...', 0)


class Factory_control(QThread):
    def __init__(self):
        super(Factory_control, self).__init__()

    def run(self):
        if Comm.SA_add == '':
            MainWindow.PrReadAdd()
        time.sleep(2)
        if Comm.SA_add == '':
            pass
        else:
            GetAPDU('Default', '厂休功控投入')
        MainWindow.ui.statusBar.showMessage('下发完成...', 0)


class Factory_control_f(QThread):
    def __init__(self):
        super(Factory_control_f, self).__init__()

    def run(self):
        if Comm.SA_add == '':
            MainWindow.PrReadAdd()
        time.sleep(2)
        if Comm.SA_add == '':
            pass
        else:
            GetAPDU('Default', '厂休功控解除')
        MainWindow.ui.statusBar.showMessage('下发完成...', 0)


class Current_power_float_control(QThread):
    def __init__(self):
        super(Current_power_float_control, self).__init__()

    def run(self):
        if Comm.SA_add == '':
            MainWindow.PrReadAdd()
        time.sleep(2)
        if Comm.SA_add == '':
            pass
        else:
            GetAPDU('Default', '投入当前功率下浮控')
        MainWindow.ui.statusBar.showMessage('下发完成...', 0)


class Current_power_float_control_f(QThread):
    def __init__(self):
        super(Current_power_float_control_f, self).__init__()

    def run(self):
        if Comm.SA_add == '':
            MainWindow.PrReadAdd()
        time.sleep(2)
        if Comm.SA_add == '':
            pass
        else:
            GetAPDU('Default', '解除当前功率下浮控')
        MainWindow.ui.statusBar.showMessage('下发完成...', 0)


class Business_report_stop(QThread):
    def __init__(self):
        super(Business_report_stop, self).__init__()

    def run(self):
        if Comm.SA_add == '':
            MainWindow.PrReadAdd()
        time.sleep(2)
        if Comm.SA_add == '':
            pass
        else:
            GetAPDU('Default', '营业报停功控投入')
        MainWindow.ui.statusBar.showMessage('下发完成...', 0)


class Business_report_stop_f(QThread):
    def __init__(self):
        super(Business_report_stop_f, self).__init__()

    def run(self):
        if Comm.SA_add == '':
            MainWindow.PrReadAdd()
        time.sleep(2)
        if Comm.SA_add == '':
            pass
        else:
            GetAPDU('Default', '营业报停功控解除')
        MainWindow.ui.statusBar.showMessage('下发完成...', 0)


class Monthly_power_control_investment(QThread):
    def __init__(self):
        super(Monthly_power_control_investment, self).__init__()

    def run(self):
        if Comm.SA_add == '':
            MainWindow.PrReadAdd()
        time.sleep(2)
        if Comm.SA_add == '':
            pass
        else:
            GetAPDU('Default', '月电控投入')
        MainWindow.ui.statusBar.showMessage('下发完成...', 0)


class Monthly_power_control_investment_f(QThread):
    def __init__(self):
        super(Monthly_power_control_investment_f, self).__init__()

    def run(self):
        if Comm.SA_add == '':
            MainWindow.PrReadAdd()
        time.sleep(2)
        if Comm.SA_add == '':
            pass
        else:
            GetAPDU('Default', '月电控解除')
        MainWindow.ui.statusBar.showMessage('下发完成...', 0)


class Purchase_of_electric_control_inputs(QThread):
    def __init__(self):
        super(Purchase_of_electric_control_inputs, self).__init__()

    def run(self):
        if Comm.SA_add == '':
            MainWindow.PrReadAdd()
        time.sleep(2)
        if Comm.SA_add == '':
            pass
        else:
            GetAPDU('Default', '购电控投入')
        MainWindow.ui.statusBar.showMessage('下发完成...', 0)


class Purchase_of_electric_control_inputs_f(QThread):
    def __init__(self):
        super(Purchase_of_electric_control_inputs_f, self).__init__()

    def run(self):
        if Comm.SA_add == '':
            MainWindow.PrReadAdd()
        time.sleep(2)
        if Comm.SA_add == '':
            pass
        else:
            GetAPDU('Default', '购电控解除')
        MainWindow.ui.statusBar.showMessage('下发完成...', 0)


class Reminder_alarm_input(QThread):
    def __init__(self):
        super(Reminder_alarm_input, self).__init__()

    def run(self):
        if Comm.SA_add == '':
            MainWindow.PrReadAdd()
        time.sleep(2)
        if Comm.SA_add == '':
            pass
        else:
            GetAPDU('Default', '催费告警投入')
        MainWindow.ui.statusBar.showMessage('下发完成...', 0)


class Reminder_alarm_input_f(QThread):
    def __init__(self):
        super(Reminder_alarm_input_f, self).__init__()

    def run(self):
        if Comm.SA_add == '':
            MainWindow.PrReadAdd()
        time.sleep(2)
        if Comm.SA_add == '':
            pass
        else:
            GetAPDU('Default', '催费告警解除')
        MainWindow.ui.statusBar.showMessage('下发完成...', 0)


class Power(QThread):
    def __init__(self):
        super(Power, self).__init__()

    def run(self):
        if Comm.SA_add == '':
            MainWindow.PrReadAdd()
        time.sleep(2)
        if Comm.SA_add == '':
            pass
        else:
            GetAPDU('Default', '保电投入')
        MainWindow.ui.statusBar.showMessage('下发完成...', 0)


class Power_f(QThread):
    def __init__(self):
        super(Power_f, self).__init__()

    def run(self):
        if Comm.SA_add == '':
            MainWindow.PrReadAdd()
        time.sleep(2)
        if Comm.SA_add == '':
            pass
        else:
            GetAPDU('Default', '保电解除')
        MainWindow.ui.statusBar.showMessage('下发完成...', 0)


class Trip(QThread):
    def __init__(self):
        super(Trip, self).__init__()

    def run(self):
        if Comm.SA_add == '':
            MainWindow.PrReadAdd()
        time.sleep(2)
        if Comm.SA_add == '':
            pass
        else:
            GetAPDU('Default', '跳闸')
        MainWindow.ui.statusBar.showMessage('下发完成...', 0)


class Trip_f(QThread):
    def __init__(self):
        super(Trip_f, self).__init__()

    def run(self):
        if Comm.SA_add == '':
            MainWindow.PrReadAdd()
        time.sleep(2)
        if Comm.SA_add == '':
            pass
        else:
            GetAPDU('Default', '合闸')
        MainWindow.ui.statusBar.showMessage('下发完成...', 0)


class Eliminate_input(QThread):
    def __init__(self):
        super(Eliminate_input, self).__init__()

    def run(self):
        if Comm.SA_add == '':
            MainWindow.PrReadAdd()
        time.sleep(2)
        if Comm.SA_add == '':
            pass
        else:
            GetAPDU('Default', '剔除投入')
        MainWindow.ui.statusBar.showMessage('下发完成...', 0)


class Eliminate_input_f(QThread):
    def __init__(self):
        super(Eliminate_input_f, self).__init__()

    def run(self):
        if Comm.SA_add == '':
            MainWindow.PrReadAdd()
        time.sleep(2)
        if Comm.SA_add == '':
            pass
        else:
            GetAPDU('Default', '剔除解除')
        MainWindow.ui.statusBar.showMessage('下发完成...', 0)


class zu(QThread):
    def __init__(self):
        super(zu, self).__init__()

    def run(self):
        if Comm.SA_add == '':
            MainWindow.PrReadAdd()
        time.sleep(2)
        if Comm.SA_add == '':
            pass
        else:
            add0 = '68 21 00 43 45 aa aa aa aa aa aa 10 62 39 06 01 34 40 05 02 00 01 01 09 06 00 00 00 00 00 01 00 57 60 16 '
            Ports().Prsend_zu(add0)
            add1 = ['06 01 36 40 00 02 00 1c 07 e2 09 0b 0a 1f 00 00']
            for i in add1:
                Ports().Prsend(Comm.BuildMessage(i.replace(' ', ''), Comm.SA_add, 'dan'))
            add2 = '68 31 00 43 85 01 00 00 00 00 00 10 39 2A 07 01 3B 80 00 81 00 01 01 02 04 51 F2 05 02 02 11 01 12 00 00 03 01 01 07 E2 09 0B 0A 13 15 01 00 C8 F8 E2 16'
            Ports().Prsend_zu(add2)
            MainWindow.statusBarshow('下发完成')


class Data_Initialization(QThread):
    def __init__(self):
        super(Data_Initialization, self).__init__()

    def run(self):
        if Comm.SA_add == '':
            MainWindow.PrReadAdd()
        time.sleep(2)
        # print('Comm.SA_add:', Comm.SA_add, 'type:', type(Comm.SA_add))
        if Comm.SA_add == '':
            pass
        else:
            GetAPDU('Default', '数据初始化')
        MainWindow.ui.statusBar.showMessage('下发完成...', 0)


class Parameter_Initialization(QThread):
    def __init__(self):
        super(Parameter_Initialization, self).__init__()

    def run(self):
        if Comm.SA_add == '':
            MainWindow.PrReadAdd()
        time.sleep(2)
        if Comm.SA_add == '':
            pass
        else:
            GetAPDU('Default', '参数初始化')
        MainWindow.ui.statusBar.showMessage('下发完成...', 0)


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = UI_MainWindow.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())

        self.cust = Customize()

        self.parsing = UI_MessageParsing_start.ParsingMain()
        self.ui.actionC.triggered.connect(self.parsing.show)

        self.ui.actionA.triggered.connect(self.about)
        self.ui.actionSdf.triggered.connect(self.PrEthernet_configuration)

        self.convert = Convert()
        self.ui.actionDf.triggered.connect(self.convert.show)

        self.ui.actionG.triggered.connect(self.PrReadAdd)
        self.ui.pushButton_2.clicked.connect(self.clear)
        self.ui.actionX_2.triggered.connect(self.cust.show)
        self.ui.actionSh.triggered.connect(self.PrReal_time_data_testing_serial_port)
        self.ui.actionRi.triggered.connect(self.PrDefaultDay)
        self.ui.action_19.triggered.connect(self.PrReal_time_data_testing_serial_port_read)
        self.ui.action_21.triggered.connect(self.PrDefaultDay_read)
        self.ui.action0200_3.triggered.connect(self.Przhejiang0200)
        self.ui.action0201_2.triggered.connect(self.Przhejiang0201)
        self.ui.action0020l.triggered.connect(self.Przhejiangcurve0200)
        self.ui.action0201l.triggered.connect(self.Przhejiangcurve0201)
        self.ui.actionQu.triggered.connect(self.PrDefaultCurve)
        self.ui.actionS.triggered.connect(self.PrTime_control)
        self.ui.action_a.triggered.connect(self.PrTime_control_f)
        self.ui.action_3.triggered.connect(self.PrFactory_control)
        self.ui.action_4.triggered.connect(self.PrFactory_control_f)
        self.ui.action_5.triggered.connect(self.PrBusiness_report_stop)
        self.ui.action_6.triggered.connect(self.PrBusiness_report_stop_f)
        self.ui.action_7.triggered.connect(self.PrMonthly_power_control_investment)
        self.ui.action_8.triggered.connect(self.PrMonthly_power_control_investment_f)
        self.ui.action_9.triggered.connect(self.PrPurchase_of_electric_control_inputs)
        self.ui.action_10.triggered.connect(self.PrPurchase_of_electric_control_inputs_f)
        self.ui.action_11.triggered.connect(self.PrReminder_alarm_input)
        self.ui.action_12.triggered.connect(self.PrReminder_alarm_input_f)
        self.ui.action_13.triggered.connect(self.PrPower)
        self.ui.action_14.triggered.connect(self.PrPower_f)
        self.ui.action_15.triggered.connect(self.PrTrip)
        self.ui.action_16.triggered.connect(self.PrTrip_f)
        self.ui.action_17.triggered.connect(self.PrEliminate_input)
        self.ui.action_18.triggered.connect(self.PrEliminate_input_f)
        self.ui.actionZ.triggered.connect(self.Przu)
        self.ui.actionShuju.triggered.connect(self.PrDateIni)

        self.ui.actionCanshu.triggered.connect(self.Prpara)
        self.ui.action_22.triggered.connect(self.PrCurrent_power_float_control)
        self.ui.action_2.triggered.connect(self.PrCurrent_power_float_control_f)
        self.apdu = APUD_send()
        self.ui.actionAPDUzu.triggered.connect(self.apdu.show)
        self.ui.textEdit_2.textChanged.connect(self.move_Cursor)


    def move_Cursor(self):
        self.ui.textEdit_2.moveCursor(QTextCursor.End)

    def statusBarshow(self, message):
        self.ui.statusBar.showMessage(message, 3)

    def PrReadAdd(self):
        self.PRD = ReadAddress()
        self.PRD.start()

    def PrEthernet_configuration(self):
        self.PEC = Ethernet_configuration()
        self.PEC.start()

    def PrReal_time_data_testing_serial_port(self):
        self.ui.statusBar.showMessage('下发中...', 0)
        self.PRTDTSP = Real_time_data_testing_serial_port()
        self.PRTDTSP.start()

    def PrReal_time_data_testing_serial_port_read(self):
        self.ui.statusBar.showMessage('下发中...', 0)
        self.PRTDTSPr = Real_time_data_testing_serial_port_read()
        self.PRTDTSPr.start()

    def PrDefaultDay(self):
        self.ui.statusBar.showMessage('下发中...', 0)
        self.PDD = Default_Day()
        self.PDD.start()

    def PrDefaultDay_read(self):
        self.ui.statusBar.showMessage('下发中...', 0)
        self.PDDr = Default_Day_read()
        self.PDDr.start()

    def PrDefaultCurve(self):
        self.ui.statusBar.showMessage('下发中...', 0)
        self.PDC = Default_Curve()
        self.PDC.start()

    def Przhejiang0200(self):
        self.ui.statusBar.showMessage('下发中...', 0)
        self.P0200 = zhejiangREAL0200()
        self.P0200.start()

    def Przhejiang0201(self):
        self.ui.statusBar.showMessage('下发中...', 0)
        self.P0201 = zhejiangREAL0201()
        self.P0201.start()

    def Przhejiangcurve0200(self):
        self.ui.statusBar.showMessage('下发中...', 0)
        self.Pcurve0200 = zhejiangCurve0200()
        self.Pcurve0200.start()

    def Przhejiangcurve0201(self):
        self.ui.statusBar.showMessage('下发中...', 0)
        self.Pcurve0201 = zhejiangCurve0201()
        self.Pcurve0201.start()

    def PrTime_control(self):
        self.ui.statusBar.showMessage('下发中...', 0)
        self.Pc = Time_Control()
        self.Pc.start()

    def PrTime_control_f(self):
        self.ui.statusBar.showMessage('下发中...', 0)
        self.PT = Time_Control_f()
        self.PT.start()

    def PrFactory_control(self):
        self.ui.statusBar.showMessage('下发中...', 0)
        self.PTc = Factory_control()
        self.PTc.start()

    def PrFactory_control_f(self):
        self.ui.statusBar.showMessage('下发中...', 0)
        self.PFc = Factory_control_f()
        self.PFc.start()

    def PrCurrent_power_float_control(self):
        self.ui.statusBar.showMessage('下发中...', 0)
        self.Pcpfc = Current_power_float_control()
        self.Pcpfc.start()

    def PrCurrent_power_float_control_f(self):
        self.ui.statusBar.showMessage('下发中...', 0)
        self.Pcpfcf = Current_power_float_control_f()
        self.Pcpfcf.start()

    def PrBusiness_report_stop(self):
        self.ui.statusBar.showMessage('下发中...', 0)
        self.PBrs = Business_report_stop()
        self.PBrs.start()

    def PrBusiness_report_stop_f(self):
        self.ui.statusBar.showMessage('下发中...', 0)
        self.PBrsf = Business_report_stop_f()
        self.PBrsf.start()

    def PrMonthly_power_control_investment(self):
        self.ui.statusBar.showMessage('下发中...', 0)
        self.PBrsf = Monthly_power_control_investment()
        self.PBrsf.start()

    def PrMonthly_power_control_investment_f(self):
        self.ui.statusBar.showMessage('下发中...', 0)
        self.PBrsf = Monthly_power_control_investment_f()
        self.PBrsf.start()

    def PrPurchase_of_electric_control_inputs(self):
        self.ui.statusBar.showMessage('下发中...', 0)
        self.PPOFECI = Purchase_of_electric_control_inputs()
        self.PPOFECI.start()

    def PrPurchase_of_electric_control_inputs_f(self):
        self.ui.statusBar.showMessage('下发中...', 0)
        self.PPOFECIf = Purchase_of_electric_control_inputs_f()
        self.PPOFECIf.start()

    def PrReminder_alarm_input(self):
        self.ui.statusBar.showMessage('下发中...', 0)
        self.PRAI = Reminder_alarm_input()
        self.PRAI.start()

    def PrReminder_alarm_input_f(self):
        self.ui.statusBar.showMessage('下发中...', 0)
        self.PRAIF = Reminder_alarm_input_f()
        self.PRAIF.start()

    def PrPower(self):
        self.ui.statusBar.showMessage('下发中...', 0)
        self.PP = Power()
        self.PP.start()

    def PrPower_f(self):
        self.ui.statusBar.showMessage('下发中...', 0)
        self.PPf = Power_f()
        self.PPf.start()

    def PrTrip(self):
        self.ui.statusBar.showMessage('下发中...', 0)
        self.Ptp = Trip()
        self.Ptp.start()

    def PrTrip_f(self):
        self.ui.statusBar.showMessage('下发中...', 0)
        self.PTF = Trip_f()
        self.PTF.start()

    def PrEliminate_input(self):
        self.ui.statusBar.showMessage('下发中...', 0)
        self.PTF = Eliminate_input()
        self.PTF.start()

    def PrEliminate_input_f(self):
        self.ui.statusBar.showMessage('下发中...', 0)
        self.PTF = Eliminate_input_f()
        self.PTF.start()

    def Przu(self):
        self.ui.statusBar.showMessage('下发中...', 0)
        self.pzu = zu()
        self.pzu.start()

    def PrDateIni(self):
        self.ui.statusBar.showMessage('下发中...', 0)
        self.pDI = Data_Initialization()
        self.pDI.start()

    def Prpara(self):
        self.ui.statusBar.showMessage('下发中...', 0)
        self.para = Parameter_Initialization()
        self.para.start()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '提示', '你确认要退出吗？', QMessageBox.Yes,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def about(self):
        QMessageBox.about(self, '关于', 'V1.0')

    def clear(self):
        self.ui.textEdit.clear()
        self.ui.textEdit_2.clear()

    def add_L(self):
        self.ui.textEdit_2.append(datetime.datetime.now().strftime('%m-%d   %T'))
        self.ui.textEdit_2.append('-----------------------')

    def add_R(self):
        self.ui.textEdit.append(datetime.datetime.now().strftime('%m-%d   %T'))
        self.ui.textEdit.append('-----------------------')

    def showText(self, turn, textlist):
        if turn == 'L':
            for x in textlist:
                self.ui.textEdit_2.append(x)
            self.add_L()
        elif turn == 'R':
            for x in textlist:
                self.ui.textEdit.append(x)
            self.add_R()
        else:
            print('ERROR ON turn')


class Ports():
    def __init__(self):
        self.communication_serial_por = ConnectionSet.ui.comboBox.currentText()
        self.check = ConnectionSet.ui.comboBox_3.currentText()
        self.Baud_rate = int(ConnectionSet.ui.comboBox_2.currentText())
        self.stop_bit = int(ConnectionSet.ui.comboBox_4.currentText())
        self.config_S = self.Communication_serial_port()

    def Prsend(self, strInput):
        self.strInput = strInput
        if self.strInput and self.strInput != '0':
            print('strInput:', self.strInput)
            if self.strInput[2] != ' ':
                self.strInput = Comm.makestr(strInput)
            t = MyThread(self.Send, args=(self.strInput,))
            t.start()
            t.join()
            # print('返回值:', t.get_result())
            if t.get_result() == 'ERROR':
                MainWindow.showText('L', ['无法发送'])
            else:
                Comm.Analysis().start698(t.get_result())
                MainWindow.showText('L', ['发送报文:', strInput, '收到报文:', Comm.makestr(t.get_result())])
        else:
            print('ERROR with strInput', strInput)

    def Send(self, strInput):
        print(self.config_S)
        if self.config_S[2] == '偶':
            self.parity_ = 'E'
        try:
            self.t = serial.Serial(self.config_S[0], self.config_S[1], timeout=0.5, parity=self.parity_,
                                   stopbits=self.config_S[3])
            self.t.write(bytes.fromhex(strInput))
            remessage = Ports.Receive(self)
            self.t.close()
        except:
            remessage = 'ERROR'
            traceback.print_exc(file=open('bug.txt', 'a+'))
        return remessage

    def Receive(self):
        time_start = time.time()
        try:
            while 1:
                time.sleep(1.5)
                num = self.t.inWaiting()
                if num > 25:
                    data = str(binascii.b2a_hex(self.t.read(num)))[2:-1]
                    print('num:', num)
                    print('Received: ', data)
                    break
                time_out = time.time()
                if time_out - time_start > 8:
                    data = 'ERROR'
                    break
            return data
        except:
            pass

    def Communication_serial_port(self):
        return self.communication_serial_por, self.Baud_rate, self.check, self.stop_bit

    def Meter_reading_serial_port(self):
        self.communication_serial_port = ConnectionSet.ui.comboBox_5.currentText()
        self.check = ConnectionSet.ui.comboBox_6.currentText()
        self.Baud_rate = int(ConnectionSet.ui.comboBox_7.currentText())
        self.stop_bit = int(ConnectionSet.ui.comboBox_8.currentText())

    def Prsend_zu(self, strInput):
        self.strInput_zu = strInput
        t = MyThread(self.Send_zu, args=(self.strInput_zu,))
        t.start()
        t.join()

    def Send_zu(self, strInput):
        print(self.config_S)
        if self.config_S[2] == '偶':
            self.parity_ = 'E'
        self.t = serial.Serial(self.config_S[0], self.config_S[1], timeout=0.5, parity=self.parity_,
                               stopbits=self.config_S[3])
        self.t.write(bytes.fromhex(strInput))
        self.t.close()
        MainWindow.showText('L', ['发送报文:', strInput])


class ConnectionSet(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = UI_ConnectionSet.Ui_Dialog()
        self.ui.setupUi(self)
        addItem = self.GetSerialNumber()
        addItem.sort()
        for self.addItem in addItem:
            self.ui.comboBox.addItem(self.addItem)
            self.ui.comboBox_5.addItem(self.addItem)
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlags(Qt.WindowStaysOnTopHint)


    def GetSerialNumber(self):
        SerialNumber = []
        port_list = list(serial.tools.list_ports.comports())
        if len(port_list) <= 0:
            print("The Serial port can't find!")
        else:
            for i in list(port_list):
                print(i[0])
                SerialNumber.append(i[0])
            return SerialNumber


class Convert(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = UI_Convert.Ui_Dialog()
        self.ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.ui.pushButton_2.clicked.connect(self.strtohex)
        self.ui.pushButton.clicked.connect(self.hextostr)

    def hextostr(self):
        try:
            self.text = self.ui.textEdit.toPlainText()
            self.output = str(binascii.unhexlify(self.text))
            self.ui.textEdit_2.setText(self.output[2:-1])
        except:
            self.ui.textEdit_2.setText('无法解析')

    def strtohex(self):
        self.text = self.ui.textEdit.toPlainText()
        self.output = str(binascii.hexlify(bytes(self.text, encoding='UTF-8')))
        self.ui.textEdit_2.setText(self.output[2:-1])


class Customize(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = UI_Customize.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)


class MyThread(threading.Thread):
    def __init__(self, func, args=()):
        super(MyThread, self).__init__()
        self.func = func
        self.args = args

    def run(self):
        self.result = self.func(*self.args)

    def get_result(self):
        try:
            return self.result
        except Exception:
            return None


def GetAPDU(kind, stat):
    f = open('source\\' + kind, 'r', encoding='UTF-8')
    while 1:
        text2 = f.readline()[:-1]
        if text2 == stat:
            while 1:
                text = f.readline()[:-1]
                if text == '':
                    print('Finished...')
                    MainWindow.statusBarshow('下发完成')
                    break
                point = re.findall('#', text)
                try:
                    if point[0] == '#':
                        text = text.split('#')
                        print(text[0])
                        MainWindow.ui.textEdit_2.append(text[0])
                        Ports().Prsend(Comm.BuildMessage(text[1].replace(' ', ''), Comm.SA_add, 'dan'))
                except:
                    print('GetAPDU ERROR')
                    MainWindow.showText('L', ['无法发送(APDU)'])
                    MainWindow.ui.statusBar.showMessage('Failed...', 2)
                    traceback.print_exc(file=open('bug.txt', 'a+'))
                    break
            f.close()
            break
        else:
            continue


class APUD_send(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = UI_APDU.Ui_Dialog()
        self.ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.ui.pushButton.clicked.connect(self.GetText)

    def GetText(self):
        if Comm.SA_add == '':
            MainWindow.PrReadAdd()
        time.sleep(2)
        if Comm.SA_add == '':
            pass
        else:
            self.text = self.ui.textEdit.toPlainText()
            if self.text:
                if self.ui.radioButton_2.isChecked():
                    Ports().Prsend(Comm.BuildMessage(self.text.replace(' ', ''), Comm.SA_add, 'dan'))
                if self.ui.radioButton.isChecked():
                    Ports().Prsend(self.text.replace(' ', ''))




if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        MainWindow = MainWindow()
        ConnectionSet = ConnectionSet()
        action = MainWindow.ui.actionSd
        action.triggered.connect(ConnectionSet.show)
        MainWindow.show()
        sys.exit(app.exec_())
    except:
        traceback.print_exc(file=open('bug.txt', 'a+'))
