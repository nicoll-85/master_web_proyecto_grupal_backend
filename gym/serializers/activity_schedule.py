from rest_framework import serializers
from gym.models.activity_schedule import ActivitySchedule


class ActivityScheduleSerializer(serializers.ModelSerializer):
    class Meta: 
        model = ActivitySchedule
        fields = '__all__'
