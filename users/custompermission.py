from rest_framework.permissions import BasePermission
from .models import UserRole


class IOperator(BasePermission):
    message = 'ВЫ не оператор'

    def has_permission(self, request, view):
        return request.user.role == UserRole.OPERATOR


class IModerator(BasePermission):
    message = 'ВЫ не модер'

    def has_permission(self, request, view):
        return request.user.role == UserRole.MODERATOR


class IAuthor(BasePermission):
    message = 'ВЫ не автор'

    def has_permission(self, request, view):
        return request.user.role == UserRole.AUTHOR
