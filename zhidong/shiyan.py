import re
import random
import configparser
import os
import time
import subprocess

biaodingweizhi = "Data\标定数据\\"
beifenweizhi = "Data\标定数据\标定备份\\"
jianchalujing = "Data\标定数据\\"
dangqianweizhi = ""

class congkai(object):
    def guanbidakai(self):
        os.system(r'taskkill /F /IM PJCXMain.exe')
        time.sleep(2)
        subprocess.Popen(r'PJCXMain.exe')

class beifen(object):
    def chuangjian(self,lujing,newlujing):
        self.lujing = lujing
        self.newlujing = newlujing
        a = os.path.exists(jianchalujing+"标定备份")
        if a == False:
            os.mkdir(jianchalujing + "标定备份")
        with open(self.lujing,"r",encoding="utf-8") as q_s:
            lines = q_s.readlines()
        with open(self.newlujing, "w", encoding="utf-8") as j_w:
            for i in lines:
                j_w.write(i)

class gongju(object):
    def xieruyuanshi(self,lujing,newlujing):
        self.lujing = lujing
        self.newlujing = newlujing
        with open(self.newlujing, "r",encoding="utf-8") as l_s:
            lines = l_s.readlines()
        with open(self.lujing, "w", encoding="utf-8") as t_w:
            for i in lines:
                t_w.write(i)

class jisuan(object):
    def xierubianliang(self,lujing,baifenbi,libuchang):
        self.baifenbi = baifenbi
        self.lujing = lujing
        self.libuchang = libuchang
        with open(self.lujing,"r",encoding="utf-8") as f:
            lines = f.readlines()
        with open(self.lujing,"w",encoding="utf-8") as f_w:
            for i in lines:
                d = re.split(r";",i)
                e = float(d[2])
                print(e)
                x = (e / int(self.baifenbi)) * int(self.libuchang) * 0.8
                x = str('%.1f'%x)
                line = i.replace(str(e),x)
                f_w.write(line)

