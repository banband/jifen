from django.shortcuts import render,redirect
from functools import reduce
from ticheng.models import 预约列表

from django.db.models import Q
# Create your views here.
def index(request):
    return render(request,'ticheng/index.html',)


def baobiao(request):
    context = {'title': '图书列表', 'list': range(10)}
    return render(request,'ticheng/baobiao.html',context)

def chaxun(request):
    return render(request,'ticheng/chaxun.html')
def chaxun_1(request):
    shuju = request.POST
    chehao = shuju['1']
    miyao = shuju['2']
    if miyao == '12357':
        chaxun_2 = 预约列表.objects.filter(车号=chehao).exclude(检测站='1')
        return render(request, 'ticheng/chaxun.html', {'chaxun_2': chaxun_2})
    else:
        return render(request,'ticheng/miyaocuowu.html')
def miyaocuowu(request):
    return render(request,'ticheng/miyaocuowu.html')
#逻辑删除指定编号的图书
def delete(request,id):
    预约列表.objects.filter(id=int(id)).update(检测站='1')
    #转向到首页
    return redirect('/chaxun')
def jisuan(request):
    shuju = request.POST

    #print(shuju['1'])
    yue = shuju['101']
    #print(yue)
    def jisuan(yue):
        s = []

        for i in shuju.keys():

            if int(i) <= int(yue):
                ss = shuju[i]
                #print(ss)
                s.append(int(ss))

        # print(s)
        asb = reduce(lambda x, y: x + y, s)
        print('总完成任务%s' % asb)
        asr = asb - int(shuju['100'])
        print('任务外总数%s' % asr)
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
            print('完成10000以内数%s' % ccc)
            print('完成任务10000以上数%s' % aaa)
            print('完成任务20000以上数%s' % bbb)
            i = int(i)
            #if 1 == 1:
            if asr - i > 0:
                g = i - bbb
                if g <= 0:
                    print('百分只10是%s，百分12是%s,百分15是%s' % (0, 0, i))
                    return {
                        'ticheng':(i / 100) * 15,
                        'zong': asb,
                        'wai': asr,
                        'yue': i,
                        'yiwxia': ccc,
                        'yiwanshang': aaa,
                        'liangwanshang': bbb,
                        'bai10':0,
                        'bai12':0,
                        'bai15':i,
                    }
                elif (i - bbb) - aaa < 0:
                    print('百分只10是%s，百分12是%s,百分15是%s' % (0, g, bbb))
                    #return ((bbb / 100) * 15) + ((g / 100) * 12)
                    return {
                        'ticheng': ((bbb / 100) * 15) + ((g / 100) * 12),
                        'zong': asb,
                        'wai': asr,
                        'yue': i,
                        'yiwxia': ccc,
                        'yiwanshang': aaa,
                        'liangwanshang': bbb,
                        'bai10': 0,
                        'bai12': g,
                        'bai15': bbb,
                    }
                else:
                    h = i - bbb - aaa
                    print('百分只10是%s，百分12是%s,百分15是%s' % (h, aaa, bbb))
                    #return ((bbb / 100) * 15) + ((aaa / 100) * 12) + (h / 10)
                    return {
                        'ticheng': ((bbb / 100) * 15) + ((aaa / 100) * 12) + (h / 10),
                        'zong': asb,
                        'wai': asr,
                        'yue': i,
                        'yiwxia': ccc,
                        'yiwanshang': aaa,
                        'liangwanshang': bbb,
                        'bai10': h,
                        'bai12': aaa,
                        'bai15': bbb,
                    }
            else:
                if asr < 10000:
                    print('百分只10是%s，百分12是%s,百分15是%s' % (asr, 0, 0))
                    #return asr / 10
                    return {
                        'ticheng': asr / 10,
                        'zong': asb,
                        'wai': asr,
                        'yue': i,
                        'yiwxia': ccc,
                        'yiwanshang': aaa,
                        'liangwanshang': bbb,
                        'bai10': asr,
                        'bai12': 0,
                        'bai15': 0,
                    }
                else:
                    h = asr - bbb - aaa
                    print('百分只10是%s，百分12是%s,百分15是%s' % (h, aaa, bbb))
                    # return ((bbb / 100) * 15) + ((aaa / 100) * 12) + (h / 10)
                    return {
                        'ticheng': ((bbb / 100) * 15) + ((aaa / 100) * 12) + (h / 10),
                        'zong': asb,
                        'wai': asr,
                        'yue': i,
                        'yiwxia': ccc,
                        'yiwanshang': aaa,
                        'liangwanshang': bbb,
                        'bai10': h,
                        'bai12': aaa,
                        'bai15': bbb,
                    }
        else:
            #return '没有提成'
            return {
                'ticheng': '没有提成',
                'zong': asb,
                'wai': asr,
                'yue': i,
                'yiwxia': 0,
                'yiwanshang': 0,
                'liangwanshang': 0,
                'bai10': 0,
                'bai12': 0,
                'bai15': 0,
            }

    ssd = jisuan(yue)
    print('提成是%s' % ssd)

    return render(request, 'ticheng/yuangong.html', ssd)

def yuangong(request):
    return render(request,'ticheng/yuangong.html')


def yingxiao(request):
    return render(request,'ticheng/yingxiao.html')


