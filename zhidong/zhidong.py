import random
def xuanze():


    xianhao = input("x")
    if xianhao == '1':
        pingban()
    elif xianhao == '2':
        guntong()
    else:
        print('输入错误')





def guntong():
    diyihang = '1;0;0.0'
    biaojidian_1_key = '2;350;'
    biaojidian_2_key = '3;716;'
    biaojidian_3_key = ''
    biaojidian_1 = 375
    biaojidian_2 = 711
    biaojidian_3 = ''
    gdbjd_1 = 375.0
    gdbjd_2 = 711.0
    gdbjd_3 = ''
    y_diyihang = '1;0;0.0'
    y_biaojidian_1_key = '2;362;'
    y_biaojidian_2_key = '3;724;'
    y_biaojidian_3_key = ''
    y_biaojidian_1 = 364
    y_biaojidian_2 = 732
    y_biaojidian_3 = 4005
    y_gdbjd_1 = 364.0
    y_gdbjd_2 = 732.0
    y_gdbjd_3 = ''


    while True:
        baifen = str(input('z'))
        chazhidian = str(input("差值点"))
        if baifen == 'q':
            xuanze()

        if baifen == '':
            biaojidian_1 = gdbjd_1
            biaojidian_2 = gdbjd_2
            biaojidian_3 = gdbjd_3
            y_biaojidian_1 = y_gdbjd_1
            y_biaojidian_2 = y_gdbjd_2
            y_biaojidian_3 = y_gdbjd_3

        else:
            chazhidianbaifenbi = int(chazhidian) + random.randint(-9,9)
            zuolunbuchang = 100 - chazhidianbaifenbi
            youlunbuchang = 100 + chazhidianbaifenbi
            print(zuolunbuchang)
            print(youlunbuchang)
            biaojidian_1 = (biaojidian_1 / int(baifen)) * int(zuolunbuchang) * 0.8
            zuizongzuoli_1 = '%.1f'%biaojidian_1
            print(zuizongzuoli_1)
            biaojidian_2 = (biaojidian_2 / int(baifen)) * int(zuolunbuchang) * 0.8
            biaojidian_3 = (biaojidian_3 / int(baifen)) * int(zuolunbuchang) * 0.8
            print(biaojidian_3)
            y_biaojidian_1 = (y_biaojidian_1 / int(baifen)) * int(youlunbuchang) * 0.8
            y_biaojidian_2 = (y_biaojidian_2 / int(baifen)) * int(youlunbuchang) * 0.8
            y_biaojidian_3 = (y_biaojidian_3 / int(baifen)) * int(youlunbuchang) * 0.8
            print(y_biaojidian_3)


        file_handle=open('Data\标定数据\左力标定.txt',mode='w')
        file_handle.writelines([diyihang,'\n',biaojidian_1_key,zuizongzuoli_1,'\n',biaojidian_2_key,'%.1f'%biaojidian_2,'\n',biaojidian_3_key,biaojidian_3])
        file_handle.close()

        file_handle = open('Data\标定数据\右力标定.txt', mode='w')
        file_handle.writelines(
            [y_diyihang, '\n', y_biaojidian_1_key, '%.1f' % y_biaojidian_1, '\n', y_biaojidian_2_key, '%.1f' % y_biaojidian_2, '\n',
             y_biaojidian_3_key,y_biaojidian_3])
        file_handle.close()

def pingban():
    diyihang = '1;0;0.0'
    qzbjd1key = '2;605;'
    qybjd1key = '2;732;'
    hzbjd1key = '2;293;'
    hybjd1key = '2;282;'
    qzbjd2key = '3;4095;'
    qybjd2key = '3;4095;'
    hzbjd2key = '3;4095;'
    hybjd2key = '3;4095;'
    qzgdbjd1 = 430.7
    qygdbjd1 = 422.4
    hzgdbjd1 = 420.4
    hygdbjd1 = 420.4
    qzgdbjd2 = 2021.1
    qygdbjd2 = 2094.8
    hzgdbjd2 = 4058.7
    hygdbjd2 = 4217.0
    qzbjd1 = 430
    qybjd1 = 422
    hzbjd1 = 420
    hybjd1 = 420
    qzbjd2 = 2021
    qybjd2 = 2094
    hzbjd2 = 4058
    hybjd2 = 4217

    while True:
        qbaifen = str(input('q'))
        hbaifen = str(input("h"))
        if qbaifen or hbaifen == 'q':
            xuanze()

        if qbaifen == '':
            qzbjd1 = qzgdbjd1
            qybjd1 = qygdbjd1
            qzbjd2 = qzgdbjd2
            qybjd2 = qygdbjd2

        else:
            qzbjd1 = qzbjd1 / int(qbaifen) * 80
            qybjd1 = qybjd1 / int(qbaifen) * 80
            qzbjd2 = qzbjd2 / int(qbaifen) * 80
            qybjd2 = qybjd2 / int(qbaifen) * 80


        if hbaifen == "":

            hzbjd1 = hzgdbjd1
            hybjd1 = hygdbjd1
            hzbjd2 = hzgdbjd2
            hybjd2 = hygdbjd2


        else:

            hzbjd1 = hzbjd1 / int(hbaifen) * 80
            hybjd1 = hybjd1 / int(hbaifen) * 80
            hzbjd2 = hzbjd2 / int(hbaifen) * 80
            hybjd2 = hybjd2 / int(hbaifen) * 80

        file_handle=open('D:\github\zhidong\平板前左力标定.txt',mode='w')
        file_handle.writelines([diyihang,'\n',qzbjd1key,'%.1f'%qzbjd1,'\n',qzbjd2key,'%.1f'%qzbjd2])
        file_handle.close()

        file_handle = open('D:\github\zhidong\平板前右力标定.txt', mode='w')
        file_handle.writelines([diyihang, '\n', qybjd1key, '%.1f' % qybjd1, '\n', qybjd2key, '%.1f' % qybjd2])
        file_handle.close()

        file_handle = open('D:\github\zhidong\平板后左力标定.txt', mode='w')
        file_handle.writelines([diyihang, '\n', hzbjd1key, '%.1f' % hzbjd1, '\n', hzbjd2key, '%.1f' % hzbjd2])
        file_handle.close()

        file_handle = open('D:\github\zhidong\平板后右力标定.txt', mode='w')
        file_handle.writelines([diyihang, '\n', hybjd1key, '%.1f' % hybjd1, '\n', hybjd2key, '%.1f' % hybjd2])
        file_handle.close()





if __name__ == '__main__':

    xuanze()