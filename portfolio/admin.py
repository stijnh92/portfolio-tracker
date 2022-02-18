from django.contrib import admin
from portfolio.models import CashTransaction, Transaction, Stock, Currency, StockRate


class CashTransactionAdmin(admin.ModelAdmin):
    list_display = ('date', 'type', 'stock', 'total')
    pass


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('stock', 'date', 'quantity', 'price', 'costs', 'cost_per_share', 'subtotal', 'total')
    pass


class StockAdmin(admin.ModelAdmin):
    list_display = ('symbol', 'name')
    pass


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('code', 'date', 'rate')
    pass


class StockRateAdmin(admin.ModelAdmin):
    list_display = ('date', 'stock', 'rate')
    pass

admin.site.register(CashTransaction, CashTransactionAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(StockRate, StockRateAdmin)
