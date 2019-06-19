def list_append(list_):
    text = ''
    for i in list_:
        text = text + i
    return text

def check(code): #code->list
    if len(code) < 20:
        return 1
    lenth = int(code[2] + code[1], 16)  # 长度
    if len(code) >= lenth + 2:
        if code[lenth + 1] == '16':
            print('check granted')
            return 0
        else:
            return 1
    else:
        print('check denied')
        return 1

def DAR(number):
    if number == '00':
        print('成功')
        return '成功'
    if number == '01':
        print('硬件失效')
        return '硬件失效'
    if number == '02':
        print('暂时失效')
        return '暂时失效'
    if number == '03':
        print('拒绝读写')
        return '拒绝读写'
    if number == '04':
        print('对象未定义')
        return '对象未定义'
    if number == '05':
        print('对象接口类不符合')
        return '对象接口类不符合'
    if number == '06':
        print('对象不存在')
        return '对象不存在'
    if number == '07':
        print('类型不匹配')
        return '类型不匹配'
    if number == '08':
        print('越界')
        return '越界'
    if number == '09':
        print('数据块不可用 ')
        return '数据块不可用'
    if number == '10':
        print('分帧传输已取消')
        return '分帧传输已取消'
    if number == '11':
        print('不处于分帧传输状态')
        return '不处于分帧传输状态'
    if number == '12':
        print('块写取消')
        return '块写取消'
    if number == '13':
        print('不存在块写状态')
        return '不存在块写状态'
    if number == '14':
        print('数据块序号无效')
        return '数据块序号无效'
    if number == '15':
        print('密码错/未授权')
        return '密码错/未授权'
    if number == '16':
        print('通信速率不能更改')
        return '通信速率不能更改'
    if number == '17':
        print('年时区数超')
        return '年时区数超'
    if number == '18':
        print('日时段数超')
        return '日时段数超'
    if number == '19':
        print('费率数超')
        return '费率数超'
    if number == '20':
        print('安全认证不匹配')
        return '安全认证不匹配'
    if number == '21':
        print('重复充值')
        return '重复充值'
    if number == '22':
        print('ESAM 验证失败')
        return 'ESAM 验证失败'
    if number == '23':
        print('安全认证失败')
        return '安全认证失败'
    if number == '24':
        print('客户编号不匹配 ')
        return '客户编号不匹配'
    if number == '25':
        print('充值次数错误')
        return '充值次数错误'
    if number == '26':
        print('购电超囤积')
        return '购电超囤积'
    if number == '27':
        print('地址异常')
        return '地址异常'
    if number == '28':
        print('对称解密错误')
        return '对称解密错误'
    if number == '29':
        print('非对称解密错误 ')
        return '非对称解密错误'
    if number == '30':
        print('签名错误')
        return '签名错误'
    if number == '31':
        print('电能表挂起')
        return '电能表挂起'
    if number == '32':
        print('时间标签无效')
        return '时间标签无效'
    if number == '33':
        print('请求超时')
        return '请求超时'
    if number == '34':
        print('ESAM 的P1P2 不正确')
        return 'ESAM 的P1P2 不正确'
    if number == '35':
        print('ESAM 的 LC 错误')
        return 'ESAM 的 LC 错误'
    if number == '255':
        print('其它')
        return '其它'


def get_list_sum(list_):
    text = ''
    for i in list_:
        text = text + ' ' + i
    return text


def Inverse_code(codes):
    recode = ''
    for code in codes[2:]:
        if code == '1':
            code_ = '0'

        else:
            code_ = '1'
        recode = recode + code_
    return recode


def makestr(message):
    str_ = ''
    x = 0
    lenth = len(message)
    while lenth > 0:
        str_ = str_ + message[x:x + 2] + ' '
        x += 2
        lenth -= 2
    return str_


def makelist(message):
    list = []
    x = 0
    lenth = len(message)
    while lenth > 0:
        list.append(message[x:x + 2])
        x += 2
        lenth -= 2
    return list


def strto0x(context):
    # print('context:', context)
    context = [int(x, 16) for x in context]
    new_context = []
    while context:
        current_context = chr(context.pop())
        new_context.append(current_context)
    new_context.reverse()
    return new_context


