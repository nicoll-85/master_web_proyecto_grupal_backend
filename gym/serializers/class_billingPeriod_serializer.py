from rest_framework import serializers
from gym.models.class_billingPeriod import BillingPeriod


class BillingPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingPeriod
        fields = '__all__'
