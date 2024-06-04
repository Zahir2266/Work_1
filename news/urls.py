from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'filter', NewsViewFilter, basename='filter')
router.register(r'n_list', ForModeration, basename='n_list')

urlpatterns = [
    path('router/', include(router.urls), name='newsfilter'),
]

