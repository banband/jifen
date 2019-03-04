# Project_wechat
#Some codings about Wechat
import os
import itchat
import time
import datetime
from aip import AipOcr
import time
from itchat.content import *
gname = '英雄杀'
context = ''
# 定义常量
APP_ID = '15654566'
API_KEY = 'QmxIgQQMvUAUSTZkMYvvYDr8'
SECRET_KEY = 'XUyGdkvSZ9OuapmvnDCDrsWEbOllO1tz'
aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)
options = {}
weiyiid = ''



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



def SendChatRoomsMsg(gname, context):
     # 获取所有群的相关信息，update=True表示信息更新
     myroom = itchat.get_chatrooms(update=True)
     # myroom = itchat.get_chatrooms()
     # print(myroom)
     global username
     # 搜索群名
     myroom = itchat.search_chatrooms(name=gname)
     # print(myroom.key())
     for room in myroom:
         # print(room)
         if room['NickName'] == gname:
             username = room['UserName']
             itchat.send_msg(context, username)
         else:
             print('No groups found')
# 监听是谁给我发消息


@itchat.msg_register([PICTURE], isGroupChat=True)
def text_reply(msg):

    # 打印获取到的信息
    #print(msg)
    wenjianjia = msg['ActualNickName']
    nowTime = datetime.datetime.now().strftime('%H%M%S')  # 现在

    mingzi = msg['ActualNickName']
    chuangjian = beifen()
    chuangjian.chuangjian(mingzi)
    #print(weiyiid)
    if msg['MsgId'] != weiyiid:

        #msg.download(mingzi + '\\' + nowTime + ".jpg")
        msg['Text'](mingzi + '\\' + nowTime + ".jpg")
        #time.sleep(5)
        filePath = mingzi + '\\' + nowTime + ".jpg"
        naha = beifen()
        naha.tongbu(msg['MsgId'])
        #print(weiyiid)
        def get_file_content(filePath):

            with open(filePath, 'rb') as fp:
                return fp.read()

        result = aipOcr.vehicleLicense(get_file_content(filePath), options)
        print(result)
        dangqianshijian = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if 'error_msg' in result:
            cuowutishi = "尊敬的%s您所发送的图片不清晰或者不是行驶证正本，请检查后重新发送。"%mingzi
            SendChatRoomsMsg(gname, cuowutishi)
        else:
            result_1 = result['words_result']
            haopai = result_1['号牌号码']['words']
            jiazihao = result_1['车辆识别代号']['words']
            tixing = "尊敬的%s您所预约的车辆号牌号码%s，车辆识别代号%s,信息已于%s记录。"%(mingzi,haopai,jiazihao,dangqianshijian)
            SendChatRoomsMsg(gname, tixing)
if __name__ == '__main__':

    itchat.auto_login(enableCmdQR=2, hotReload=True)
    SendChatRoomsMsg(gname, context)
    print(username)
    itchat.run()
