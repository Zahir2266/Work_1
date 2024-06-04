from rest_framework.permissions import BasePermission, SAFE_METHODS


class IOperator(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class IModerator(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class IOReader(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