def pppfcs16(fcs, p, length):
    fcstab = (
        0x0000, 0x1189, 0x2312, 0x329b, 0x4624, 0x57ad, 0x6536, 0x74bf,
        0x8c48, 0x9dc1, 0xaf5a, 0xbed3, 0xca6c, 0xdbe5, 0xe97e, 0xf8f7,
        0x1081, 0x0108, 0x3393, 0x221a, 0x56a5, 0x472c, 0x75b7, 0x643e,
        0x9cc9, 0x8d40, 0xbfdb, 0xae52, 0xdaed, 0xcb64, 0xf9ff, 0xe876,
        0x2102, 0x308b, 0x0210, 0x1399, 0x6726, 0x76af, 0x4434, 0x55bd,
        0xad4a, 0xbcc3, 0x8e58, 0x9fd1, 0xeb6e, 0xfae7, 0xc87c, 0xd9f5,
        0x3183, 0x200a, 0x1291, 0x0318, 0x77a7, 0x662e, 0x54b5, 0x453c,
        0xbdcb, 0xac42, 0x9ed9, 0x8f50, 0xfbef, 0xea66, 0xd8fd, 0xc974,
        0x4204, 0x538d, 0x6116, 0x709f, 0x0420, 0x15a9, 0x2732, 0x36bb,
        0xce4c, 0xdfc5, 0xed5e, 0xfcd7, 0x8868, 0x99e1, 0xab7a, 0xbaf3,
        0x5285, 0x430c, 0x7197, 0x601e, 0x14a1, 0x0528, 0x37b3, 0x263a,
        0xdecd, 0xcf44, 0xfddf, 0xec56, 0x98e9, 0x8960, 0xbbfb, 0xaa72,
        0x6306, 0x728f, 0x4014, 0x519d, 0x2522, 0x34ab, 0x0630, 0x17b9,
        0xef4e, 0xfec7, 0xcc5c, 0xddd5, 0xa96a, 0xb8e3, 0x8a78, 0x9bf1,
        0x7387, 0x620e, 0x5095, 0x411c, 0x35a3, 0x242a, 0x16b1, 0x0738,
        0xffcf, 0xee46, 0xdcdd, 0xcd54, 0xb9eb, 0xa862, 0x9af9, 0x8b70,
        0x8408, 0x9581, 0xa71a, 0xb693, 0xc22c, 0xd3a5, 0xe13e, 0xf0b7,
        0x0840, 0x19c9, 0x2b52, 0x3adb, 0x4e64, 0x5fed, 0x6d76, 0x7cff,
        0x9489, 0x8500, 0xb79b, 0xa612, 0xd2ad, 0xc324, 0xf1bf, 0xe036,
        0x18c1, 0x0948, 0x3bd3, 0x2a5a, 0x5ee5, 0x4f6c, 0x7df7, 0x6c7e,
        0xa50a, 0xb483, 0x8618, 0x9791, 0xe32e, 0xf2a7, 0xc03c, 0xd1b5,
        0x2942, 0x38cb, 0x0a50, 0x1bd9, 0x6f66, 0x7eef, 0x4c74, 0x5dfd,
        0xb58b, 0xa402, 0x9699, 0x8710, 0xf3af, 0xe226, 0xd0bd, 0xc134,
        0x39c3, 0x284a, 0x1ad1, 0x0b58, 0x7fe7, 0x6e6e, 0x5cf5, 0x4d7c,
        0xc60c, 0xd785, 0xe51e, 0xf497, 0x8028, 0x91a1, 0xa33a, 0xb2b3,
        0x4a44, 0x5bcd, 0x6956, 0x78df, 0x0c60, 0x1de9, 0x2f72, 0x3efb,
        0xd68d, 0xc704, 0xf59f, 0xe416, 0x90a9, 0x8120, 0xb3bb, 0xa232,
        0x5ac5, 0x4b4c, 0x79d7, 0x685e, 0x1ce1, 0x0d68, 0x3ff3, 0x2e7a,
        0xe70e, 0xf687, 0xc41c, 0xd595, 0xa12a, 0xb0a3, 0x8238, 0x93b1,
        0x6b46, 0x7acf, 0x4854, 0x59dd, 0x2d62, 0x3ceb, 0x0e70, 0x1ff9,
        0xf78f, 0xe606, 0xd49d, 0xc514, 0xb1ab, 0xa022, 0x92b9, 0x8330,
        0x7bc7, 0x6a4e, 0x58d5, 0x495c, 0x3de3, 0x2c6a, 0x1ef1, 0x0f78)
    i = 0
    while length:
        length -= 1
        fcs = (fcs >> 8) ^ fcstab[(fcs ^ ord(p[i])) & 0xff]
        i += 1
    return fcs ^ 0xffff


def list2str(message):
    text = ''
    i = 0
    lenth = len(message)
    while lenth > 0:
        text = text + message[i]
        i += 1
        lenth -= 1
    return text


def dec2bin(num):
    l = []
    if num < 0:
        return '-' + dec2bin(abs(num))
    while True:
        num, remainder = divmod(num, 2)
        l.append(str(remainder))
        if num == 0:
            return ''.join(l[::-1])


