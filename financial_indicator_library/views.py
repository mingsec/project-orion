from django.shortcuts import render
from django.http      import HttpResponseRedirect
from django.urls      import reverse
from .models          import Indicator, TypeOfEnterprise, BusinessScale, BusinessStatus, IndicatorData


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
    
    indicator_data = IndicatorData()

    if request.method == "POST":
        te  = request.POST.get("type_of_enterprise")
        bs  = request.POST.get("business_scale")
        bss = request.POST.get("business_status")
       
        indicator_data = IndicatorData.objects.get(te=te, bs=bs, bss=bss)
        print(indicator_data.te)

    context = {"te_all":te_all, "bs_all":bs_all, "bss_all":bss_all, "indicator_data":indicator_data}

    return render(request, 'financial_indicator_library/average.html', context)
