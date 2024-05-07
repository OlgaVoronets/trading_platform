from rest_framework import generics, status
from rest_framework.response import Response

from users.models import User
from users.serializers import UserSerializer


class UserCreateView(generics.CreateAPIView):
    """Регистрация нового пользователя"""
    serializer_class = UserSerializer
