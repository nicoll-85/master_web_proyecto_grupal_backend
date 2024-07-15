from rest_framework import serializers

from gym.models.activity_schedule import ActivitySchedule
from gym.serializers.activity import ActivitySerializer


class ActivityScheduleCoachSerializer(serializers.ModelSerializer):
    activity_name = serializers.CharField(source='activity.name', read_only=True)
    modality_name = serializers.CharField(source='activity.modality.name', read_only=True)
    plan_name = serializers.CharField(source='activity.plan.name', read_only=True)
    class Meta:
        model = ActivitySchedule
        fields = ['start_time', 'end_time', 'day_week', 'activity_name', 'modality_name', 'plan_name']