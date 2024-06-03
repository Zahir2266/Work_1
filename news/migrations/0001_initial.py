# Generated by Django 5.0.6 on 2024-06-03 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('status', models.IntegerField(choices=[(1, 'Draft'), (2, 'Moderation'), (3, 'ReadyPublication'), (4, 'Publish')], default=1, verbose_name='Статус')),
            ],
        ),
    ]