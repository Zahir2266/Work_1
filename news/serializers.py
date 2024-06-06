from ctypes import cast

from rest_framework import serializers
from news.models import News


class NewsSerializer(serializers.ModelSerializer[News]):
    class Meta:
        model = News
        fields = "__all__"



