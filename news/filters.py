import django_filters
from .models import *


class NewsFilter(django_filters.FilterSet):
    class Meta:
        model = News
        fields = '__all__'
