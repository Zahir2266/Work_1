from rest_framework.permissions import BasePermission, SAFE_METHODS


class IOperator(BasePermission):
    message = 'ВЫ не писатель'

    def has_permission(self, request, view):
        if request.User['role'] == "Operator":
            return True
        else:
            return False


class IModerator(BasePermission):
    message = 'ВЫ не модер'

    def has_permission(self, request, view):
        if request.User['role'] == "Moderator":
            return True
        else:
            return False


class IOReader(BasePermission):
    message = 'ВЫ не оператор'

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
