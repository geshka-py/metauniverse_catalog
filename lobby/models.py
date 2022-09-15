from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=1000)
    price = models.FloatField()
    created_time = models.DateTimeField()
    image = models.ImageField(upload_to='media')
    model_file = models.FileField(upload_to='media', blank=True)

