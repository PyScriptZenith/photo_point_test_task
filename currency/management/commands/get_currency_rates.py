import time

from django.core.management import BaseCommand
import requests

from config import settings
from currency.models import Currency


class Command(BaseCommand):

    """Кастомная команда парсинга курса USD/RUR"""

    def handle(self, *args, **options):
        API_KEY = settings.API_KEY

        # Очищаем БД перед заполнением

        Currency.objects.all().delete()

        # Формируем историю запросов

        for x in range(10):
            last_10_rates = requests.get(
            f'https://openexchangerates.org/api/latest.json?app_id={API_KEY}&base=USD&symbols=RUB').json()
            time.sleep(10)
            exchange_rate = last_10_rates['rates']['RUB']
            Currency.objects.create(exchange_rate=exchange_rate)

        # Получаем актуальный курс

        curent_rate = requests.get(
            f'https://openexchangerates.org/api/latest.json?app_id={API_KEY}&base=USD&symbols=RUB').json()

        current_exchange_rate = curent_rate['rates']['RUB']
        Currency.objects.create(exchange_rate=current_exchange_rate, is_current_rate=True)