if __name__ == '__main__':
    dangqianweizhi = __file__
    print("使用说明：\n"
          "1、本软件需放在检测系统根目录下运行，自动识别《参数配置.ini》文件下参数识别检测线类型，\n"
          "《参数配置.ini》下要求[参数]和标定数据文件夹下都需含有左力通道、右力通道、平板前左力通道、平板前右力通道、平板后左力通道、平板后右力通道。\n"
          "《参数配置.ini》[工位设定]下要求含有平板= 项目，《参数配置.ini》下每个子项目下不能含有重名字典。如不符合可能造成软件崩溃。\n"
          "2、本软件根据运行环境自动选择是否开启自动关闭、打开主控功能。\n"
          "3、本软件可以自动识别滚筒线、平板线、左右轮是否通道相同，根据识别后的参数自动选择运行模式。\n"
          "4、本软件会在打开的同时在标定数据文件夹下创建标定数据备份，请在关闭软件之前空按回车将备份还原，\n"
          "软件每次打开都会覆盖备份，请将主控程序备份妥善保管，以免因为不当的操作或此软件BUG造成文件丢失。\n"
          "5、此软件无法运行在win7系统以下运行，如果要在win7以下运行请选择“曲线救国模式：工位机开启文件夹共享，将此软件在win7以上系统上远程执行。”")
    input("6、确认已经认真阅读以上4条，进入软件请按回车键，如造成崩溃，请按照以上4条修改参数配置。")
    if dangqianweizhi[0] in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q",
                                 "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]:
        dangqianweizhi = 1
        print("*******软件运行在本机环境，已开启自动关闭主控、打开主控功能！")
    else:
        dangqianweizhi = 0
        print("*******软件运行在共享文件夹环境，已关闭自动关闭主控、打开主控功能！")

    config = configparser.ConfigParser(allow_no_value=True)
    config.read("参数配置.ini")
    zuolitongdao = config.get("参数", "左力通道")
    youlitongdao = config.get("参数", "右力通道")
    jiancexianleixing = config.get("工位设定", "平板")
    pingbanqianzuolitongdao = config.get("参数", "平板前左力通道")
    pingbanqianyoulitongdao = config.get("参数", "平板前右力通道")
    pingbanhouzuolitongdao = config.get("参数", "平板后左力通道")
    pingbanhouyoulitongdao = config.get("参数", "平板后右力通道")
    if jiancexianleixing == "1":
        print("这是一套平板线")
        beifen_1 = beifen()
        beifen_1.chuangjian(biaodingweizhi+"平板前左力标定.txt", beifenweizhi+"平板前左力标定备份.txt")
        beifen_1.chuangjian(biaodingweizhi+"平板前右力标定.txt", beifenweizhi+"平板前右力标定备份.txt")
        beifen_1.chuangjian(biaodingweizhi+"平板后左力标定.txt", beifenweizhi+"平板后左力标定备份.txt")
        beifen_1.chuangjian(biaodingweizhi+"平板后右力标定.txt", beifenweizhi+"平板后右力标定备份.txt")
        while True:
            if pingbanqianzuolitongdao == pingbanqianyoulitongdao and pingbanhouzuolitongdao == pingbanhouyoulitongdao:
                print("左右轮并行")
                zhidonglvq = input("请输入前轴制动力（回车默认恢复默认）：")
                zhidonglvh = input("请输入后轴制动力（回车默认恢复默认）：")
                if zhidonglvq == "" or zhidonglvh == "":
                    chongzhi = gongju()
                    chongzhi.xieruyuanshi(biaodingweizhi+"平板前左力标定.txt", beifenweizhi+"平板前左力标定备份.txt")
                    chongzhi.xieruyuanshi(biaodingweizhi+"平板前右力标定.txt", beifenweizhi+"平板前右力标定备份.txt")
                    chongzhi.xieruyuanshi(biaodingweizhi+"平板后左力标定.txt", beifenweizhi+"平板后左力标定备份.txt")
                    chongzhi.xieruyuanshi(biaodingweizhi+"平板后右力标定.txt", beifenweizhi+"平板后右力标定备份.txt")
                else:
                    chazhidian = 100
                    zhidonglvq = int(zhidonglvq)
                    zhidonglvh = int(zhidonglvh)
                    baifenbi = jisuan()
                    baifenbi.xierubianliang(biaodingweizhi+"平板前左力标定.txt", zhidonglvq, chazhidian)
                    baifenbi.xierubianliang(biaodingweizhi+"平板前右力标定.txt", zhidonglvq, chazhidian)
                    baifenbi.xierubianliang(biaodingweizhi+"平板后左力标定.txt", zhidonglvh, chazhidian)
                    baifenbi.xierubianliang(biaodingweizhi+"平板后右力标定.txt", zhidonglvh, chazhidian)

            else:
                print("正常线路")
                zhidonglvq = input("请输入前轴制动力（回车默认恢复默认）：")
                zhidonglvh = input("请输入后轴制动力（回车默认恢复默认）：")
                if zhidonglvq == "" or zhidonglvh == "":
                    chongzhi = gongju()
                    chongzhi.xieruyuanshi(biaodingweizhi+"平板前左力标定.txt", beifenweizhi+"平板前左力标定备份.txt")
                    chongzhi.xieruyuanshi(biaodingweizhi+"平板前右力标定.txt", beifenweizhi+"平板前右力标定备份.txt")
                    chongzhi.xieruyuanshi(biaodingweizhi+"平板后左力标定.txt", beifenweizhi+"平板后左力标定备份.txt")
                    chongzhi.xieruyuanshi(biaodingweizhi+"平板后右力标定.txt", beifenweizhi+"平板后右力标定备份.txt")
                else:
                    chazhidianq = input("请输入前轴差值点（回车默认0%,其他（包括输入0）正负随机9）：")
                    chazhidianh = input("请输入后轴差值点（回车默认0%,其他（包括输入0）正负随机9）：")
                    if chazhidianq == "":
                        chazhidianq = 100
                        baifenbi = jisuan()
                        baifenbi.xierubianliang(biaodingweizhi+"平板前左力标定.txt", zhidonglvq, chazhidianq)
                        baifenbi.xierubianliang(biaodingweizhi+"平板前右力标定.txt", zhidonglvq, chazhidianq)
                    else:
                        chazhidianq = int(chazhidianq) + random.randint(-9, 9)
                        zuolibuchang = 100 - chazhidianq
                        youlibuchang = 100 + chazhidianq
                        baifenbi = jisuan()
                        baifenbi.xierubianliang(biaodingweizhi+"平板前左力标定.txt", zhidonglvq, zuolibuchang)
                        baifenbi.xierubianliang(biaodingweizhi+"平板前右力标定.txt", zhidonglvq, youlibuchang)
                    if chazhidianh == "":
                        chazhidianh = 100
                        baifenbi = jisuan()
                        baifenbi.xierubianliang(biaodingweizhi+"平板后左力标定.txt", zhidonglvh, chazhidianh)
                        baifenbi.xierubianliang(biaodingweizhi+"平板后右力标定.txt", zhidonglvh, chazhidianh)
                    else:
                        chazhidianh = int(chazhidianh) + random.randint(-9, 9)
                        zuolibuchang = 100 - chazhidianh
                        youlibuchang = 100 + chazhidianh
                        baifenbi = jisuan()
                        baifenbi.xierubianliang(biaodingweizhi+"平板后左力标定.txt", zhidonglvh, zuolibuchang)
                        baifenbi.xierubianliang(biaodingweizhi+"平板后右力标定.txt", zhidonglvh, youlibuchang)

            if dangqianweizhi == 1:
                q = congkai()
                q.guanbidakai()

    if jiancexianleixing == "0":
        beifen_1 = beifen()
        beifen_1.chuangjian(biaodingweizhi+"左力标定.txt",beifenweizhi+"左力标定备份.txt")
        beifen_1.chuangjian(biaodingweizhi+"右力标定.txt",beifenweizhi+"右力标定备份.txt")
        print("这是一套滚筒线")
        while True:
            if zuolitongdao == youlitongdao:
                print("左右轮并行")
                zhidonglv = input("请输入制动力（回车默认恢复默认）：")
                if zhidonglv == "":
                    chongzhi = gongju()
                    chongzhi.xieruyuanshi(biaodingweizhi+"左力标定.txt",beifenweizhi+"左力标定备份.txt")
                    chongzhi.xieruyuanshi(biaodingweizhi+"右力标定.txt",beifenweizhi+"右力标定备份.txt")
                else:
                    chazhidian = 100
                    zhidonglv = int(zhidonglv)
                    baifenbi = jisuan()
                    baifenbi.xierubianliang(biaodingweizhi+"左力标定.txt", zhidonglv, chazhidian)
                    baifenbi.xierubianliang(biaodingweizhi+"右力标定.txt", zhidonglv, chazhidian)

            else:
                print("正常线路")
                zhidonglv = input("请输入制动力（回车默认恢复默认）：")
                if zhidonglv == "":
                    chongzhi = gongju()
                    chongzhi.xieruyuanshi(biaodingweizhi+"左力标定.txt", beifenweizhi+"左力标定备份.txt")
                    chongzhi.xieruyuanshi(biaodingweizhi+"右力标定.txt", beifenweizhi+"右力标定备份.txt")
                else:
                    chazhidian = input("请输入差值点（回车默认0%,其他（包括输入0）正负随机9）：")
                    if chazhidian == "":
                        chazhidian = 100
                        baifenbi = jisuan()
                        baifenbi.xierubianliang(biaodingweizhi+"左力标定.txt", zhidonglv, chazhidian)
                        baifenbi.xierubianliang(biaodingweizhi+"右力标定.txt", zhidonglv, chazhidian)
                    else:
                        chazhidian = int(chazhidian) + random.randint(-9, 9)
                        zuolibuchang = 100 - chazhidian
                        youlibuchang = 100 + chazhidian
                        baifenbi = jisuan()
                        baifenbi.xierubianliang(biaodingweizhi+"左力标定.txt", zhidonglv, zuolibuchang)
                        baifenbi.xierubianliang(biaodingweizhi+"右力标定.txt", zhidonglv, youlibuchang)
            if dangqianweizhi == 1:
                q = congkai()
                q.guanbidakai()



