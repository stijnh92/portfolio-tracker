from django.db import models
from .stock import Stock


class CashTransaction(models.Model):
    date = models.DateField()
    type = models.CharField(max_length=16)
    total = models.FloatField()
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f'{self.type} - EUR {self.total}'
