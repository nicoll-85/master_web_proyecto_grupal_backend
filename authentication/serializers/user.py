from rest_framework import serializers

from authentication.models import User
from gym.serializers.billing_plan import BillingPlanSerializer


class UserSerializer(serializers.ModelSerializer):
    billing_plan = BillingPlanSerializer(read_only = True)


    class Meta:
        model = User
        fields = '__all__'


class UserBasicSerializer(serializers.ModelSerializer):
    billing_plan = BillingPlanSerializer(read_only = True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'phone',
                  'date_joined', 'title', 'description', 'billing_plan', 'groups']

