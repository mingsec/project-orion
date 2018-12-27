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


class Client(models.Model):
    """客户数据"""
    number_of_client               = models.CharField(max_length=8 )
    name_of_client                 = models.CharField(max_length=50)
    taxpayer_identification_number = models.CharField(max_length=18)
    province                       = models.CharField(max_length=10)
    city                           = models.CharField(max_length=10)
    address                        = models.CharField(max_length=60)
    telephone                      = models.CharField(max_length=15)
    deposit_bank                   = models.CharField(max_length=50)
    bank_account                   = models.CharField(max_length=20)

    def __str__(self):
        """返回客户名称"""
        return self.name_of_client


class Product(models.Model):
    """产品信息"""
    number_of_product    = models.CharField(max_length=4 )
    name_of_product      = models.CharField(max_length=20)
    value_added_tax_rate = models.CharField(max_length=5 )

    def __str__(self):
        """返回产品名称"""
        return self.name_of_product


class Price(models.Model):
    """价格信息"""
    product      = models.ForeignKey(Product, on_delete=models.CASCADE)
    service_life = models.IntegerField(choices=((30,'30天'), (60,'60天'), (180,'180天'), (360,'360天'), (720,'720天')))
    price        = models.CharField(max_length=20)

    def __str__(self):
        """返回产品名称"""
        return self.price

