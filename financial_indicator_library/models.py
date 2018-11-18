from django.db                  import models

# Create your models here.
#在此处创建你的模型。


class TypeOfEnterprise(models.Model):
    """企业的类型"""
    type_of_enterprise = models.CharField(max_length=20)

    def __str__(self):
        """返回模型的值"""
        return self.type_of_enterprise


class BusinessScale(models.Model):
    """企业的规模"""
    business_scale = models.CharField(max_length=10)

    def __str__(self):
        """返回模型的值"""
        return self.business_scale


class BusinessStatus(models.Model):
    """企业的状况"""
    business_status = models.CharField(max_length=5)

    class Meta:
        verbose_name_plural = 'BusinessStatus'

    def __str__(self):
        """返回模型的值"""
        return self.business_status


class  TypeOfIndicator(models.Model):
    """指标类型"""
    type_of_indicators_zh = models.CharField(max_length=20)
    type_of_indicators_en = models.CharField(max_length=40)

    def __str__(self):
        """返回模型的值"""
        return self.type_of_indicators_zh


class  Indicator(models.Model):
    """指标库"""
    indicator_type        = models.ForeignKey(TypeOfIndicator, on_delete=models.CASCADE)
    indicator_name_zh     = models.CharField(max_length=50)
    indicator_name_en     = models.CharField(max_length=100)
    indicator_short_name  = models.CharField(max_length=10)
    unit_of_measurement   = models.CharField(max_length=10)
    indicator_description = models.CharField(max_length=300)

    def __str__(self):
        """返回模型的值"""
        return self.indicator_name_zh


class IndicatorData(models.Model):
    """指标数据"""
    te      = models.ForeignKey(TypeOfEnterprise, on_delete=models.CASCADE)
    bs      = models.ForeignKey(BusinessScale, on_delete=models.CASCADE)
    bss     = models.ForeignKey(BusinessStatus, on_delete=models.CASCADE)
    roe     = models.CharField(max_length=20)
    rota    = models.CharField(max_length=20)
    ros     = models.CharField(max_length=20)
    scsm    = models.CharField(max_length=20)
    rpce    = models.CharField(max_length=20)
    roc     = models.CharField(max_length=20)
    tat     = models.CharField(max_length=20)
    art     = models.CharField(max_length=20)
    bar     = models.CharField(max_length=20)
    cat     = models.CharField(max_length=20)
    cra     = models.CharField(max_length=20)
    alr     = models.CharField(max_length=20)
    ntie    = models.CharField(max_length=20)
    qr      = models.CharField(max_length=20)
    cfcr    = models.CharField(max_length=20)
    ibdr    = models.CharField(max_length=20)
    clr     = models.CharField(max_length=20)
    sgr     = models.CharField(max_length=20)
    cpar    = models.CharField(max_length=20)
    opgr    = models.CharField(max_length=20)
    tagr    = models.CharField(max_length=20)
    tir     = models.CharField(max_length=20)
    it      = models.CharField(max_length=20)
    tgapca  = models.CharField(max_length=20)
    cepoi   = models.CharField(max_length=20)
    evar    = models.CharField(max_length=20)
    ebitdar = models.CharField(max_length=20)
    car     = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'IndicatorData'

    def __str__(self):
        """返回模型的值"""
        return str(self.te) + "-" + str(self.bs) + "-" + str(self.bss)