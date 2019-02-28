import re
import random
import configparser
import os

biaodingweizhi = "Data\标定数据\\"
beifenweizhi = "Data\标定数据\标定备份\\"
jianchalujing = "Data\标定数据\\"
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


