from django.db import models

from blog.models.comment import Comment
from common.models.mixins import DateMixin
from users.models.users import User


class Post(DateMixin):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='posts', verbose_name = 'Автор', )
    title = models.CharField('Название статьи', max_length=100)
    text = models.TextField('Текст статьи')
    image = models.ImageField('Фото статьи', blank=True, null=True, upload_to='pictures')
    likes = models.IntegerField('Количество лайков', default=0)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ('-created_at', )

    def __str__(self):
        return f'Статья "{self.title}" - автор: {self.author}'