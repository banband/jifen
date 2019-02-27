import configparser


class Jc:

    def huoqubiaodingwenjian(self):

        pass


            #  file_context = open(file).read().splitlines()
            #ile_context是一个list，每行文本内容是list中的一个元素
            #biaoding = open("平板线\Data\标定数据\左力标定.txt", "w")
            #biaoding.write(biaoding)
            #biaoding.close()

    def biaodingxieru(self):

        biaoding = open("平板线\Data\标定数据\左力标定.txt", "w")
        biaoding.write()
        biaoding.close()

    def huoqupeizhiwenjian(self):
        config = configparser.ConfigParser(allow_no_value=True)
        config.read("参数配置.ini")

        zuolitongdao = config.get("参数","左力通道")
        youlitongdao = config.get("参数","右力通道")
        jiancexianleixing = config.get("工位设定","平板")
        pingbanqianzuolitongdao = config.get("参数","平板前左力通道")
        pingbanqianyoulitongdao = config.get("参数","平板前右力通道")
        pingbanhouzuolitongdao = config.get("参数","平板后左力通道")
        pingbanhuoyoulitongdao = config.get("参数","平板后右力通道")
        print(zuolitongdao)
        print(youlitongdao)
        print(jiancexianleixing)

        if jiancexianleixing == 1:
            #这个是平板线
            pass
        else:
            #滚筒线
            guntong()


    def guntong(self):
        if zuolitongdao == youlitongdao:
            #两轮并1
            pass
        else:
            zuolibiaoding = open("平板线\Data\标定数据\左力标定.txt")
            file_context = zuolibiaoding.readlines()  # file_context是一个string，读取完后，就失去了对test.txt的文件引用
            zuolibiaoding.close()
            print(file_context)
            #zuolixiugaihou = "".join(file_context)
            #print(zuolixiugaihou)


if __name__ == '__main__':
    huoqupeizhiwenjian()
