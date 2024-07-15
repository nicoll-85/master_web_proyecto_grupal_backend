from rest_framework import viewsets
from gym.models.class_schedule import ClassSchedule
from gym.serializers.class_schedule_serializer import ClassScheduleSerializer

class ClassScheduleViewSet(viewsets.ModelViewSet):
    queryset = ClassSchedule.objects.all()
    serializer_class = ClassScheduleSerializer
