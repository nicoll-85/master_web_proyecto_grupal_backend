from django.db import models

from gym.models.activity_modality import ActivityModality
from gym.models.activity_plan import ActivityPlan


class BillingPlan(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    plan = models.ForeignKey(ActivityPlan, on_delete=models.CASCADE) # Básico, intermedio, avanzado
    modality = models.ForeignKey(ActivityModality, on_delete=models.CASCADE) #Virtual o presencial

    class Meta:
        ordering = ['name']
        verbose_name = 'billing_plan'
        verbose_name_plural = 'billing_plans'

    def __str__(self):
        return self.name
