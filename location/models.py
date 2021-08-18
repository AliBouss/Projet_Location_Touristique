from django.db import models


class Location(models.Model):
    title = models.CharField(max_length=123)
    locality = models.CharField(max_length=123)
    type = models.CharField(max_length=123)
    category = models.CharField(max_length=123)
    description = models.CharField(max_length=123)
    price = models.IntegerField(max_length=123)
    date_on = models.DateTimeField(max_length=123)
    date_end = models.DateTimeField(max_length=123)
    condition = models.CharField(max_length=123)
    photo = models.ImageField(upload_to='photos')
    photo_1 = models.ImageField(upload_to='photos')
    photo_2 = models.ImageField(upload_to='photos')
    photo_3 = models.ImageField(upload_to='photos')
    photo_4 = models.ImageField(upload_to='photos')

    def __str__(self):
        return self.title