def yingxiao_jisuan(request):
    shuju = request.POST

    print(shuju)
    jidu = shuju['101']

    # print(yue)
    def jisuan(j1,j2,j3,g):
        s = []

        for i in shuju.keys():

            if int(i) <= int(j3):
                ss = shuju[i]
                #print(ss)
                s.append(int(ss))


        # print(s)
        asb = reduce(lambda x, y: x + y, s)
        print('总完成任务%s' % asb)
        asr = asb - 9000
        if g == 2:
            h1 = int(shuju['1']) + int(shuju['2']) + int(shuju['3'])
            if h1 < 9000:
                asr -= h1
            else:
                asr -= 9000
            print(asb)
        if g == 3:
            h1 = int(shuju['1']) + int(shuju['2']) + int(shuju['3'])
            h2 = int(shuju['4']) + int(shuju['5']) + int(shuju['6'])


            if h1 < 9000:
                asr -= h1
            else:
                asr -= 9000
            if h2 < 9000:
                asr -= h2
            else:
                asr -= 9000
        if g == 4:
            h1 = int(shuju['1']) + int(shuju['2']) + int(shuju['3'])
            h2 = int(shuju['4']) + int(shuju['5']) + int(shuju['6'])
            h3 = int(shuju['7']) + int(shuju['8']) + int(shuju['9'])

            if h1 < 9000:
                asr -= h1
            else:
                asr -= 9000
            if h2 < 9000:
                asr -= h2
            else:
                asr -= 9000
            if h3 < 9000:
                asr -= h2
            else:
                asr -= 9000

        print('任务外总数%s' % asr)
        i = int(shuju[str(j1)]) + int(shuju[str(j2)]) + int(shuju[str(j3)])
        print('查询季度完成任务%s' % i)
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
            print('完成10000以内数%s' % ccc)
            print('完成任务10000以上数%s' % aaa)
            print('完成任务20000以上数%s' % bbb)
            i = int(i)
            # if 1 == 1:
            if asr - i > 0:
                g = i - bbb
                if g <= 0:
                    print('百分只10是%s，百分12是%s,百分15是%s' % (0, 0, i))
                    return {
                        'ticheng': (i / 100) * 15,
                        'zong': asb,
                        'wai': asr,
                        'yue': i,
                        'yiwxia': ccc,
                        'yiwanshang': aaa,
                        'liangwanshang': bbb,
                        'bai10': 0,
                        'bai12': 0,
                        'bai15': i,
                    }
                elif (i - bbb) - aaa < 0:
                    print('百分只10是%s，百分12是%s,百分15是%s' % (0, g, bbb))
                    # return ((bbb / 100) * 15) + ((g / 100) * 12)
                    return {
                        'ticheng': ((bbb / 100) * 15) + ((g / 100) * 12),
                        'zong': asb,
                        'wai': asr,
                        'yue': i,
                        'yiwxia': ccc,
                        'yiwanshang': aaa,
                        'liangwanshang': bbb,
                        'bai10': 0,
                        'bai12': g,
                        'bai15': bbb,
                    }
                else:
                    h = i - bbb - aaa
                    print('百分只10是%s，百分12是%s,百分15是%s' % (h, aaa, bbb))
                    # return ((bbb / 100) * 15) + ((aaa / 100) * 12) + (h / 10)
                    return {
                        'ticheng': ((bbb / 100) * 15) + ((aaa / 100) * 12) + (h / 10),
                        'zong': asb,
                        'wai': asr,
                        'yue': i,
                        'yiwxia': ccc,
                        'yiwanshang': aaa,
                        'liangwanshang': bbb,
                        'bai10': h,
                        'bai12': aaa,
                        'bai15': bbb,
                    }
            else:
                if (i - 9000) < 10000:
                    print('百分只10是%s，百分12是%s,百分15是%s' % (i - 9000, 0, 0))
                    # return asr / 10
                    return {
                        'ticheng': (i - 9000) / 10,
                        'zong': asb,
                        'wai': asr,
                        'yue': i,
                        'yiwxia': ccc,
                        'yiwanshang': aaa,
                        'liangwanshang': bbb,
                        'bai10': i -9000,
                        'bai12': 0,
                        'bai15': 0,
                    }
                else:
                    h = (i - 9000) - bbb - aaa
                    print('百分只10是%s，百分12是%s,百分15是%s' % (h, aaa, bbb))
                    # return ((bbb / 100) * 15) + ((aaa / 100) * 12) + (h / 10)
                    return {
                        'ticheng': ((bbb / 100) * 15) + ((aaa / 100) * 12) + (h / 10),
                        'zong': asb,
                        'wai': asr,
                        'yue': i,
                        'yiwxia': ccc,
                        'yiwanshang': aaa,
                        'liangwanshang': bbb,
                        'bai10': h,
                        'bai12': aaa,
                        'bai15': bbb,
                    }
        else:
            # return '没有提成'
            return {
                'ticheng': '没有提成',
                'zong': asb,
                'wai': asr,
                'yue': i,
                'yiwxia': 0,
                'yiwanshang': 0,
                'liangwanshang': 0,
                'bai10': 0,
                'bai12': 0,
                'bai15': 0,
            }
    if jidu == '1':
        ssd = jisuan(1,2,3,1)
        print('提成是%s' % ssd)
        return render(request, 'ticheng/yingxiao.html',ssd)
    elif jidu == '2':
        ssd = jisuan(4, 5, 6, 2)
        print('提成是%s' % ssd)
        return render(request, 'ticheng/yingxiao.html', ssd)
    elif jidu == '3':
        ssd = jisuan(7, 8, 9, 3)
        print('提成是%s' % ssd)
        return render(request, 'ticheng/yingxiao.html', ssd)
    elif jidu == '4':
        ssd = jisuan(10, 11, 12, 4)
        print('提成是%s' % ssd)
        return render(request, 'ticheng/yingxiao.html', ssd)


    #return render(request, 'ticheng/yingxiao.html')

