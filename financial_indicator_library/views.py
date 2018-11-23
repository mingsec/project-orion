from django.shortcuts import render
from django.http      import HttpResponseRedirect
from django.urls      import reverse
from .models          import Indicator, TypeOfEnterprise, BusinessScale, BusinessStatus, IndicatorData
from .forms           import AverageForm


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
    indicator_data = IndicatorData()

    if request.method != 'POST':
        #当操作为非提交数据时，则创建一个新的表单
        form = AverageForm()
    else:
        #当操作为提交数据时，则对数据进行处理
        form = AverageForm(request.POST)

        if form.is_valid():        
            #获取post数据all_data['te']
            all_data = form.clean()
            te  = all_data['te']
            bs  = all_data['bs']
            bss = all_data['bss']

            indicator_data = IndicatorData.objects.get(te=te, bs=bs, bss=bss)

    context = {"form":form, "indicator_data":indicator_data}

    return render(request, 'financial_indicator_library/average.html', context)
