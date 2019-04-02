from django.contrib import admin
from ticheng.models import 预约列表
# Register your models here.




class yuyueAdmin(admin.ModelAdmin):
    list_display = ['id','姓名','车号','预约时间','检测时间','积分','车辆类型','检测站','照片路径',]
    search_fields = ('姓名','车号',)
admin.site.register(预约列表,yuyueAdmin)