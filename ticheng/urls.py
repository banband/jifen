"""jifen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from ticheng import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^index$', views.index),
    url(r'^jisuan$', views.jisuan),
    url(r'^yingxiao$', views.yingxiao),
    url(r'^yingxiao_jisuan$', views.yingxiao_jisuan),
    url(r'^yuangong$', views.yuangong),
    url(r'^baobiao$', views.baobiao),
    url(r'^chaxun$', views.chaxun),
    url(r'^chaxun_1$', views.chaxun_1),
    url(r'^delete(\d+)/$', views.delete),
    url(r'^miyaocuowu$', views.miyaocuowu)
]
