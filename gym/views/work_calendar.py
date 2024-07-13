from rest_framework import viewsets
from gym.models.work_calendar import WorkCalendar
from gym.serializers.work_calendar import WorkCalendarSerializer


class WorkCalendarViewSet(viewsets.ModelViewSet):
    queryset = WorkCalendar.objects.all()
    serializer_class = WorkCalendarSerializer
