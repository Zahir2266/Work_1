# Generated by Django 5.0.6 on 2024-06-03 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.TextField(choices=[('Operator', 'Автор'), ('Moderator', 'Модер'), ('Reader', 'Пользователь')], default='Reader', verbose_name='Роль'),
        ),
    ]
