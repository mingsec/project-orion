# -*- coding: utf-8 -*-
# @Author: ZhuZefeng
# @Date:   2018-10-31 14:21:35
# @Last Modified by:   ZeFeng
# @Last Modified time: 2018-11-05 22:02:27


from django  import forms
from .models import Topic, Entry, Blog

class TopicForm(forms.ModelForm):
    class Meta:
        model  = Topic
        fields = ['text', ]
        labels = {'text':'主题名称',}

class EntryForm(forms.ModelForm):
    class Meta:
        model   = Entry
        fields  = ['text',]
        labels  = {'text':'科目名称',}
        #widgets = {'text': forms.Textarea(attrs={'cols': 50})}

class BlogForm(forms.ModelForm):
    class Meta:
        model   = Blog
        fields  = ['title', 'text']
        labels  = {'title':'条目名称', 'text':'学习内容'}
        widgets = {'text': forms.Textarea(attrs={'cols': 22})}

