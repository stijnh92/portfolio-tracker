from django.db import models


class Stock(models.Model):
    symbol = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=256)

    class Meta:
        ordering = ['symbol']

    def __str__(self):
        return f'{self.name} ({self.symbol})'
