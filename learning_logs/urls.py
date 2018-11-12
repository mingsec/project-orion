# -*- coding: utf-8 -*-
# @Author: ZhuZefeng
# @Date:   2018-10-30 17:48:18
# @Last Modified by:   ZhuZefeng
# @Last Modified time: 2018-11-09 11:19:03


"""
为应用程序learning_logs定义URL模式
"""

from django.urls import path, re_path
from .           import views

app_name = 'learning_logs'

urlpatterns = [
               #learning_log的主页
               path('',views.index, name='index'),

               #显示所有主题
               path('topics', views.topics, name='topics'),

               #显示所有题目
               re_path('(?P<topic_name>[A-Z]+)/entries', views.entries, name='entries'),

               #显示所有条目
               re_path('(?P<topic_name>[A-Z]+)/(?P<entry_name>[A-Z]+)/blogs', views.blogs, name='blogs'),

               #用于添加新主题的页面 
               path('new_topic', views.new_topic, name='new_topic'), 

               #用于添加新科目的页面 
               re_path('(?P<topic_name>[A-Z]+)/new_entry', views.new_entry, name='new_entry'),

               #用于添加新条目的页面
               re_path('(?P<topic_name>[A-Z]+)/(?P<entry_name>[A-Z]+)/new_blog', views.new_blog, name='new_blog'),

               #用于编辑条目的页面
               re_path('(?P<topic_name>[A-Z]+)/(?P<entry_name>[A-Z]+)/(?P<blog_name>[A-Z]+)/edit_blog', views.edit_blog, name='edit_blog'),

               #显示当前登录用户创建的所有条目
               re_path('my_blogs', views.my_blogs, name='my_blogs'),

              ]
