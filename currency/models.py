from django.db import models


class Currency(models.Model):
    currency_from = models.CharField(max_length=5, default='USD')
    currency_to = models.CharField(max_length=5, default='RUR')
    exchange_rate = models.DecimalField(max_digits=10, decimal_places=6)
    rate_time = models.DateTimeField(auto_now_add=True)
    is_current_rate = models.BooleanField(default=False)

    def __str__(self):
        return f"Курс на {self.rate_time} {self.currency_from} --> {self.currency_to}: {self.exchange_rate}"

    class Meta:
        verbose_name = "курс валют"
        verbose_name_plural = "курсы валют"
        ordering = ['-is_current_rate', '-rate_time']