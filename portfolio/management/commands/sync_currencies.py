from django.core.management.base import BaseCommand
from portfolio.models.currency import Currency


class Command(BaseCommand):
    help = 'Sync all the currencies'

    def add_arguments(self, parser):
        parser.add_argument('currency_code', type=str)

    def handle(self, *args, **options):
        currency_code = options['currency_code']
        currency = Currency()
        currency.code = currency_code
        currency.save()
