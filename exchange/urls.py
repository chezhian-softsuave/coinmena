from django.urls import path

from exchange.views import ExchangeRateGenericAPIView

urlpatterns = [
    path('quotes/', ExchangeRateGenericAPIView.as_view(), name='quotes')
]
