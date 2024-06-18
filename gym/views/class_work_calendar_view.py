from rest_framework import viewsets
from gym.models.class_work_calendar import WorkCalendar
from gym.serializers.class_work_calendar_serializer import WorkCalendarSerializer


class WorkCalendarViewSet(viewsets.ModelViewSet):
    queryset = WorkCalendar.objects.all()
    serializer_class = WorkCalendarSerializer
