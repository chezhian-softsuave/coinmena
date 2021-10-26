from django.db import models


class ExchangeRate(models.Model):
    from_currency_code = models.CharField(max_length=15)
    from_currency_name = models.CharField(max_length=50)
    to_currency_code = models.CharField(max_length=15)
    to_currency_name = models.CharField(max_length=50)
    exchange_rate = models.DecimalField(max_digits=20, decimal_places=8)
    last_refreshed = models.CharField(max_length=50)
    time_zone = models.CharField(max_length=15)
    bid_price = models.DecimalField(max_digits=20, decimal_places=8)
    ask_price = models.DecimalField(max_digits=20, decimal_places=8)

    class Meta:
        db_table = 'exchange_rate'

    def __str__(self):
        return self.exchange_rate

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(force_insert, force_update, using, update_fields)