def BuildMessage(APDU, SA_address, stat='dan'):
    print('sa',SA_address)
    if SA_address == []:
        message_full = '0'
    else:
        C = '43'
        if stat == 'zu':
            SA_sign = '8'
        else:
            SA_sign = '0'
        CA = '00'
        APDUlist = makelist(APDU.replace(' ', ''))
        SA_address_nospace = list2str(SA_address)
        lenth = int(dec2bin(len(SA_address)), 2)
        SA_sign = SA_sign + str(lenth - 1)
        Total_length = hex(5 + lenth + 3 + len(APDUlist) + 3 - 2)[2:].zfill(4)
        lenth1 = Total_length[2:]
        lenth2 = Total_length[0:2]
        # print('Comm line:126', lenth1, lenth2, C, SA_sign, SA_address_nospace, CA)
        Head = strto0x(makelist(lenth1 + lenth2 + C + SA_sign + SA_address_nospace + CA))
        HCS = str(hex(pppfcs16(0xffff, Head, len(Head)))).zfill(4)[2:]
        if len(HCS) == 3:
            HCS = '0' + HCS
        HCS = HCS[2:] + HCS[0:2]
        message = strto0x(makelist(lenth1 + lenth2 + C + SA_sign + SA_address_nospace + CA + HCS + APDU.replace(' ', '')))
        FCS = hex(pppfcs16(0xffff, message, len(message))).zfill(4)[2:]
        if len(FCS) == 3:
            FCS = '0' + FCS
        FCS = FCS[2:] + FCS[0:2]
        message_full = '68' + lenth1 + lenth2 + C + SA_sign + SA_address_nospace + CA + HCS + APDU.replace(' ', '') + FCS + '16'
        print('组成报文:', message_full)
    return message_full


class Analysis:
    def start698(self, code):
        self.code = self.clear(makelist(code))
        if self.code == 'ERROR':
            print('698解析错误,ERROR')
        else:
            lenth = int(self.code[2] + self.code[1], 16)  # exception 68 16
            ctrlcode = self.ctrlc_1(dec2bin(int(self.code[3], 16)).zfill(2))
            code_remain = self.code[4:]
            SA_len_num = self.SASign(dec2bin(int(code_remain[0], 16)).zfill(8))
            self.SA_len = code_remain[1:1 + SA_len_num]
            global SA_add
            SA_add = self.SA_len
            CA = code_remain[1 + SA_len_num:][0]
            HCS = code_remain[1 + SA_len_num:][1] + code_remain[1 + SA_len_num:][2]
            APDU = code_remain[1 + SA_len_num:][3:-3]
            print('APDU:', APDU)
            return self.Information(APDU[0],APDU[1],APDU)

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
                if list2str(APDU[3:7]) == '40010200':
                    add = list2str(APDU[10:16])
                    print('add',add)
                    return '地址为:{}'.format(add)
            elif detail == '02':
                print(detail, '读取若干个对象属性的响应 (GetResponseNormalList) ')
            elif detail == '03':
                print(detail, '读取一个记录型对象属性的响应 (GetResponseRecord) ')
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
            if detail == '01':
                print(detail, '设置一个对象属性的确认信息响应')
                return DAR(APDU[7])
        elif num == '07':
            print(num, '操作请求')
        elif num == '87':
            print(num, '操作响应')
            if detail == '01':
                print(detail, '操作一个对象方法的确认信息响应')
                return DAR(APDU[7])
        elif num == '08':
            print(num, '上报回应')
        elif num == '88':
            print(num, '上报请求')
        return 0


    def clear(self, code):
        while 1:
            if not code:
                code = 'ERROR'
                break
            if code[0] == '68':
                break
            else:
                del code[0]
        return code

    def ctrlc_1(self, num):
        if num[0] == '0' and num[1] == '0':
            # print(num, 'DIR=0 PRM=0 客户机对服务器上报的响应')
            return 0
        elif num[0] == '0' and num[1] == '1':
            # print(num, 'DIR=0 PRM=1 客户机发起请求')
            return 1
        elif num[0] == '1' and num[1] == '0':
            # print(num, 'DIR=1 PRM=0 服务器发起上报')
            return 2
        else:
            # print(num, 'DIR=1 PRM=1 服务器对客户机请求的响应')
            return 3

    def SASign(self, num):
        numadd = int(str(num[0] + num[1]), 2)
        if numadd == 0:
            # print('0 单地址')
            pass
        elif numadd == 1:
            # print('1 通配地址')
            pass
        elif numadd == 2:
            print('2 组地址')
        else:
            print('3 广播地址')
        # print(' 逻辑地址: ', num[2], num[3])
        numadd1 = int(num[4:], base=2)
        # print('地址长度 N: ', numadd1+1)
        return numadd1 + 1


def SetSA(SA):
    global SA_add
    SA_add = SA

def re_sa():
    global SA_add
    return SA_add

SA_add = []
