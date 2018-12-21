from django.shortcuts import render
from django.http      import HttpResponseRedirect
from django.urls      import reverse
from .models          import Order
from .forms           import OrderForm

# Create your views here.
#在此处创建你的视图函数

def index(request):
    """accounting程序的主页"""
    return render(request, 'accounting/index.html')

def orders(request):
    """显示目前所有的销售订单"""
    orders = Order.objects.all()
    context = {'orders':orders}

    return render(request, 'accounting/orders.html', context)

def new_order(request):
    """创建新的销售订单"""
    if request.method != 'POST':
        #当操作为非提交数据时，则创建一个新的销售订单
        form = OrderForm()
    else:
        #当操作为提交数据时，则对数据进行处理
        form = OrderForm(request.POST)
        if form.is_valid():
            #保存数据
            form.save()
            return HttpResponseRedirect(reverse('accounting:orders'))

    context = {'form':form}

    return render(request, 'accounting/new_order.html', context)

