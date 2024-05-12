from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Отображение торговой сети в панели администратора"""
    list_display = ('id', 'email', 'is_active', 'is_superuser')
