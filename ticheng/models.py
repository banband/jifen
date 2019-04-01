from django.db import models

# Create your models here.


class 预约列表(models.Model):
    姓名 = models.CharField(max_length=255,null=True,blank=True,db_column='xingming')
    车号 = models.CharField(max_length=255, null=True, blank=True,db_column='chehao')
    车辆类型 = models.CharField(max_length=255, null=True, blank=True,db_column='leixing')
    检测站 = models.CharField(max_length=255, null=True, blank=True,db_column='jiancezhan')
    积分 = models.CharField(max_length=255, null=True, blank=True,db_column='jifen')
    预约时间 = models.CharField(max_length=255, null=True, blank=True,db_column='yuyueshijian')
    检测时间 = models.CharField(max_length=255, null=True, blank=True,db_column='jianceshijian')
    照片路径 = models.CharField(max_length=255, null=True, blank=True,db_column='zhaopianlujing')
