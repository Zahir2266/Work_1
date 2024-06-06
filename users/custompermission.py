import requests.models
import mypy_django_plugin.transformers.request as myrequest
from rest_framework.permissions import BasePermission
from .models import *


def requested(request) -> User:
    return request.user


class IOperator(BasePermission):
    message = 'ВЫ не оператор'

    def has_permission(self, request: myrequest, view) -> bool:
        return request.user.role == UserRole.OPERATOR


class IModerator(BasePermission):
    message = 'ВЫ не модер'

    def has_permission(self, request: myrequest, view) -> bool:
        return request.user.role == UserRole.MODERATOR


class IAuthor(BasePermission):
    message = 'ВЫ не автор'

    def has_permission(self, request: myrequest, view) -> bool:
        return request.user.role == UserRole.AUTHOR
