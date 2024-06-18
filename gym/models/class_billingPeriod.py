from django.db import models

class BillingPeriod(models.Model):
    id = models.AutoField(primary_key=True)
    fee = models.FloatField()
    payment_date = models.DateField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    #user_id = models.ForeignKey(BillingPlan, on_delete=models.CASCADE)

    def __str__(self):
        return self.payment_date
        #f"{self.user_id.name} - {self.payment_date}"