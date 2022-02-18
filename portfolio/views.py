from django.shortcuts import render
from .models import Transaction


def dashboard(request):
    transactions = Transaction.objects.all()
    total = 0
    for transaction in transactions:
        total += transaction.total

    print(total)

    context = {
        'transactions': transactions,
        'total': total
    }
    return render(request, 'dashboard.html', context)


def transactions(request):
    transactions = Transaction.objects.all()
    total = 0
    current_value = 0
    for transaction in transactions:
        total += transaction.total
        if transaction.currency:
            current_value += round((transaction.current_rate * transaction.quantity / transaction.currency.rate), 2)
        else:
            current_value += transaction.current_rate * transaction.quantity

    difference = - (1 - current_value / total) * 100

    context = {
        'transactions': transactions,
        'total': total,
        'current_value': current_value,
        'difference': difference
    }
    return render(request, 'transactions.html', context)
