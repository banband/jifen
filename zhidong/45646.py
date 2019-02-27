import re
zuolibiaoding = open("平板线\Data\标定数据\左力标定.txt",'w')
file_context = zuolibiaoding.readlines()  # file_context是一个string，读取完后，就失去了对test.txt的文件引用
for i in file_context:
    d = re.findall(r";.*?;(.+?)\n", i)

    d = d[0]
    x = float(d)
    x = x * 100
    print(d)
    print(x)

zuolibiaoding.close()
#print(file_context)