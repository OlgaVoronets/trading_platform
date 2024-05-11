from rest_framework import serializers

from retail.models import Network, Trader, Product


class NetworkSerializer(serializers.ModelSerializer):
    """Базовый сериализатор для модели торговой сети"""

    class Meta:
        model = Network
        fields = '__all__'


class TraderSerializer(serializers.ModelSerializer):
    """Базовый сериализатор для модели звена торговой сети
    Поле задолженности перед поставщиком запрещено для редактирования
    список продуктов для звена выводится по наименованиям (не id)"""
    products = serializers.StringRelatedField(many=True)

    class Meta:
        model = Trader
        fields = '__all__'
        read_only_fields = ('debt',)


class ProductSerializer(serializers.ModelSerializer):
    """Базовый сериализатор для модели продукта"""

    class Meta:
        model = Product
        fields = '__all__'
