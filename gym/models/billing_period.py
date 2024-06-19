from django.db import models


class BillingPeriod(models.Model):
    fee = models.FloatField()
    payment_date = models.DateField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    client = models.ForeignKey('authentication.User', on_delete=models.CASCADE)

    class Meta:
        ordering = ['payment_date']
        verbose_name = 'period'
        verbose_name_plural = 'periods'

    def __str__(self):
        return self.payment_date

