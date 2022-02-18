from datetime import date, timedelta
from yahoo_fin.stock_info import get_data
from django.core.management.base import BaseCommand

from portfolio.models import StockRate
from portfolio.models import Transaction


class Command(BaseCommand):
    help = 'Sync all the stock prices'

    def handle(self, *args, **options):
        transactions = Transaction.objects.all()
        end_date = date.today() + timedelta(1)
        for transaction in transactions:
            stock_data = get_data(transaction.stock.symbol, start_date=transaction.date, end_date=end_date)
            for stock_date, row in stock_data.iterrows():
                self.create_stock_rate_if_not_exists(stock_date, transaction.stock, row)

        self.stdout.write(self.style.SUCCESS('All done!'))

    def create_stock_rate_if_not_exists(self, date, stock, stock_data):
        # First check if this rate doesn't already exist.
        stock_rate_exists = StockRate.objects.filter(date=date, stock=stock).exists()
        if stock_rate_exists:
            self.stdout.write('%s (%s) already exists' % (stock, date))
            return

        stock_rate = StockRate(
            stock=stock,
            date=date,
            rate=stock_data.close
        )
        stock_rate.save()
