from django.db import models

from common.models.mixins import DateMixin
from users.models.users import User


class Comment(DateMixin):
    commentator = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='commentator', verbose_name = 'Комментатор', )
    post = models.ForeignKey(
        to="blog.Post", on_delete=models.CASCADE, related_name="comments", verbose_name="Статья"
    )
    text = models.TextField('Текст комментария')
    likes = models.IntegerField('Количество лайков', default=0)
    is_changed = models.BooleanField('Изменен ли комментарий', default=False)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('-created_at', )

    def __str__(self):
        return f'Комментарий @{self.commentator}'
