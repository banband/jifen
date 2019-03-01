# -*- coding: UTF-8 -*-
from aip import AipOcr

# 定义常量
APP_ID = '15654566'
API_KEY = 'QmxIgQQMvUAUSTZkMYvvYDr8'
SECRET_KEY = 'XUyGdkvSZ9OuapmvnDCDrsWEbOllO1tz'

# 初始化AipFace对象
aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)

# 读取图片
filePath = "2-9.jpg"


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


options = {}

result = aipOcr.vehicleLicense(get_file_content(filePath), options)
print(result)

for key in result['words_result']:
    print(key + ':' + str(result['words_result'][key]['words']))