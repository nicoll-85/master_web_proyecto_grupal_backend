from rest_framework import serializers
from gym.models.billing_plan import BillingPlan
from gym.serializers.activity_modality import ActivityModalitySerializer
from gym.serializers.activity_plan import ActivityPlanSerializer


class BillingPlanSerializer(serializers.ModelSerializer):
    plan = serializers.CharField(source='plan.name', read_only = True)
    modality = serializers.CharField(source='modality.name', read_only = True)
    class Meta:
        model = BillingPlan
        fields = '__all__'
