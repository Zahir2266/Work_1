from django.db import models

from users.models import *


# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    class NewsStatus(models.IntegerChoices):
        Draft = (1, 'Draft')
        Moderation = (2, 'Moderation')
        ReadyPublication = (3, 'ReadyPublication')
        Publish = (4, 'Publish')

    status = models.IntegerField(
        choices=NewsStatus.choices,
        default=NewsStatus.Draft,
        verbose_name='Статус')

    author = models.ForeignKey(to=User, on_delete=models.CASCADE,
                               related_name='authors',
                               verbose_name='Статус')
    moderator = models.ForeignKey(to=User, on_delete=models.CASCADE,
                                  related_name='moderators',
                                  verbose_name='Модер')
