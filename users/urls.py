# -*- coding: utf-8 -*-
# @Author: ZhuZefeng
# @Date:   2018-11-01 16:59:13
# @Last Modified by:   ZhuZefeng
# @Last Modified time: 2018-11-02 18:09:50


"""为应用程序users定义URL模式"""
from django.contrib.auth.views import LoginView
from django.urls               import path
from .                         import views

app_name = 'users'

urlpatterns = [
               # 登录页面
               path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),

               #注销页面
               path('logout', views.logout_view, name='logout'),

               #注册页面
               path('register', views.register, name='register'),

              ]