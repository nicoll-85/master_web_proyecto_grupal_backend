from rest_framework import serializers
from gym.models.billing_plan import BillingPlan


class BillingPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingPlan
        fields = '__all__'
