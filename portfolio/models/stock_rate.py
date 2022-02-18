from django.db import models
from .stock import Stock


class StockRate(models.Model):
    date = models.DateField()
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, null=True, blank=True)
    rate = models.FloatField()

    class Meta:
        ordering = ['-date']
        unique_together = ('date', 'stock')
