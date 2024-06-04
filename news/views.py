from rest_framework import permissions, viewsets, status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from django_filters import rest_framework as filters
from rest_framework.decorators import action

from .models import News
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

    @action(detail=True, methods=['get', 'put'], )#permissions=(IOperator,)
    def do_for_moder(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        instance = News.objects.get(pk=pk)

        serializer = NewsSerializer(data=request.data, instance=instance) #

        if serializer.is_valid():
            # serializer.save()
            return Response({"post": " Вроде норм"})
        else:
            return Response({"post": pk})

    @action(detail=True, methods=['get', 'put'], ) # permissions=(IModerator,)
    def do_for_post(self, request, *args, **kwargs):
        if request.user.UserRole == "Moderator":
            pass
        pass

    @action(detail=True, methods=['get', 'put'], ) # permissions=(IOReader,)
    def do_post(self, request, *args, **kwargs):
        if request.user.UserRole == "Reader":
            pass
        pass
