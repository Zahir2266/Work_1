from rest_framework import permissions, viewsets, status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from django_filters import rest_framework as filters

from .models import News
from .serializers import NewsSerializer
from .filters import NewsFilter
from django.http import Http404


class NewsViewFilter(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filterset_class = NewsFilter
    filter_backends = (filters.DjangoFilterBackend,)
    # ordering_fields = ['title', 'author', 'slug']

    def get_queryset(self):
        return News.objects.filter(title='1')

    def get(self, request, *args, **kwargs):
        news = self.get_queryset()
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)

    # def post(self, request, format=None):
    #     serializer = NewsSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
