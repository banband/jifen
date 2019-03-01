# Project_wechat
#Some codings about Wechat

import itchat
import time
from itchat.content import *
gname = '英雄杀'
context = '这是一条我设定群的群发消息，微信正式处于托管状态。大家可以忽略'
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
@itchat.msg_register([itchat.content.PICTURE], isGroupChat=True)
def text_reply(msg):
     # 打印获取到的信息
     print(msg)
     msg['Text'](msg['FileName'])
     itchat.send("您发送了：\'%s\'\n微信目前处于python托管，你的消息我会转发到手机，谢谢" %
                 (msg['Text']), toUserName=msg['FromUserName'])
# @itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
# def download_files(msg):
#     #msg.download(msg['FileName'])   #这个同样是下载文件的方式
#     msg['Text'](msg['FileName'])      #下载文件
#     #将下载的文件发送给发送者
#     itchat.send('@%s@%s' % ('img' if msg['Type'] == 'Picture' else 'fil', msg["FileName"]), msg["FromUserName"])
itchat.auto_login(enableCmdQR=True, hotReload=True)
SendChatRoomsMsg(gname, context)
itchat.run()
