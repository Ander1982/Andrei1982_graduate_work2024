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


class ProductCategory(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Категория шин")
    description = models.TextField(blank=True, verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name="Марка шин")
    image = models.ImageField(upload_to="service_images/", blank=True, verbose_name="Изображение")
    description = models.TextField(blank=True, verbose_name="Описание")
    short_description = models.CharField(max_length=100, blank=True, verbose_name="Краткое описание")
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name="Цена")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество")
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, verbose_name="Категория")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'шина'
        verbose_name_plural = 'Шины'


class Photo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")
    add_photo = models.ImageField(upload_to="service_images/add/", blank=True, verbose_name="Фото")

    class Meta:
        verbose_name = 'изображение'
        verbose_name_plural = 'Изображения'
