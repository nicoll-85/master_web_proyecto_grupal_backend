from rest_framework import serializers

from authentication.models import User
from gym.serializers.billing_plan import BillingPlanSerializer
from gym.models.billing_plan import BillingPlan


class UserSerializer(serializers.ModelSerializer):
    billing_plan = BillingPlanSerializer(read_only = True)


    class Meta:
        model = User
        fields = '__all__'

    def update(self, instance, validated_data):
        modality = validated_data.pop('modality', None)
        plan = validated_data.pop('plan', None)
        if modality and plan:
            try:
                billing_plan = BillingPlan.objects.get(modality_id=modality, plan_id=plan)
                instance.billing_plan = billing_plan
            except BillingPlan.DoesNotExist:
                raise serializers.ValidationError("Invalid modality or plan")
        return super().update(instance, validated_data)


class UserBasicSerializer(serializers.ModelSerializer):
    billing_plan = BillingPlanSerializer(read_only = True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'phone',
                  'date_joined', 'title', 'description', 'billing_plan', 'groups']

