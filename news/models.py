from django.db import models

from users.models import *


class NewsStatus(models.IntegerChoices):
    Draft = (1, 'Черновик')
    Moderation = (2, 'На модерации')
    ReadyPublication = (3, 'Готов к публикации')
    Publish = (4, 'Опубликован')


class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    status = models.IntegerField(
        choices=NewsStatus.choices,
        default=NewsStatus.Draft,
        verbose_name='Статус')

    author = models.ForeignKey(to=User, on_delete=models.CASCADE,
                               related_name='authors',
                               verbose_name='authors')
    moderator = models.ForeignKey(to=User, on_delete=models.CASCADE,
                                  related_name='moderators',
                                  verbose_name='Модер')

    def __str__(self):
        return self.title
