from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    description = models.CharField(max_length=250, verbose_name="описание")
    image = models.ImageField(upload_to='service/images/', verbose_name='картинка')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "услугу"
        verbose_name_plural = 'услуги'


class StatusOrder(models.Model):
    status_name = models.CharField(max_length=200, verbose_name="Название статуса")

    def __str__(self):
        return self.status_name

    class Meta:
        verbose_name = "статус"
        verbose_name_plural = "Статусы"


class Order(models.Model):
    order_dt = models.DateTimeField(auto_now_add=True, verbose_name="Дата")
    order_name = models.CharField(max_length=200, verbose_name="Имя")
    order_phone = models.CharField(max_length=200, verbose_name="Телефон")
    order_text = models.TextField(verbose_name='Описание заказа')
    order_status = models.ForeignKey(StatusOrder, on_delete=models.PROTECT, null=True, blank=True,
                                     verbose_name="Статус")

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = "заказ"
        verbose_name_plural = "Заказы"
