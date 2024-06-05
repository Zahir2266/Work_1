from rest_framework import permissions, viewsets, status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from django_filters import rest_framework as filters
from rest_framework.decorators import action

from .models import *
from .serializers import NewsSerializer
from .filters import NewsFilter
from users.custompermission import *
from django.http import Http404


class NewsViewFilter(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    filterset_class = NewsFilter
    filter_backends = (filters.DjangoFilterBackend,)


class ForModeration(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    @action(detail=False)
    def list_news(self, request):
        list = News.objects.all().order_by('title')

        page = self.paginate_queryset(list)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(list, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['GET', 'PUT'], permission_classes=[permissions.IsAuthenticated])
    def redact(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        instance = News.objects.get(pk=pk)

        try:
            news = News.objects.get(pk=pk)
        except News.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        news.status = NewsStatus.Moderation
        news.save()

        return Response({"новый статус": news.status}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['GET', 'PUT'], permission_classes=[permissions.IsAuthenticated])
    def moderation(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        instance = News.objects.get(pk=pk)

        try:
            news = News.objects.get(pk=pk)
        except News.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        news.status = NewsStatus.Moderation
        news.save()

        return Response({"новый статус": news.status}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['GET', 'PUT'], permission_classes=[permissions.IsAuthenticated])
    def publication(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        instance = News.objects.get(pk=pk)

        try:
            news = News.objects.get(pk=pk)
        except News.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        news.status = NewsStatus.Moderation
        news.save()

        return Response({"новый статус": news.status}, status=status.HTTP_200_OK)
