import re

with open("右力标定.txt","r",encoding="utf-8") as f:
    lines = f.readlines()
    print(lines)
#写的方式打开文件
with open("右力标定.txt","w",encoding="utf-8") as f_w:
    for i in lines:


        d = re.findall(r";.*?;(.*?)\n", i)
        print(d)
        d = d[0]
        x = float(d)
        x = str(x * 100)
        print(d)
        print(x)
        #
        #
        #      #替换
        line = i.replace(d,x)
        f_w.write(line)