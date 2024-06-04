from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'news', NewsViewFilter)

urlpatterns = [
    path('filter/', include(router.urls), name='newsfilter')

]