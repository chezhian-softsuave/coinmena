from rest_framework import serializers

from exchange.models import ExchangeRate


class ExchangeRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeRate
        fields = ('from_currency_code', 'from_currency_name',
                  'to_currency_code', 'to_currency_name',
                  'exchange_rate',
                  'last_refreshed', 'time_zone',)


class ExchangeRateDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeRate
        fields = ('from_currency_code', 'to_currency_code')
