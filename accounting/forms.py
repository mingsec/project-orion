# -*- coding: utf-8 -*-
# @Author: ZhuZefeng
# @Date:   2018-12-21 15:22:57
# @Last Modified by:   ZhuZefeng
# @Last Modified time: 2018-12-22 17:23:21


from django       import forms
from django.forms import widgets
from .models      import Order

class OrderForm(forms.ModelForm):
    """用于创建销售订单的表单"""
    
    class Meta:
        model  = Order
        fields = ['number_of_purchase_contract', 
                    'number_of_client', 
                    'product', 
                    'date_of_sale', 
                    'service_life', 
                    'sales_amount', 
                    'tax_included_or_not', 
                    'invoiced_or_not', 
                    'number_of_invoiced', 
                    'closed_or_not',]

    '''
    number_of_purchase_contract = forms.CharField(label='订单编号')
    number_of_client            = forms.CharField(label='客户名称')
    product                     = forms.CharField(label='产品名称')
    date_of_sale                = forms.DateField(label='销售日期')
    service_life                = forms.IntegerField(label='使用期限')
    sales_amount                = forms.FloatField(label='销售金额')
    tax_included_or_not         = forms.IntegerField(label='是否含税', widget=forms.Select(choices=(('0','不含增值税'),('1','含增值税'))))
    invoiced_or_not             = forms.IntegerField(label='是否开票', widget=forms.Select(choices=(('0','未开发票'),('1','已开发票'))))
    number_of_invoiced          = forms.CharField(label='发票编号')
    closed_or_not               = forms.IntegerField(label='是否到期', widget=forms.Select(choices=(('0','未到期'),('1','已到期'))))
    '''