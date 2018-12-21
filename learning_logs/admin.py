from django.contrib import admin

#引入自己的模型
from learning_logs.models import Topic, Entry, Blog

# Register your models here.
#在此处注册自己的模型
admin.site.register(Topic)
admin.site.register(Entry)
admin.site.register(Blog)