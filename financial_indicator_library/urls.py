# -*- coding: utf-8 -*-
# @Author: ZhuZefeng
# @Date:   2018-11-15 17:54:51
# @Last Modified by:   ZhuZefeng
# @Last Modified time: 2018-11-15 17:56:22


"""
为应用程序financial_indicator_library定义URL模式
"""

from django.urls import path, re_path
from .           import views

app_name = 'financial_indicator_library'

urlpatterns = [
               #financial_indicator_library的主页
               path('',views.index, name='index'),

              ]