from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory
from exchange.models import ExchangeRate
from exchange.serializers import ExchangeRateSerializer
from exchange.views import ExchangeRateGenericAPIView


class ExchangeRateTest(TestCase):
    """
    Test case for adding data into database via model class
    """

    def setUp(self) -> None:
        pass

    def test_get_valid_exchange_rate(self):
        factory = APIRequestFactory()
        ex_rate = ExchangeRate.objects.get(pk=1)
        request = factory.get('/quotes/')
        view = ExchangeRateGenericAPIView.as_view()
        response = view(request)
        serializer = ExchangeRateSerializer(ex_rate)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_puppy(self):
        factory = APIRequestFactory()
        request = factory.get('/quote/')
        view = ExchangeRateGenericAPIView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
