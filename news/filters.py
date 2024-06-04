import django_filters
from .models import *


class NewsFilter(django_filters.FilterSet):
    author = django_filters.ChoiceFilter(choices=News.NewsStatus, label='Статус')

    class Meta:
        model = News
        fields = '__all__'
