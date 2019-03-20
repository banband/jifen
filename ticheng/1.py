from functools import reduce

shuju = {
    '100': 3000,
    '1': 2000,
    '2': 1000,
    '3': 1000,
    '4': 1000,
    '5': 9000,
    '6': 0,
    '7': 0,
    '8': 0,
    '9': 0,
    '10': 0,
    '11': 0,
    '12': 0,
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
    if asr >= 0:

        bbb = asr - 20000
        aaa = asr - 10000
        if bbb <= 0:
            bbb = 0
        if aaa > 10000:
            aaa = 10000
        if aaa <= 0:
            aaa = 0
        ccc = asr - aaa - bbb
        print('完成10000以内数%s'%ccc)
        print('完成任务10000以上数%s' % aaa)
        print('完成任务20000以上数%s' % bbb)

        if asr - i > 0:
            g = i - bbb
            if g <= 0:
                print('百分只10是%s，百分12是%s,百分15是%s' % (0, 0, i))
                return (i/100)*15
            elif (i - bbb) - aaa < 0:
                print('百分只10是%s，百分12是%s,百分15是%s' % (0, g, bbb))
                return ((bbb/100)*15)+((g/100)*12)
            else:
                h = i - bbb - aaa
                print('百分只10是%s，百分12是%s,百分15是%s' % (h, aaa, bbb))
                return ((bbb/100)*15)+((aaa/100)*12)+(h/10)

        else:
            print('百分只10是%s，百分12是%s,百分15是%s' % (asr, 0, 0))
            return asr /10
    else:
        return '没有提成'


ssd = jisuan(5)
print('提成是%s' % ssd)