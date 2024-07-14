from rest_framework import serializers
from gym.models.activity import Activity
from gym.serializers.activity_modality import ActivityModalitySerializer
from gym.serializers.activity_plan import ActivityPlanSerializer


class ActivitySerializer(serializers.ModelSerializer):
    modality = ActivityModalitySerializer(read_only = True)
    plan = ActivityPlanSerializer(read_only = True)
    class Meta: 
        model = Activity
        fields = '__all__'
