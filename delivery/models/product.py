from django.contrib.auth.models import User
from django.db import models

from common.models.mixins import InfoMixin


class Product(InfoMixin):

    class Category(models.TextChoices):
        DRINK = 'DRINK', 'Напиток'
        DESSERT = 'DESSERT', 'Десерт'
        HOT = 'HOT', 'Горячее блюдо'

    class Availability(models.TextChoices):
        ABSENT = 'ABSENT', 'Товар отсутствует'
        AVAILABLE = 'AVAILABLE', 'В наличии'

    name = models.CharField('Название товара', max_length=255)
    price = models.DecimalField('Цена товара', max_digits=10, decimal_places=2)
    description = models.TextField('Описание товара', null=True, blank=True)
    category = models.CharField('Категория товара', max_length=100, choices=Category.choices, null=True, default=Availability.AVAILABLE)
    availability = models.CharField('Наличие', max_length=100, choices=Availability.choices, default=Availability.AVAILABLE)
    image = models.ImageField('Фотография товара', blank=True, null=True)
    rating = models.FloatField('Рейтинг товара', blank=True, null=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('created_at', )

    def __str__(self):
        return self.name
