from rest_framework import serializers

from authentication.serializers.user import UserBasicSerializer
from gym.models.activity_schedule import ActivitySchedule
from gym.serializers.activity import ActivitySerializer
from gym.serializers.activity_modality import ActivityModalitySerializer
from gym.serializers.activity_plan import ActivityPlanSerializer


class ActivityScheduleSerializer(serializers.ModelSerializer):
    coach = UserBasicSerializer(read_only = True)
    activity = ActivitySerializer(read_only = True)

    class Meta: 
        model = ActivitySchedule
        fields = '__all__'
