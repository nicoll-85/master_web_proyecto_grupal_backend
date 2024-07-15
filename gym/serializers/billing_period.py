from rest_framework import serializers
from gym.models.billing_period import BillingPeriod


class BillingPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingPeriod
        fields = '__all__'
