import pymssql
import random
import decimal
import time
import datetime
import subprocess
import configparser
import os


class MSSQL:
    def __init__(self,host,user,pwd,db,port):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db
        self.port = port

    def __GetConnect(self):
        if not self.db:
            raise(NameError,"没有设置数据库信息")
        self.conn = pymssql.connect(host=self.host,user=self.user,password=self.pwd,database=self.db,port=self.port,charset="utf8")
        cur = self.conn.cursor()
        if not cur:
            raise(NameError,"连接数据库失败")
        else:
            return cur

    def ExecQuery(self,sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()

        #查询完毕后必须关闭连接
        self.conn.close()
        return resList

    def ExecNonQuery(self,sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()

curpath = os.path.dirname(os.path.realpath(__file__))
cfgpath = os.path.join(curpath, "cfg.ini")
print(cfgpath) # cfg.ini的路径

# 创建管理对象
conf = configparser.ConfigParser()

# 读ini文件
conf.read(cfgpath, encoding="utf-8") # python3

# conf.read(cfgpath)  # python2

# 获取所有的section
sections = conf.sections()

#print(sections) # 返回list

items = conf.items('sqlxinxi')
#print(items) # list里面对象是元祖
host_1 = items[0][1]
#print(host_1)
user_1 = items[1][1]
#print(user_1)
pwd_1 = items[2][1]
#print(pwd_1)
db_1 = items[3][1]
#print(db_1)
port_1 = items[4][1]
#print(port_1)




while True:
    mima = input("请输入密码：")
    nowtime = int(datetime.datetime.now().strftime('%Y%m%d'))
    zhengquemima = str(nowtime)
    if mima == zhengquemima:
        print("*" * 40)
        print("车辆整备质量验证系统  V1.0")
        print("*" * 40)
        hphm_1 = input("请输入要检查车辆的号牌号码:黑")
        hphm = "黑" + str(hphm_1)
        print("*" * 40)
        print("输入的车牌号为：%s。正在查询·········"% hphm)
        print("*" * 40)
        ms = MSSQL(host=host_1,user=user_1,pwd=pwd_1,db=db_1,port=port_1)
        reslist = ms.ExecQuery("SELECT * FROM Data_ZBZL WHERE hphm = '%s'"% hphm)

        if reslist == []:
            print("请检查车辆号码%s是否输入错误（或者未称重），\n请等待3秒清屏后重新输入·········"%hphm)
            time.sleep(3)
            i = subprocess.call("cls", shell=True)
            continue
        reslist_1 = reslist[0]
        jylsh = reslist_1[1]
        reslist_2 = int(reslist_1[10])
        reslist_3 = random.randint(reslist_2 - 30, reslist_2 + 30)
        reslist_3 /= 10
        reslist_3 = '%d' %reslist_3
        reslist_3 = int(reslist_3) * 10
        hphm_3 = str(hphm)
        newsql = "update Data_ZBZL set jczczbzl='%s' where jylsh = '%s'" % (reslist_3,jylsh)
        ms.ExecNonQuery(newsql.encode('utf-8'))
        print("验证成功，%s 整备质量为：%skg，5秒后清理屏幕。"%(hphm,reslist_3))
        print("*" * 40)
        time.sleep(5)
        i = subprocess.call("cls", shell=True)
    else:
        print("密码输入错误，程序5秒后退出。")
        time.sleep(5)
        quit()