from django.db import models

from common.models.mixins import GeolocationMixin


class Cafe(GeolocationMixin):
    address = models.TextField('Адрес кофейни')
    barista_number = models.PositiveSmallIntegerField('Число бариста на смене', default=0)

    class Meta:
        verbose_name = 'Кофейня'
        verbose_name_plural = 'Кофейни'
        ordering = ('barista_number', )

    def __str__(self):
        return self.address

