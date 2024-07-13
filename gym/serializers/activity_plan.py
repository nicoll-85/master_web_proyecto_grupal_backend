from rest_framework import serializers
from gym.models.activity_plan import ActivityPlan


class ActivityPlanSerializer(serializers.ModelSerializer):
    class Meta: 
        model = ActivityPlan
        fields = '__all__'
