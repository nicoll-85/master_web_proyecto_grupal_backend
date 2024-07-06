from rest_framework import serializers

from gym.models.activity import Activity
from gym.serializers.activity_schedule import ActivityScheduleSerializer


class ActivitySerializer(serializers.ModelSerializer):
    schedule = ActivityScheduleSerializer()
    class Meta:
        model = Activity
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']