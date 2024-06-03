from django.db import models
from users.models import *


# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    STATUS_CHOICES = (
        (1, 'Draft'),
        (2, 'Moderation'),
        (3, 'ReadyPublication'),
        (3, 'Publish'),
    )
    status = models.IntegerField(
        choices=STATUS_CHOICES,
        verbose_name='Статус')

    author = models.ForeignKey(to=User, verbose_name='Статус')  # limit_choices_to={'group : 1'},
    moderator = models.ForeignKey(to=User, verbose_name='Модер')  # limit_choices_to={'group : 1'},
