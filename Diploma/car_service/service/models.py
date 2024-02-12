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
