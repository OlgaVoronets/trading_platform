from rest_framework import permissions


class UserIsActive(permissions.BasePermission):
    """Только активные сотрудники имеют доступ к API."""
    message = "Доступно только действующим сотрудникам"

    def has_permission(self, request, view):
        return request.user.is_active
