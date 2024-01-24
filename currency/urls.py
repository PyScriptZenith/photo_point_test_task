from currency.apps import CurrencyConfig
from django.urls import path

from currency.views import CurrencyListAPIView

app_name = CurrencyConfig.name

urlpatterns = [
    path("get-current-usd/", CurrencyListAPIView.as_view(), name="get-current-usd")
]
