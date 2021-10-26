import requests

from cryptocurrency.settings import ALPHAVANTAGE_API_KEY
from exchange.models import ExchangeRateLog


def insert_data(response):
    """
    Insert data in the database
    :return: object instance
    """
    currency_exchange_rate = response['Realtime Currency Exchange Rate']
    exchange = ExchangeRateLog.objects.create(
        from_currency_code=currency_exchange_rate['1. From_Currency Code'],
        from_currency_name=currency_exchange_rate['2. From_Currency Name'],
        to_currency_code=currency_exchange_rate['3. To_Currency Code'],
        to_currency_name=currency_exchange_rate['4. To_Currency Name'],
        exchange_rate=currency_exchange_rate['5. Exchange Rate'],
        last_refreshed_time=currency_exchange_rate['6. Last Refreshed'],
        time_zone=currency_exchange_rate['7. Time Zone'],
        bid_price=currency_exchange_rate['8. Bid Price'],
        ask_price=currency_exchange_rate['9. Ask Price']
    )
    return exchange


def exchange_api(from_currency='BTC', to_currency='USD'):
    """
    Get data from alphavantage api
    :return: api response json
    """

    url = "https://www.alphavantage.co/query"
    params = {
        'function': 'CURRENCY_EXCHANGE_RATE',
        'from_currency': from_currency,
        'to_currency': to_currency,
        'apikey': ALPHAVANTAGE_API_KEY
    }
    response = requests.get(url=url, params=params)
    return response.json(), response.status_code
