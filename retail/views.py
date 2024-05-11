from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from retail.models import Trader, Network, Product
from retail.serializers import TraderSerializer, NetworkSerializer, ProductSerializer
from users.permissions import UserIsActive


class TraderListCreateView(generics.ListCreateAPIView):
    """Контроллер создания звена торговой сети и просмотра списка уже существующих звеньев"""
    serializer_class = TraderSerializer
    queryset = Trader.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('country',)
    permission_classes = [UserIsActive]


class TraderDetailUpgateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """Контроллер просмотра, редактирования и удаления звена торговой сети"""
    serializer_class = TraderSerializer
    queryset = Trader.objects.all()
    permission_classes = [UserIsActive]


class NetworkViewSet(ModelViewSet):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer
    permission_classes = [UserIsActive]


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [UserIsActive]
