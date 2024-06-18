from rest_framework import serializers
from gym.models.class_work_calendar import WorkCalendar


class WorkCalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkCalendar
        fields = '__all__'