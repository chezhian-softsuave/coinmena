from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from exchange.api import exchange_api, insert_data
from exchange.models import ExchangeRate
from exchange.serializers import ExchangeRateSerializer, ExchangeRateDataSerializer


class ExchangeRateGenericAPIView(APIView):
    @swagger_auto_schema(responses={200: ExchangeRateSerializer()})
    def get(self, request):
        try:
            er = ExchangeRate.objects.get()
        except ExchangeRate.DoesNotExist:
            return Response({}, status=status.HTTP_200_OK)
        serializer = ExchangeRateSerializer(er)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={201: ExchangeRateDataSerializer()},
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'from_currency_code': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
                'to_currency_code': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
            })
    )
    def post(self, request):
        serializer = ExchangeRateDataSerializer(data=self.request.data)
        if serializer.is_valid():
            response, status_code = exchange_api(
                from_currency=serializer['from_currency_code'].value,
                to_currency=serializer['to_currency_code'].value
            )
            er = insert_data(response)
            return Response({'exchange_data': er.exchange_rate}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
