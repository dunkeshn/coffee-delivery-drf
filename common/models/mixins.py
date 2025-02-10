from django.utils import timezone

from django.db import models

from config import settings


class DateMixin(models.Model):
    created_at = models.DateTimeField(
        'Дата и время создания', null=True
    )
    updated_at = models.DateTimeField('Дата и время обновления', null=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.pk and not self.created_at:
            self.created_at = timezone.now()
        self.update_at = timezone.now()
        return super(DateMixin, self).save(*args, **kwargs)


class InfoMixin(DateMixin):
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, models.SET_NULL, 'created_%(app_label)s_%(class)s',
        verbose_name='Создано пользователем', null=True
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, models.SET_NULL, 'updated_%(app_label)s_%(class)s',
        verbose_name='Обновлено пользователем', null=True,
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        from crum import get_current_user
        user = get_current_user()

        if user and not user.pk:
            user = None
        if not self.pk:
            self.created_by = user
        self.updated_by = user
        super().save(*args, **kwargs)


class GeolocationMixin(models.Model):
    latitude = models.FloatField('Широта', blank=True, null=True)
    longitude = models.FloatField('Долгота', blank=True, null=True)

    class Meta:
        abstract = True