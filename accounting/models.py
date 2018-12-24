from django.db import models

# Create your models here.
#在此处创建你的模型。

class Order(models.Model):
    """销售订单数据"""
    number_of_purchase_contract = models.CharField(max_length=15)
    number_of_client            = models.CharField(max_length=8 )
    product                     = models.CharField(max_length=20)
    date_of_sale                = models.DateField()
    service_life                = models.IntegerField()
    sales_amount                = models.FloatField()
    tax_included_or_not         = models.BooleanField(choices=((False,'不含增值税'),(True,'含增值税')), default=False)
    invoiced_or_not             = models.BooleanField(choices=((False,'未开发票'),(True,'已开发票')), default=False)
    number_of_invoiced          = models.CharField(max_length=20)
    closed_or_not               = models.BooleanField(choices=((False,'未到期'),(True,'已到期')), default=False)

    def __str__(self):
        """返回销售订单编号"""
        return self.number_of_purchase_contract

