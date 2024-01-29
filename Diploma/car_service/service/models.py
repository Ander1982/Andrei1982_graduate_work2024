from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='service/images/')

    def __str__(self):
        return self.title
