from functools import reduce

shuju = {
    '100':5000,
    '1':4000,
    '2':9000,
    '3':5000,
    '4':5000,
    '5':5000,
    '6':5000,
    '7':5000,
    '8':5000,
    '9':5000,
    '10':5000,
    '11':5000,
    '12':5000,
}
def jisuan(yue):
    s = []

    for i in shuju.keys():

        if int(i) <= yue:
            ss = shuju[i]
            #print(ss)
            s.append(ss)

    #print(s)
    asb = reduce(lambda x,y:x+y, s)
    print('总完成任务%s'%asb)
    asr = asb - shuju['100']
    print('任务外总数%s'%asr)
    i = shuju[str(yue)]
    print('查询月份完成任务%s' % i)
    if asr >= i:

        aaa = asb - 20000
        print('完成任务20000以上数%s' % aaa)

        cao20000 = aaa - i
        if cao20000 >= 0:
            return (i / 100) * 15
        elif aaa <= 0:
            return i / 10
        else:
            bai10 = i - aaa
            bai15 = i - bai10
            print('百分只10是%s，百分15是%s'%(bai10,bai15))
            return (bai10 / 10)+((bai15 /100) *15)
    elif asr >= 0:
        return asr /10
    else:
        return '没有提成'


ssd = jisuan(2)
print('提成是%s'%ssd)