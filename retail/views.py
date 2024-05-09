from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView

from retail.models import Trader
from retail.serializers import TraderSerializer


class TraderDetailView(generics.RetrieveAPIView):
    serializer_class = TraderSerializer
    queryset = Trader.objects.all()
