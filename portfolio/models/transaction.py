from django.db import models
from .stock import Stock
from .stock_rate import StockRate
from .currency import Currency


class Transaction(models.Model):
    ACTION_CHOICES = [
        ('buy', 'Buy'),
        ('sell', 'Sell')
    ]
    date = models.DateField()
    action = models.CharField(max_length=10, choices=ACTION_CHOICES)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()
    costs = models.FloatField()
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, null=True, blank=True)

    @property
    def subtotal(self):
        return round((self.quantity * self.price + self.costs), 2)

    @property
    def cost_per_share(self):
        return round((self.subtotal / self.quantity), 2)

    @property
    def currency_code(self):
        return self.currency and self.currency.symbol or '€'

    @property
    def average_cost(self):
        return self.price + self.costs / self.quantity

    @property
    def diff_percentage(self):
        return - (1 - self.current_rate / self.average_cost) * 100

    @property
    def current_rate(self):
        stock_rate = StockRate.objects.filter(stock=self.stock)[0]
        return stock_rate.rate

    @property
    def total(self):
        if self.currency:
            return round((self.subtotal / self.currency.rate), 2)

        return self.subtotal

    class Meta:
        ordering = ['-date']
