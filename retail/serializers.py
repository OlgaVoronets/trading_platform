from rest_framework import serializers

from retail.models import Network


class NetworkSerializer(serializers.ModelSerializer):
    """Базовый сериализатор для модели торговой сети"""

    class Meta:
        model = Network
        fields = '__all__'
