import xml.etree.ElementTree as ET
import UI_MessageParsing, Comm
from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from PyQt5.QtCore import Qt


class MessageParsing():
    def __init__(self):
        self.data = open('source\output.xml', 'r', encoding='UTF-8', errors='ignore')
        self.root = ET.parse(self.data).getroot()

    def Analysis_1(self, code):
        while 1:
            if len(code) == 0:
                break
            if code[0] != '6':
                code = code[1:]
            elif code[-1] != '6':
                code = code[0:-1]
            else:
                break
        if len(code) == 0:
            print('无法解析len')
            return 'ErrorLen'
        else:
            code = Comm.makelist(code.replace(' ', ''))
            try:
                Rectrlc_1 = Comm.Analysis().ctrlc_1(Comm.dec2bin(int(code[3], 16)).zfill(2))
                if Rectrlc_1 == 3:
                    SA_len_num = Comm.Analysis().SASign(Comm.dec2bin(int(code[4], 16)).zfill(8))
                    APDU = code[5 + SA_len_num:][3:-3]
                    print(APDU)
                    if APDU[0] == '85' and APDU[1] == '03':
                        self.Information(APDU[0], APDU[1], APDU)
                    else:
                        print('暂时不支持apdu')
                        return 'ErrorAPDU'
                    print('dic:', dic, '\nkey:', key)
            except:
                print('Rectrlc_1_error')

            else:
                print('暂时不支持:控制码!=3')
                return 'ErrorConctrlCode!=3'

    def APDUstart(self, APDU):
        print('APDU start')
        while 1:
            if APDU[0] != '8':
                APDU = APDU[1:]

            else:
                break
        APDU = Comm.makelist(APDU.replace(' ', ''))
        self.Information(APDU[0], APDU[1], APDU)

    def Information(self, num, detail, APDU):
        if num == '01':
            print(num, '预链接请求')
        elif num == '81':
            print(num, '预链接响应')
        elif num == '02':
            print(num, '应用链接请求')
        elif num == '82':
            print(num, '应用链接响应')
        elif num == '03':
            print(num, '断开链接响应')
        elif num == '83':
            print(num, '断开链接请求')
        elif num == '05':
            print(num, '读取请求', end=' ')
            if detail == '01':
                print(detail, '读取一个对象属性请求(GetRequestNormal) ')
            elif detail == '02':
                print(detail, '读取若干个对象属性请求 (GetRequestNormalList) ')
            elif detail == '03':
                print(detail, '读取一个记录型对象属性请求 (GetRequestRecord) ')
            elif detail == '04':
                print(detail, '读取若干个记录型对象属性请求 (GetRequestRecordList) ')
            elif detail == '05':
                print(detail, '读取分帧响应的下一个数据块请求 (GetRequestNext) ')
            elif detail == '06':
                print(detail, '读取一个对象属性的 MD5 值 (GetRequestMD5) ')
            else:
                print('ERROR:05??')
        elif num == '85':
            print(num, '读取响应', end=' ')
            if detail == '01':
                print(detail, '读取一个对象属性的响应(GetResponseNormal) ')
            elif detail == '02':
                print(detail, '读取若干个对象属性的响应 (GetResponseNormalList) ')
            elif detail == '03':
                print(detail, '读取一个记录型对象属性的响应 (GetResponseRecord) ')
                self.A_ResultRecord_SEQUENCE(APDU[3:])

            elif detail == '04':
                print(detail, '读取若干个记录型对象属性的响应 (GetResponseRecordList) ')
            elif detail == '05':
                print(detail, '分帧响应一个数据块 (GetResponseNext) ')
            elif detail == '06':
                print(detail, '读取一个对象属性的 MD5 值的响应 (GetResponseMD5) ')
            else:
                print('ERROR:85??')
        elif num == '06':
            print(num, '设置请求')
        elif num == '86':
            print(num, '设置响应')
        elif num == '07':
            print(num, '操作请求')
        elif num == '87':
            print(num, '操作响应')
        elif num == '08':
            print(num, '上报回应')
        elif num == '88':
            print(num, '上报请求')

    def A_ResultRecord_SEQUENCE(self, remain):
        OAD = int(remain[0] + remain[1])
        self.OAD_SEQUENCE(OAD, remain[2], remain[3])
        returnvalue = self.DataResponse_CHOICE(self.RCSD(remain[4], remain[5:]))
        if not returnvalue:
            print('A_ResultRecord_SEQUENCE ERROR')
        returnvalue = self.GetRecodeResult(returnvalue)
        print('A_ResultRecord_SEQUENCE & Left:', returnvalue)

    def GetRecodeResult(self, args):
        type = args[0]
        if type == '01':
            returnvalue = self.SequenceOfARecordRow_SEQUENCE(args[1:])
            return returnvalue

    def RCSD(self, remain_len, args):
        lens = int(remain_len, 16)
        print('lens', lens)
        self.RCSDLENS = lens
        while lens > 0:
            print('RCSD after', args)
            args = self.CSD_CHOICE(args)
            lens -= 1
            print('RCSD before', args)
        return args

    def CSD_CHOICE(self, args):
        type = args[0]
        if type == '00':
            print('CSD:', type)
            OAD = args[1] + args[2]
            self.OAD_SEQUENCE(OAD, args[3], args[4])
            if args == []:
                print('CSD_CHOICE is NULL')
            self.CSD_TYPE = 0
            return args[5:]
        elif type == '01':
            value = self.ROAD(args[1:])
            if value == []:
                print('CSD_CHOICE is NULL')
            return value
        else:
            print('ERRORS:CSD_CHOICE')

    def ROAD(self, args):
        OAD = int(args[0] + args[1])
        self.OAD_SEQUENCE(OAD, args[2], args[3])
        len = int(args[4], 16)
        again = args[5:]
        while len > 0:
            len -= 1
            OAD = again[0] + again[1]
            self.OAD_SEQUENCE(OAD, again[2], again[3])
            again = again[4:]
        if not again:
            print('ROAD is NULL')
        return again

    def OAD_SEQUENCE(self, OI, unsigned1, unsigned2):
        unsigned11 = Comm.dec2bin(int(unsigned1)).zfill(8)  # 特征值
        unsigned11 = int(unsigned11[0:4], 10)
        unsigned1 = '属性 ' + unsigned1[1]
        OIcount = str(OI)[0]
        if 5 <= int(OIcount) <= 7:
            for child in self.root[0]:
                for childern in child:  # Table
                    for grandchildern in childern:  # Row
                        Data = grandchildern.find("Data")
                        try:
                            if Data.text == str(OI):
                                print(Data.text, end=' ')

                                global i
                                i = 0
                            i += 1
                            if i == 3:
                                print(Data.text, end=' ')

                                global x
                                x += 1
                            if x == 1:
                                try:
                                    if Data.text[3] == unsigned1[3]:
                                        print(Data.text, '特征:', unsigned11, '索引:', unsigned2)
                                        x += 1
                                    # key.append(Data.text)
                                except:
                                    pass
                        except:
                            pass
        if int(OIcount) < 5:
            for child in self.root[1]:
                for childern in child:  # Table
                    for grandchildern in childern:  # Row
                        Data = grandchildern.find("Data")
                        try:
                            if Data.text == str(OI).zfill(4):
                                print(Data.text, unsigned1, end=' ')

                                global ii
                                ii = 0
                            ii += 1
                            if ii == 2:
                                print('class id :', Data.text)
                                Class_id(Data.text, unsigned1[3])
                            if ii == 3:
                                print(Data.text, '特征:', unsigned11, '索引:', unsigned2)
                                key.append(Data.text)
                        except:
                            pass

    def DataResponse_CHOICE(self, message):

        if message[0] == '00':
            self.DAR(message[1])
        elif message[0] == '01':  # 数据
            returnvalue = self.SequenceOfARecordRow_SEQUENCE(message[1:])
            if returnvalue == []:
                print('DataResponse_CHOICE is NULL')
            return returnvalue
        else:
            print('ERROR:DataResponse_CHOICE out of range')

    def SequenceOfARecordRow_SEQUENCE(self, len_within_args):
        len1 = int(len_within_args[0], 16)
        try:
            if self.CSD_TYPE == 0:
                len1 = len1 * self.RCSDLENS
        finally:
            if len1 == 0:
                print('长度为0')
                global mark
                mark = 1
                return len_within_args[1:]
            len_within_args = len_within_args[1:]
            while len1 > 0:
                remain = self.Data(len_within_args[0], len_within_args[1:])
                len1 -= 1
                len_within_args = remain
            if not remain:
                print('SequenceOfARecordRow_SEQUENCE is NULL')
            return remain

    def DAR(self, number):
        if number == '00':
            print('成功')
        if number == '01':
            print('硬件失效')
        if number == '02':
            print('暂时失效')
        if number == '03':
            print('拒绝读写')
        if number == '04':
            print('对象未定义')
        if number == '05':
            print('对象接口类不符合')
        if number == '06':
            print('对象不存在')
        if number == '07':
            print('类型不匹配')
        if number == '08':
            print('越界')
        if number == '09':
            print('数据块不可用 ')
        if number == '10':
            print('分帧传输已取消')
        if number == '11':
            print('不处于分帧传输状态')
        if number == '12':
            print('块写取消')
        if number == '13':
            print('不存在块写状态')
        if number == '14':
            print('数据块序号无效')
        if number == '15':
            print('密码错/未授权')
        if number == '16':
            print('通信速率不能更改')
        if number == '17':
            print('年时区数超')
        if number == '18':
            print('日时段数超')
        if number == '19':
            print('费率数超')
        if number == '20':
            print('安全认证不匹配')
        if number == '21':
            print('重复充值')
        if number == '22':
            print('ESAM 验证失败')
        if number == '23':
            print('安全认证失败')
        if number == '24':
            print('客户编号不匹配 ')
        if number == '25':
            print('充值次数错误')
        if number == '26':
            print('购电超囤积')
        if number == '27':
            print('地址异常')
        if number == '28':
            print('对称解密错误')
        if number == '29':
            print('非对称解密错误 ')
        if number == '30':
            print('签名错误')
        if number == '31':
            print('电能表挂起')
        if number == '32':
            print('时间标签无效')
        if number == '33':
            print('请求超时')
        if number == '34':
            print('ESAM 的P1P2 不正确')
        if number == '35':
            print('ESAM 的 LC 错误')
        if number == '255':
            print('其它')

    def Data(self, DataDescribe, args):
        DataDescribe = str(int(DataDescribe, 16)).zfill(2)
        if DataDescribe == '00':
            print('NULL', DataDescribe)
            dic.append('NULL')
            return args

        elif DataDescribe == '01':
            print('array:', DataDescribe, end=' ')
            len1 = int(args[0], 16)
            lenori = len1
            args = args[1:]
            print('len:', len1)
            dic.append('len:' + str(lenori))
            while len1 > 0:
                args = self.Data(args[0], args[1:])
                len1 -= 1
                print('Data', args)

            return args
        elif DataDescribe == '02':
            print('structure: ', DataDescribe)
            len2 = int(args[0], 16)
            lenori = len2
            args = args[1:]
            dic.append('len:' + str(lenori))
            print('len:', len2)
            while len2 > 0:
                args = self.Data(args[0], args[1:])
                len2 -= 1
                print('Data', args)

            return args
        elif DataDescribe == '03':
            print('bool:', DataDescribe)
        elif DataDescribe == '04':
            print('bit-string:', DataDescribe)
            value = Comm.list2str(args[1:3])
            print('value', Comm.list2str(value))
            dic.append(value)
            return args[3:]
        elif DataDescribe == '05':
            print('double-long: ', DataDescribe)
            value = int(args[0] + args[1] + args[2] + args[3], 16)
            if value > 2147483647:
                value = Comm.Inverse_code(bin(value))
                value = int(value, 2) + 1
                value = -value
            print('value', value)
            dic.append(value)
            return args[4:]
        elif DataDescribe == '06':  # 4byte
            print('double-long-unsigned: ', DataDescribe)
            value = int(args[0] + args[1] + args[2] + args[3], 16)
            if value > 2147483647:
                value = Comm.Inverse_code(bin(value))
                value = int(value, 2) + 1
                value = -value
            print('value', value)
            dic.append(value)
            return args[4:]
        elif DataDescribe == '09':
            print('octet-string: ', DataDescribe)
        elif DataDescribe == '10':
            print('visible-string: ', DataDescribe)
        elif DataDescribe == '12':
            print('UTF8-string:', DataDescribe)
        elif DataDescribe == '15':
            print('integer:', DataDescribe)
        elif DataDescribe == '16':
            print('long: ', DataDescribe)
            value = int(args[0] + args[1], 16)
            if value > 32767:
                value = Comm.Inverse_code(bin(value))
                value = int(value, 2) + 1
                value = -value
            print('value', value)
            dic.append(value)
            return args[2:]
        elif DataDescribe == '17':
            print('unsigned:', DataDescribe)
        elif DataDescribe == '18':
            print('long-unsigned:', DataDescribe)
            value = int(args[0] + args[1], 16)
            if value > 32767:
                value = Comm.Inverse_code(bin(value))
                value = int(value, 2) + 1
                value = -value
            print('value', value)
            dic.append(value)
            return args[2:]
        elif DataDescribe == '20':
            print('long64: ', DataDescribe)
        elif DataDescribe == '21':
            print('long64-unsigned', DataDescribe)
        elif DataDescribe == '22':
            print('enum', DataDescribe)
        elif DataDescribe == '23':
            print('float32', DataDescribe)
        elif DataDescribe == '24':
            print('float64', DataDescribe)
        elif DataDescribe == '25':
            print('date_time', DataDescribe)
        elif DataDescribe == '26':
            print('date', DataDescribe)
        elif DataDescribe == '27':
            print('time', DataDescribe)
        elif DataDescribe == '28':
            print('date_time_s', DataDescribe)
            year = int(args[0] + args[1], 16)
            mouth = int(args[2], 16)
            day = int(args[3], 16)
            hour = int(args[4], 16)
            minute = int(args[5], 16)
            second = int(args[6], 16)
            datatime = str(year) + '年' + str(mouth) + '月' + str(day) + '日' + '   '+ str(hour) + ':' + str(minute) + ':' + str(
                second).zfill(2)
            print('时间为:', year, '年', mouth, '月', day, '日', hour, ':', minute, ':', second)
            print(args[7:])
            dic.append(datatime)
            return args[7:]
        elif DataDescribe == '80':
            print('OAD ', DataDescribe)
        elif DataDescribe == '82':
            print('ROAD ', DataDescribe)
        elif DataDescribe == '83':
            print('OMD ', DataDescribe)
        elif DataDescribe == '84':
            print('TI', DataDescribe)
        elif DataDescribe == '85':
            print('TSA', DataDescribe)
            value = args[0:8]
            print('TSA', value)
            dic.append(value)
            return args[8:]
        elif DataDescribe == '86':
            print('MAC', DataDescribe)
        elif DataDescribe == '87':
            print('RN', DataDescribe)
        elif DataDescribe == '88':
            print('Region', DataDescribe)
        elif DataDescribe == '89':
            print('Scaler_Unit ', DataDescribe)
        elif DataDescribe == '90':
            print('RSD', DataDescribe)
        elif DataDescribe == '91':
            print('CSD', DataDescribe)
        elif DataDescribe == '92':
            print('MS', DataDescribe)
        elif DataDescribe == '93':
            print('SID', DataDescribe)
        elif DataDescribe == '94':
            print('SID_MAC', DataDescribe)
        elif DataDescribe == '95':
            print('COMDCB', DataDescribe)
        elif DataDescribe == '96':
            print('RCSD', DataDescribe)
        else:
            print('ERROR on Data')


