# -*- coding: utf-8 -*-
# @Author: ZhuZefeng
# @Date:   2018-11-15 17:54:51
# @Last Modified by:   ZhuZefeng
# @Last Modified time: 2018-11-20 17:04:35


"""
为应用程序financial_indicator_library定义URL模式
"""

from django.urls import path, re_path
from .           import views

app_name = 'financial_indicator_library'

urlpatterns = [
               #financial_indicator_library的主页
               path('', views.index, name='index'),

               #显示目前所有收集的财务指标的页面
               path('indicators', views.indicators, name='indicators'),

               #显示各行业关键财务指标的平均水平的页面             
               path('average', views.average, name='average'),
              ]