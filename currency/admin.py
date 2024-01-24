from django.contrib import admin

from currency.models import Currency


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('currency_from', 'currency_to', 'is_current_rate', 'exchange_rate', 'rate_time',)
