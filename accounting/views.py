from django.shortcuts import render
from django.http      import HttpResponseRedirect
from django.urls      import reverse
from .models          import Order, Client
from .forms           import OrderForm, ClientForm

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

def clients(request):
    """显示目前所有的客户信息"""
    clients = Client.objects.all()
    context = {'clients':clients}

    return render(request, 'accounting/clients.html', context)

def new_client(request):
    """添加新的客户信息"""
    if request.method != 'POST':
        #当操作为非提交数据时，则创建一个新的客户信息页面
        form = ClientForm()
    else:
        #当操作为提交数据时，则对数据进行处理
        form = ClientForm(request.POST)
        if form.is_valid():
            #保存数据
            form.save()
            return HttpResponseRedirect(reverse('accounting:clients'))

    context = {'form':form}

    return render(request, 'accounting/new_client.html', context)