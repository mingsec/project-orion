# -*- coding: utf-8 -*-
# @Author: ZhuZefeng
# @Date:   2018-12-20 17:56:56
# @Last Modified by:   ZhuZefeng
# @Last Modified time: 2018-12-27 11:46:35


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

               #显示所有客户信息的页面
               path('clients', views.clients, name='clients'),

               #新增客户的页面
               path('new_client', views.new_client, name='new_client'),

               #显示所有产品信息的页面
               path('products', views.products, name='products'),

               #新增产品的页面
               #path('new_product', views. new_product, name=' new_product'),
               
              ]