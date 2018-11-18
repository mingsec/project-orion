from django.shortcuts import render
from django.urls      import reverse

# Create your views here.
#在此处创建你的视图函数

def index(request):
    """financial_indicator_library网站的主页"""
    return render(request, 'financial_indicator_library/index.html')