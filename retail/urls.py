from django.urls import path

from retail.apps import RetailConfig
from retail.views import TraderDetailView

app_name = RetailConfig.name

urlpatterns = [
    #  Модель звена торговой сети
    path('trader/<int:pk>/', TraderDetailView.as_view(), name='trader_detail'),
]
