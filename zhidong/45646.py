import re

import sys
import os
import time
import subprocess

dangqianweizhi = __file__

if dangqianweizhi[0] not in ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]:
    print("部是")



subprocess.Popen(r'滚筒线\PJCXMain.exe')
print('打开成功')
time.sleep(5)
print('休息5s')
os.system(r'taskkill /F /IM PJCXMain.exe')
print('关闭成功')