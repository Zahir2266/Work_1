from django.db import models
from django.contrib.auth.models import AbstractUser
from .custompermission import *


class User(AbstractUser):
    name3 = models.CharField(max_length=100, unique=True, verbose_name='Отчетсво')

    class UserRole(models.TextChoices):
        OPERATOR = 'Operator', 'Автор'
        MODERATOR = 'Moderator', 'Модер'
        READER = 'Reader', 'Пользователь'

    role = models.TextField(
        choices=UserRole.choices,
        default=UserRole.READER,
        verbose_name='Роль')

    def __str__(self):
        return self.username
