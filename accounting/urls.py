# -*- coding: utf-8 -*-
# @Author: ZhuZefeng
# @Date:   2018-12-20 17:56:56
# @Last Modified by:   ZhuZefeng
# @Last Modified time: 2018-12-21 15:43:56


"""
为应用程序accounting定义URL模式
"""

from django.urls import path, re_path
from .           import views

app_name = 'accounting'

urlpatterns = [
               #accounting程序的主页
               path('', views.index, name='index'),

               #显示所有销售订单的页面
               path('orders', views.orders, name='orders'),

               #新增销售订单的页面
               path('new_order', views.new_order, name='new_order'),
               
              ]