class ParsingMain(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = UI_MessageParsing.Ui_Dialog()
        self.ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.ui.pushButton_2.clicked.connect(self.GetText)

    def ShowMessage(self, dir, codes):
        number = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(number)
        if dir == 'L':
            self.ui.tableWidget.setItem(0, 0, QTableWidgetItem(codes))
        if dir == 'R':
            self.ui.tableWidget.setItem(0, 1, QTableWidgetItem(codes))

    def GetText(self):
        number = self.ui.tableWidget.rowCount()
        while 1:
            if number > 0:
                self.ui.tableWidget.removeRow(number)
                number -= 1
            else:
                break
        self.ui.tableWidget.removeRow(number)
        message = self.ui.textEdit.toPlainText()
        revalue = MessageParsing().Analysis_1(message.upper())
        if revalue:
            self.ShowMessage('L', revalue)
        global mark, key, dic
        if mark == 0:
            count = 0
            for y in key:
                global left, right
                left = []
                right = []
                left.append(y)
                number = self.ui.tableWidget.rowCount()
                self.ui.tableWidget.insertRow(number)
                self.ui.tableWidget.setItem(number, 0, QTableWidgetItem(y))
                big_time = 0
                small_time = 0
                a = 0
                b = 0
                while 1:
                    if big_time == 0 and small_time == 0:
                        if a == 0:
                            a += 1
                        elif a == 1:
                            break
                    if str(dic[count])[0:3] == 'len' and big_time == 0:
                        big_time = int(dic[count][4])
                        count += 1
                        continue
                    elif big_time > 0 and small_time == 0:
                        if str(dic[count])[0:3] == 'len':
                            small_time = int(dic[count][4])
                            if y == '正向有功最大需量' or y == '反向有功最大需量' or y == '组合无功 1 最大需量' or y == '组合无功 2 最大需量':
                                count += 1
                                continue
                            if b == 0:
                                b += 1
                            elif b == 1:
                                break
                            count += 1
                            continue
                        elif big_time > 0:
                            right.append(str(dic[count]))
                            number = self.ui.tableWidget.rowCount()
                            self.ui.tableWidget.insertRow(number)
                            xx = str(dic[count])
                            self.ui.tableWidget.setItem(number - 1, 1, QTableWidgetItem(xx))
                            count += 1
                            big_time -= 1
                            continue

                    if big_time > 0 and small_time > 0:
                        right.append(str(dic[count]))
                        number = self.ui.tableWidget.rowCount()
                        self.ui.tableWidget.insertRow(number)
                        xx = str(dic[count])
                        self.ui.tableWidget.setItem(number - 1, 1, QTableWidgetItem(xx))
                        count += 1
                        small_time -= 1
                        if small_time == 0:
                            big_time -= 1
                        continue

                    if big_time == 0 and small_time == 0:
                        right.append(str(dic[count]))
                        number = self.ui.tableWidget.rowCount()
                        self.ui.tableWidget.insertRow(number)
                        xx = str(dic[count])
                        self.ui.tableWidget.setItem(number - 1, 1, QTableWidgetItem(xx))
                        count += 1
                    continue

                print('输出:', left, '\n', right)
        else:
            for y in key:
                print(y, 'NULL')
        dic = []
        key = []


left = []
right = []
mark = 0
dic = []
key = []
