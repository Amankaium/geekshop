from django.db import models


# Create your models here.
class Vegetables(models.Model):
    name = models.CharField(max_length=255)
    calories = models.IntegerField(default=0)
    price = models.PositiveIntegerField(default=1)
    is_avialable = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True)
