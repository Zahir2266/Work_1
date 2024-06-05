from django.db import models
from django.contrib.auth.models import AbstractUser
from .custompermission import *


class UserRole(models.TextChoices):
    """
    class containing - the main roles for working with access
    """
    OPERATOR = 'Operator', 'Автор'
    MODERATOR = 'Moderator', 'Модер'
    READER = 'Reader', 'Пользователь'


class User(AbstractUser):
    name3 = models.CharField(max_length=100, unique=True, verbose_name='Отчетсво')

    role = models.TextField(
        choices=UserRole.choices,
        default=UserRole.READER,
        verbose_name='Роль')

    def __str__(self):
        return self.username
