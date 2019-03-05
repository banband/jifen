from wxpy import *
import datetime
import time
from aip import AipOcr
import os
import pymysql


weiyiid = ''
class sql_mokuai(object):

    def charu(self,id_1,xingming_1,chehao_1,leixing_1,jiancezhan_1,jifen_1,yuyueshijian_1,jianceshijian_1,zhaopianlujing_1):

        self.id = id_1
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
        # SQL 插入语句
        sql = "INSERT INTO yuyue(id, xingming, chehao, leixing, jiancezhan, " \
              "jifen, yuyueshijian, jianceshijian,zhaopianlujing)VALUES ('%s','%s','%s','%s','" \
              "%s','%s','%s','%s','%s')" %(self.id,self.xingming, self.chehao, self.leixing,
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

    def chaxun(self,chehao_1,cheliangleixing_1):
        self.chehao = chehao_1
        self.cheliangleixing = cheliangleixing_1
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "sa", "mysql")

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 查询语句
        sql = "SELECT * FROM yuyue WHERE chehao = '%s' and leixing = '%s'" % (self.chehao,self.cheliangleixing)
        #print(sql)
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

# 将老板的消息转发到文件传输助手
@bot.register(company_group)
def forward_boss_message(msg):
    print(msg.raw)
    if '#' in msg.raw['Text']:
        print("包含#号")



    if msg.raw['MsgId'] != weiyiid:
        naha = beifen()
        naha.tongbu(msg.raw['MsgId'])
        nowTime = datetime.datetime.now().strftime('%H%M%S')
        yonghu = msg.raw['ActualNickName']
        # print(msg)
        # print(yonghu)
        msg.get_file('照片\\'+ yonghu + nowTime +'.jpg')
        a = '照片\\'+ yonghu + nowTime +'.jpg'
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
                    tixing = "@%s  您所预约的车辆号牌号码%s，车辆识别代号%s,信息已于%s记录。" % (yonghu, haopai, jiazihao, dangqianshijian)
                    # print(tixing)
                    company_group.send(tixing)
                    cc.charu("",yonghu,haopai,cheliangleixing,"致远","",dangqianshijian,"",a)
                else:
                    # print("chonggfule")
                    # print(paichong[0])
                    tixing_2 = "@%s  您所预约的车辆号牌号码%s，于%s 已经被 %s 预约，请勿重复预约，如有异议请联系客服处理。" % (yonghu, paichong[0][2], paichong[0][6], paichong[0][1])
                    company_group.send(tixing_2)






# 堵塞线程






embed()