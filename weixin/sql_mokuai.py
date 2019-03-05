import pymysql

class sql_mokuai(object):

    def charu(self,id_1,xingming_1,chehao_1,leixing_1,jiancezhan_1,jifen_1,yuyueshijian_1,jianceshijian_1):

        self.id = id_1
        self.xingming = xingming_1
        self.chehao = chehao_1
        self.leixing = leixing_1
        self.jiancezhan = jiancezhan_1
        self.jifen = jifen_1
        self.yuyueshijian= yuyueshijian_1
        self.jianceshijian = jianceshijian_1
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "sa", "mysql")

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 插入语句
        sql = "INSERT INTO yuyue(id, xingming, chehao, leixing, jiancezhan, " \
              "jifen, yuyueshijian, jianceshijian)VALUES ('%s','%s','%s','%s','" \
              "%s','%s','%s','%s')" %(self.id,self.xingming, self.chehao, self.leixing,
                                      self.jiancezhan, self.jifen, self.yuyueshijian,self.jianceshijian)
        #try:
            # 执行sql语句
        cursor.execute(sql)
            # 提交到数据库执行
        db.commit()
        print("成功")
        #except:
            # 如果发生错误则回滚
            #db.rollback()
            # print("失败")

        # 关闭数据库连接
        db.close()

    def chaxun(self,jifen):
        self.jifen = jifen
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "sa", "mysql")

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 查询语句
        sql = "SELECT * FROM yuyue \
               WHERE jifen > %s" % (self.jifen)
        print(sql)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            print(results)
            for row in results:
                id = row[0]
                xingming = row[1]
                chehao = row[2]
                leixing = row[3]
                jiancezhan = row[4]
                jifen = row[5]
                yuyueshijian = row[6]
                jianceshijian = row[7]

                # 打印结果
                print("id=%s,姓名=%s,车号=%s,类型=%s,检测站=%s,积分=%s,预约时间=%s,检测时间=%s" % \
                      (id, xingming, chehao, leixing, jiancezhan,jifen,yuyueshijian,jianceshijian))
        except:
            print("Error: unable to fetch data")

        # 关闭数据库连接
        db.close()

if __name__ == '__main__':
    a = sql_mokuai()
    #a.chaxun(100)
    a.charu('3','wangdang','hei111222','qingxing','zhiyuan','300','2019-03-05','1')