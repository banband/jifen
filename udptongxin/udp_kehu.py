# encoding:utf-8
import datetime
from  decimal import Decimal
import socket
import time
import pymssql
import configparser
import os
import ast

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
#print

fuwuqi = conf.items('fuwuqi')
benji = conf.items('benji')
#print(fuwuqi)

def send_msg(udp_socket,a,sst):

    dest_ip = str(fuwuqi[0][1])
    dest_port = int(fuwuqi[1][1])
    send_data = '{"chehao":"%s","jifen":"%s"}' % (sst, a)

    print('sss%s'%send_data)
    udp_socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))



def recv_msg(udp_socket):
    recv_data = udp_socket.recvfrom(1024)
    print("%s:%s" % (str(recv_data[1]), recv_data[0].decode("utf-8")))
    ss = recv_data[0].decode("utf-8")
    #time.sleep(3)
    print(ss)
    ss_dict = ast.literal_eval(ss)
    print(ss_dict)
    sst = ss_dict['chehao']
    shijian = ss_dict["yuyueshijian"][:10] + ' 23:59:59'
    print(shijian)
    ms = MSSQL(host=host_1, user=user_1, pwd=pwd_1, db=db_1, port=port_1)
    reslist = ms.ExecQuery("SELECT * FROM Data_Info WHERE BD7 = '%s' and BD3 > '%s'" % (sst,shijian))
    print(reslist)
    xiaoqiyou = 300
    xiaocaiyou = 400
    zhongkeqiyou = 360
    zhongkecaiyou = 510
    dakeqiyou = 420
    dakecaiyou = 570
    zhonghuoqiyou = 450
    zhonghuocaiyou = 650
    dahuoqiyou = 500
    dahuocaiyou = 700
    for i in reslist:
        a = 0

        if '安全检测' in i:
            print("在这里")
            daxiao = i[16][:2]
            chexing = i[16][-2:]
            ranliao = i[19]
            print("%s   %s     %s " % (daxiao, chexing, ranliao))
            if daxiao == '小型' or daxiao == '轻型' or daxiao == '微型' or daxiao == '三轮':

                if ranliao == '汽油':
                    a = xiaoqiyou
                if ranliao == '柴油':
                    a = xiaocaiyou
            if daxiao == '中型':
                if chexing == '客车':
                    if ranliao == '汽油':
                        a = zhongkeqiyou
                    if ranliao == '柴油':
                        a = zhongkecaiyou
                if chexing == '货车' or chexing == '引车' or chexing == '业车':
                    if ranliao == '汽油':
                        a = zhonghuoqiyou
                    if ranliao == '柴油':
                        a = zhonghuocaiyou
            if daxiao == '大型' or daxiao == '重型':
                if chexing == '客车':
                    if ranliao == '汽油':
                        a = dakeqiyou
                    if ranliao == '柴油':
                        a = dakecaiyou
                if chexing == '货车' or chexing == '引车' or chexing == '业车':
                    if ranliao == '汽油':
                        a = dahuoqiyou
                    if ranliao == '柴油':
                        a = dahuocaiyou
        else:
            print('没有')









    if reslist == []:
        a = '0'
    send_msg(udp_socket,a,sst)


def main():

    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    udp_socket.bind(("", int(benji[0][1])))


    while True:
        #send_msg(udp_socket)
        recv_msg(udp_socket)


if __name__ == '__main__':

    main()