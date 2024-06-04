import django_filters
from .models import *


class NewsFilter(django_filters.FilterSet):
    # author = django_filters.ChoiceFilter(choices=News.NewsStatus, label='статус')

    class Meta:
        model = News
        fields = '__all__'
