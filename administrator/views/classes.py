from rest_framework import viewsets
from administrator.models.Classes import Classes
from rest_framework.permissions import IsAuthenticated
from administrator.serializers.Classes import ClassesSerializer
from gym.models.activity_schedule import ActivitySchedule
from gym.serializers.activity_schedule import ActivityScheduleSerializer


class ClassesViewSet(viewsets.ModelViewSet):
    queryset = Classes.objects.all()
    serializer_class = ClassesSerializer
    permission_classes = [IsAuthenticated]

    def __str__(self):
        return self.name






    # queryset = .objects.select_related('activity__modality', 'coach').all()
    # serializer_class = ActivityScheduleSerializer, ClassesSerializer
    # permission_classes = [IsAuthenticated]
    #
    # def __str__(self):
    #     return self.name
