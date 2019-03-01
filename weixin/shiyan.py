

biaodingweizhi = "Data\标定数据\\"
beifenweizhi = "Data\标定数据\标定备份\\"
jianchalujing = "Data\标定数据\\"
dangqianweizhi = ""


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