from django.contrib.auth import get_user_model
from django.db import models

import blog
from api import apps


class Profile(models.Model):

    class AuthorStatus(models.TextChoices):
        READER = 'READER', 'Читатель',
        WRITER = 'WRITER', 'Писатель',

    user = models.OneToOneField('users.User',
                                on_delete=models.CASCADE,
                                related_name='profile',
                                verbose_name='Пользователь',
                                primary_key=True,
                                )
    telegram_id = models.CharField('Telegram', max_length=64, null=True, blank=True)
    beans = models.IntegerField('Зерна', default=0)
    author_status = models.CharField('Статус автора', max_length=100, choices=AuthorStatus.choices,
                                     default=AuthorStatus.READER)
    liked_posts = models.ManyToManyField('blog.Post', blank=True, verbose_name='Понравившиеся статьи', related_name='liked_posts')

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'

    def __str__(self):
        return f'{self.user} {self.pk}'
