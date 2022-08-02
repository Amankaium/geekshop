from django.db import models


class Feedback(models.Model):
    first_name = models.CharField(max_length=255)
    rating = models.IntegerField(default=10)
    text = models.TextField(null=True, blank=True)
    contact = models.CharField(max_length=255, verbose_name='Номер или email для связи')
