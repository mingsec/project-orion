# -*- coding: utf-8 -*-
# @Author: ZhuZefeng
# @Date:   2018-11-22 10:35:08
# @Last Modified by:   ZhuZefeng
# @Last Modified time: 2018-12-21 20:03:57


from django  import forms
from .models import TypeOfEnterprise, BusinessScale, BusinessStatus, IndicatorData

class AverageForm(forms.Form):
    """定义从企业类型、企业规模及企业状况表中读取数据供用户查询"""
    #创建下拉选择框，值为数字，将id传到后台处理 
    te  = forms.IntegerField(label='企业类型', widget=forms.Select())
    bs  = forms.IntegerField(label='企业规模', widget=forms.Select())
    bss = forms.IntegerField(label='企业状况', widget=forms.Select())

    def __init__(self, *args, **kwargs):
        super(AverageForm, self).__init__(*args, **kwargs)
        #从企业类型表中读取全部数据
        self.fields['te'].widget.choices  = TypeOfEnterprise.objects.all().values_list('id', 'type_of_enterprise')
        self.fields['bs'].widget.choices  = BusinessScale.objects.all().values_list('id', 'business_scale')
        self.fields['bss'].widget.choices = BusinessStatus.objects.all().values_list('id', 'business_status')
