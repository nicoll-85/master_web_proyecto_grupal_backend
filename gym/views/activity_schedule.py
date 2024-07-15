from rest_framework import viewsets

from gym.models.activity_schedule import ActivitySchedule
from gym.serializers.activity_schedule import ActivityScheduleSerializer


class ActivityScheduleViewSet(viewsets.ModelViewSet):
    queryset = ActivitySchedule.objects.all()
    serializer_class = ActivityScheduleSerializer
