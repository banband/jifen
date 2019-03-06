from wxpy import *
import datetime
import time
from aip import AipOcr
import os
import pymysql


weiyiid = ''
class sql_mokuai(object):
    def charu(self,xingming_1,chehao_1,leixing_1,jiancezhan_1,jifen_1,yuyueshijian_1,jianceshijian_1,zhaopianlujing_1):
        self.xingming = xingming_1
        self.chehao = chehao_1
        self.leixing = leixing_1
        self.jiancezhan = jiancezhan_1
        self.jifen = jifen_1
        self.yuyueshijian= yuyueshijian_1
        self.jianceshijian = jianceshijian_1
        self.zhaopianlujing = zhaopianlujing_1
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "sa", "mysql")

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        sql = "INSERT INTO yuyue(xingming, chehao, leixing, jiancezhan, " \
              "jifen, yuyueshijian, jianceshijian,zhaopianlujing)VALUES ('%s','%s','%s','" \
              "%s','%s','%s','%s','%s')" % (self.xingming, self.chehao, self.leixing,
                                      self.jiancezhan, self.jifen, self.yuyueshijian,self.jianceshijian,self.zhaopianlujing)
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()

        except:
            # 如果发生错误则回滚
            db.rollback()
            print("失败")

        # 关闭数据库连接
        db.close()

    def gengxin(self, xingming_1, chehao_1):
        self.xingming = xingming_1
        self.chehao = chehao_1

        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "sa", "mysql")

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        sql = "UPDATE yuyue SET xingming='%s' WHERE chehao = '%s'" %(self.xingming,self.chehao)
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()

        except:
            # 如果发生错误则回滚
            db.rollback()
            print("失败")

        # 关闭数据库连接
        db.close()

    def chaxun(self,chehao_1,cheliangleixing_1):
        self.chehao = chehao_1
        self.cheliangleixing = cheliangleixing_1
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "sa", "mysql")

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 查询语句
        sql = "SELECT * FROM yuyue WHERE chehao = '%s' and leixing = '%s'" % (self.chehao,self.cheliangleixing)
        print(sql)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            #print(results)
            return results

                # 打印结果
        except:
            print("Error: unable to fetch data")

        # 关闭数据库连接
        db.close()
    def chaxun_1(self,chehao_1,):
        self.chehao = chehao_1
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "sa", "mysql")

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 查询语句
        sql = "SELECT * FROM yuyue WHERE chehao = '%s'" % self.chehao
        print(sql)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            #print(results)
            return results

                # 打印结果
        except:
            print("Error: unable to fetch data")

        # 关闭数据库连接
        db.close()

    def chaxundangri(self, xingming):
        self.xingming = xingming
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "sa", "mysql")

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        dangqianshijian = time.strftime("%Y-%m-%d ", time.localtime())
        # SQL 查询语句
        sql = "SELECT * FROM yuyue WHERE xingming = '%s' and yuyueshijian >= '%s00:00:00' and yuyueshijian <= '%s23:59:59'" % (self.xingming,dangqianshijian,dangqianshijian)
        print(sql)

        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            # print(results)
            return results

            # 打印结果
        except:
            print("Error: unable to fetch data")

        # 关闭数据库连接
        db.close()
    def shanchu(self,chehao):
        self.chehao = chehao

        db = pymysql.connect("localhost", "root", "sa", "mysql")

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 查询语句
        sql = "DELETE FROM yuyue WHERE chehao = '%s'" %self.chehao
        print(sql)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            db.commit()
            # print(results)

            # 打印结果
        except:
            # 如果发生错误则回滚
            db.rollback()
            print("失败")

        # 关闭数据库连接
        db.close()


class beifen(object):
    def chuangjian(self,lujing):
        self.lujing = lujing
        a = os.path.exists(self.lujing)

        if a == False:
            os.mkdir(self.lujing)
        return a
    def tongbu(self,msgid):
        self.msgid =msgid
        global weiyiid
        weiyiid = self.msgid

class baiduai(object):
    def shibei(self,filepath):
        # 定义常量
        APP_ID = '15654566'
        API_KEY = 'QmxIgQQMvUAUSTZkMYvvYDr8'
        SECRET_KEY = 'XUyGdkvSZ9OuapmvnDCDrsWEbOllO1tz'

        # 初始化AipFace对象
        aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)

        # 读取图片
        self.filePath = filepath

        def get_file_content(filepath):
            with open(self.filePath, 'rb') as fp:
                return fp.read()

        options = {}

        result = aipOcr.vehicleLicense(get_file_content(self.filePath), options)
        return result

bot = Bot(cache_path=True, console_qr=False)

# 定位公司群
company_group = ensure_one(bot.groups().search('英雄杀'))

company_group.send('机器人已启动')

