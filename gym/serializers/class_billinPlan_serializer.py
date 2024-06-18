from rest_framework import serializers
from gym.models.class_billingPlan import BillingPlan

class BillingPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingPlan
        fields = '__all__'


