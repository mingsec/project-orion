from django.contrib import admin

#引入自己的模型
from financial_indicator_library.models  import TypeOfEnterprise, BusinessScale, BusinessStatus
from financial_indicator_library.models  import TypeOfIndicator, Indicator, IndicatorData

# Register your models here.
#在此处注册自己的模型
admin.site.register(TypeOfEnterprise)
admin.site.register(BusinessScale)
admin.site.register(BusinessStatus)
admin.site.register(TypeOfIndicator)
admin.site.register(Indicator)
admin.site.register(IndicatorData)