from django.contrib    import admin
from accounting.models import Order, Client

# Register your models here.
#注册自己的模型
admin.site.register(Order)
admin.site.register(Client)
