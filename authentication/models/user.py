from django.contrib.auth.models import AbstractUser
from django.db import models

from gym.models.billing_plan import BillingPlan


class User(AbstractUser):
    phone = models.CharField(max_length = 20, null = True)
    title = models.CharField(max_length = 50, null = True)
    description = models.TextField(null = True)
    billing_plan = models.ForeignKey(BillingPlan, on_delete=models.CASCADE, null = True,blank = True)

    def get_billing_periods(self):
        return self.billingperiod_set.all()
