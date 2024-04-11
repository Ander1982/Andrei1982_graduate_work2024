from django.db import models
from django.contrib.auth.models import User
from works.models import Works


class Rec(models.Model):
    rec_name = models.CharField(max_length=200, verbose_name='клиент')
    rec_day = models.DateField(verbose_name='дата')
    rec_time = models.TimeField(verbose_name='время')

    def __str__(self):
        return self.rec_name

    class Meta:
        verbose_name = "запись"
        verbose_name_plural = 'Записи'


class Service(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    description = models.CharField(max_length=250, verbose_name="описание")
    image = models.ImageField(upload_to='service/images/', verbose_name='картинка')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "услугу"
        verbose_name_plural = 'услуги'


class Staff(models.Model):
    name = models.CharField(max_length=100, verbose_name='имя')
    categories = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='вид услуг')
    skills = models.IntegerField(default=0, verbose_name='классность')
    photo = models.ImageField(upload_to='static/service/', default='user-default.png', verbose_name='фотографии')
    vote_total = models.IntegerField(default=0, blank=True, null=True)
    vote_ratio = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-vote_ratio", "-vote_total", "name"]
        verbose_name = "сотрудника"
        verbose_name_plural = 'Сотрудники'

    def reviewers(self):
        queryset = self.review_set.all().values_list("owner__id", flat=True)
        return queryset

    def get_vote_count(self):
        reviews = self.review_set.all()
        up_votes = reviews.filter(value='положительный').count()
        total_votes = reviews.count()

        ratio = up_votes / total_votes * 100
        self.vote_total = total_votes
        self.vote_ratio = ratio

        self.save()


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
    order_status = models.ForeignKey(StatusOrder, on_delete=models.DO_NOTHING, null=True, blank=True,
                                     verbose_name="Статус")

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = "заказ"
        verbose_name_plural = "Заказы"


class Review(models.Model):
    VOTE_TYPE = (
        ('положительный', 'Положительный'),
        ('отрицательный', 'Отрицательный')
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='клиент')
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, verbose_name='сотрудник')
    body = models.TextField(null=True, blank=True, verbose_name='отзыв')
    value = models.CharField(max_length=100, choices=VOTE_TYPE, verbose_name='отзыв')
    created = models.DateTimeField(auto_now_add=True, verbose_name='время создания')

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "отзыв"
        verbose_name_plural = "Отзывы"
        unique_together = ['owner', 'staff']
