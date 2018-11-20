from django.shortcuts import render
from django.urls      import reverse
from .models          import Indicator, TypeOfEnterprise, BusinessScale, BusinessStatus


# Create your views here.
#在此处创建你的视图函数

def index(request):
    """financial_indicator_library网站的主页"""
    return render(request, 'financial_indicator_library/index.html')


def indicators(request):
    """显示目前已收集的所有财务指标"""
    indicators = Indicator.objects.all()
    context = {'indicators':indicators}

    return render(request, 'financial_indicator_library/indicators.html', context)


def average(request):
    """显示各行业关键财务指标的平均水平"""
    te_all  = TypeOfEnterprise.objects.all()
    bs_all  = BusinessScale.objects.all()
    bss_all = BusinessStatus.objects.all()

    context = {"te_all":te_all, "bs_all":bs_all, "bss_all":bss_all}

    return render(request, 'financial_indicator_library/average.html', context)
