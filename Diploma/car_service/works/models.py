from django.db import models

class Works(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название услуги')
    description = models.TextField(verbose_name="Описание")
    date = models.DateField(verbose_name='Дата')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "услугу"
        verbose_name_plural = 'услуги'
