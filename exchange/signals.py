from django.db.models.signals import post_save
from django.dispatch import receiver

from exchange.models import ExchangeRate, ExchangeRateLog


@receiver(post_save, sender=ExchangeRateLog)
def create_or_update_exchange_data(sender, instance, **kwargs):
    """
    Update the exchange table from log table
    :param sender: ExchangeRateLog
    :param instance: ExchangeRateLog
    :param kwargs: Any
    :return: None
    """
    exchange_count = ExchangeRate.objects.count()
    if exchange_count >= 1:
        ExchangeRate.objects.update(
            from_currency_code=instance.from_currency_code,
            from_currency_name=instance.from_currency_name,
            to_currency_code=instance.to_currency_code,
            to_currency_name=instance.to_currency_name,
            exchange_rate=instance.exchange_rate,
            last_refreshed_time=instance.last_refreshed_time,
            time_zone=instance.time_zone,
            bid_price=instance.bid_price,
            ask_price=instance.ask_price
        )
    else:
        ExchangeRate.objects.create(
            from_currency_code=instance.from_currency_code,
            from_currency_name=instance.from_currency_name,
            to_currency_code=instance.to_currency_code,
            to_currency_name=instance.to_currency_name,
            exchange_rate=instance.exchange_rate,
            last_refreshed_time=instance.last_refreshed_time,
            time_zone=instance.time_zone,
            bid_price=instance.bid_price,
            ask_price=instance.ask_price
        )
