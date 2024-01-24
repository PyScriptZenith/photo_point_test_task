from rest_framework.generics import ListAPIView

from currency.models import Currency
from currency.serializers import CurrencySerializer



class CurrencyListAPIView(ListAPIView):
    serializer_class = CurrencySerializer
    queryset = Currency.objects.all()

