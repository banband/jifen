import re
import os
beifenweizhi = "Data\标定数据"
a = os.path.exists("11")
print(a)
if a == False:
    os.mkdir(beifenweizhi+"\\标定备份")
