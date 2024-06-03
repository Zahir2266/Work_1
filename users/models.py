from django.db import models

from django.contrib.auth.models import AbstractUser


class Group(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Роль')

    class Meta:
        db_table = 'roles'
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'


class User(AbstractUser):
    name3 = models.CharField(max_length=100, unique=True, verbose_name='Отчетсво')

    STATUS_CHOICES = (0, 1, 2)

    group = models.ForeignKey(to=Group, on_delete=models.CASCADE, choices=STATUS_CHOICES, verbose_name='роль')
