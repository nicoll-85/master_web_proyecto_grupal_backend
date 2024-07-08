from rest_framework import serializers

from gym.models.activity import Activity
from gym.serializers.activity_schedule import ActivityScheduleSerializer


class ActivitySerializer(serializers.ModelSerializer):
    schedules = ActivityScheduleSerializer(read_only = True, many = True)

    class Meta:
        model = Activity
        fields = '__all__'
