from rest_framework import serializers

from authentication.models import User
from gym.serializers.billing_plan import BillingPlanSerializer


class UserSerializer(serializers.ModelSerializer):
    billing_plan = BillingPlanSerializer()
    class Meta:
        model = User
        fields = '__all__'
