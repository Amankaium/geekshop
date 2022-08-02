from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = "Категории"


# Create your models here.
class Vegetables(models.Model):
    name = models.CharField(max_length=255)
    calories = models.IntegerField(default=0)
    price = models.PositiveIntegerField(default=1)
    is_avialable = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(
        to=Category, null=True, blank=True, related_name='vegetables',
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return f"{self.id} - {self.name}"


