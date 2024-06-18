from django.db import models


#Comentadas las líneas con FKs (hasta unir código)

class BillingPlan(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    #plan_id = models.ForeignKey('ClassPlan', on_delete=models.CASCADE, related_name="billingPlans", null=True)  # Placeholder for future model
    #modality_id = models.ForeignKey('ClassModality', on_delete=models.CASCADE, related_name="classmodalities", null=True)  # Placeholder for future model

    def __str__(self):
        return self.name