@bot.register(company_group,TEXT)
def forward_boss_message(msg):
    yonghu = msg.raw['ActualNickName']
    mingling = str.upper(msg.raw['Text'])
    print(mingling)
    if "预约" in mingling:
        yuyue = mingling[2:]
        cheliangleixing = ""
        if len(yuyue) == 7 and u'\u4e00' <= yuyue[0] <= u'\u9fff':

            print("zhongwen")

            cc = sql_mokuai()
            paichong = cc.chaxun(yuyue, cheliangleixing)
            if paichong == ():
                dangqianshijian = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                tixing = "@%s  您所预约的车辆号牌号码%s，信息已于%s记录,预约成功。" % (yonghu, yuyue, dangqianshijian)
                # print(tixing)
                company_group.send(tixing)
                cc.charu(yonghu, yuyue, cheliangleixing, "", "", dangqianshijian, "", '')
            else:
                # print("chonggfule")
                # print(paichong[0])
                tixing_2 = "@%s  您所预约的车辆号牌号码%s，于%s 已经被 %s 预约，请勿重复预约，如有异议请联系客服处理。" % (
                yonghu, paichong[0][2], paichong[0][6], paichong[0][1])
                company_group.send(tixing_2)

        else:
            tixing_3 = "@%s  您所输入信息有误，请参照示例：预约黑K12345 或 预约黑K1234挂，重新输入。" % yonghu
            company_group.send(tixing_3)
    if "查询" in mingling:
        cx = sql_mokuai()
        cx = cx.chaxundangri(yonghu)
        chaxunbiao = []
        for i in cx:
            chaxunbiao.append(i[2])
        suliang = (len(chaxunbiao))
        tixing_4 = "@%s  您今日预约车辆%s台次，车号:%s，请再接再厉！。" % (yonghu,suliang,chaxunbiao)
        company_group.send(tixing_4)
    if "帮助" in mingling:
        tixing_5 = "@%s你好，普通员工命令：1、查询  --查询当日预约车辆数量及车号。   管理员命令：1、更改黑K12345高显超 --将黑K12345更改为高显超名下，2、删除黑K12345 --将黑K12345车号删除。" % yonghu
        company_group.send(tixing_5)
    if "更改" in mingling:
        genggai = sql_mokuai()
        chaxun = genggai.chaxun_1(mingling[2:9])
        if chaxun == ():
            tixing_7 = "@%s你好，没有查询到%s，请核对后重新发送。" % (yonghu, mingling[2:9])
            company_group.send(tixing_7)
        else:
            genggai.gengxin(mingling[9:],mingling[2:9])
            tixing_8 = "@%s你好，%s，已更名为%s。" % (yonghu, mingling[2:9],mingling[9:])
            company_group.send(tixing_8)

    if "删除" in mingling:
        shanchu = sql_mokuai()
        chaxun = shanchu.chaxun_1(mingling[2:])
        if chaxun == ():
            tixing_6 = "@%s你好，没有查询到%s，请核对后重新发送。" % (yonghu,mingling[2:])
            company_group.send(tixing_6)
        else:
            shanchu.shanchu(mingling[2:])
            tixing_7 = "@%s你好，%s，已经删除成功。" % (yonghu, mingling[2:])
            company_group.send(tixing_7)














# 将老板的消息转发到文件传输助手
@bot.register(company_group,PICTURE)
def forward_boss_message(msg):

    if msg.raw['MsgId'] != weiyiid:
        print(msg.raw)
        naha = beifen()
        naha.tongbu(msg.raw['MsgId'])
        nowTime = datetime.datetime.now().strftime('%H%M%S')
        yonghu = msg.raw['ActualNickName']
        # print(msg)
        # print(yonghu)
        msg.get_file('D:\github\weixin\照片\\'+ yonghu + nowTime +'.jpg')
        a = 'D:\github\weixin\照片\\'+ yonghu + nowTime +'.jpg'
        b = baiduai()
        result = b.shibei(a)
        # print(result)
        if 'error_msg' in result:
            cuowutishi = "@%s  您所发送的图片不清晰或者不是行驶证正本，请检查后重新发送。"%yonghu
            company_group.send(cuowutishi)
        else:
            result_1 = result['words_result']
            print(result_1)
            haopai = result_1['号牌号码']['words']
            cheliangleixing = result_1['车辆类型']['words']
            if len(haopai) != 7:
                cuowutishi = "@%s  您所发送的图片不清晰或者不是行驶证正本，请检查后重新发送。" % yonghu
                company_group.send(cuowutishi)

            else:
                cc = sql_mokuai()
                paichong = cc.chaxun(haopai,cheliangleixing)
                # print(paichong)
                if paichong == ():
                    jiazihao = result_1['车辆识别代号']['words']
                    dangqianshijian = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    tixing = "@%s  您所预约的车辆号牌号码%s，车辆识别代号%s,信息已于%s记录，预约成功。" % (yonghu, haopai, jiazihao, dangqianshijian)
                    # print(tixing)
                    company_group.send(tixing)
                    cc.charu(yonghu,haopai,cheliangleixing,"","",dangqianshijian,"",a)
                else:
                    # print("chonggfule")
                    # print(paichong[0])
                    tixing_2 = "@%s  您所预约的车辆号牌号码%s，于%s 已经被 %s 预约，请勿重复预约，如有异议请联系客服处理。" % (yonghu, paichong[0][2], paichong[0][6], paichong[0][1])
                    company_group.send(tixing_2)






# 堵塞线程






embed()