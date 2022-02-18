from django.db import models


class Currency(models.Model):
    code = models.CharField(max_length=3)
    symbol = models.CharField(max_length=1)
    rate = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return f'{self.code} {self.rate} ({self.date})'

    class Meta:
        ordering = ['-date']
        verbose_name_plural = "currencies"
