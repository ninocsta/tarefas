from celery import shared_task
from .models import Stock


@shared_task
def create_stock():
    Stock.objects.create(name='AAPL', price=100.0)
    return f'Stock AAPL created'