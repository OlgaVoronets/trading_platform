from rest_framework import generics
from users.serializers import UserSerializer


class UserCreateView(generics.CreateAPIView):
    """Регистрация нового пользователя"""
    serializer_class = UserSerializer
