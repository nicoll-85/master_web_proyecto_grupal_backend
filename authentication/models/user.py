from django.contrib.auth.models import AbstractUser
from django.db import models

from gym.models.billing_plan import BillingPlan


class User(AbstractUser):
    billing_plan = models.ForeignKey(BillingPlan, on_delete=models.CASCADE, blank = True)
    pass
