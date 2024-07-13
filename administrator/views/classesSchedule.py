from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from administrator.models import Classes
from administrator.serializers.Classes import ClassesSerializer


class ClassScheduleViewSet(viewsets.ModelViewSet):
    queryset = Classes.objects.select_related('activity_modality','activity_schedule').all()
    serializer_class = ClassesSerializer
    permission_classes = [IsAuthenticated]

    def __str__(self):
        return self.name



# class ActivityScheduleViewSet(viewsets.ModelViewSet):
# queryset = ActivitySchedule.objects.select_related('activity__modality',).all()
