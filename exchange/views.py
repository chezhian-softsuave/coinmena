from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from exchange.api import exchange_api, insert_data
from exchange.models import ExchangeRate
from exchange.serializers import ExchangeRateSerializer, ExchangeRateDataSerializer


class ExchangeRateGenericAPIView(APIView):
    def get(self, request):
        er = ExchangeRate.objects.all().latest('id')
        serializer = ExchangeRateSerializer(er)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ExchangeRateDataSerializer(data=self.request.data)
        if serializer.is_valid():
            response, status_code = exchange_api(
                from_currency=serializer['from_currency'].value,
                to_currency=serializer['to_currency'].value
            )
            er = insert_data(response)
            return Response({'exchange_data': er.exchange_rate}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
