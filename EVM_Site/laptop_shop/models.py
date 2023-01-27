from django.db import models


class Laptop(models.Model):
    photo = models.ImageField(blank=True, upload_to='img/')
    name = models.CharField(max_length=150)
    is_gaming = models.BooleanField(default=False)
    processor = models.TextField()
    graphic_card = models.TextField()
    ram = models.IntegerField()
    os = models.BooleanField(default=False)
    price = models.IntegerField(blank=True)
