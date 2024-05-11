from rest_framework import permissions


class UserIsActive(permissions.BasePermission):
    """Только активные сотрудники имеют доступ к API."""
    message = "Доступно только действующим сотрудникам"

    def has_permission(self, request, view):
        return request.user.is_active


class IsOwner(permissions.BasePermission):
    """Проверка прав доступа пользователя к профилю"""
    message = "Доступно владельцу"

    def has_object_permission(self, request, view, obj):
        return request.user.email == obj.email
