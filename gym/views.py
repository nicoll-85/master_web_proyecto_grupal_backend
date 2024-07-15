from rest_framework import viewsets
from .models import ClassPlan, ClassModality, Classes, ClassSchedule, UsersClasses
from .serializers import ClassPlanSerializer, ClassModalitySerializer, ClassesSerializer, ClassScheduleSerializer, UsersClassesSerializer

class ClassPlanViewSet(viewsets.ModelViewSet):
    queryset = ClassPlan.objects.all()
    serializer_class = ClassPlanSerializer

class ClassModalityViewSet(viewsets.ModelViewSet):
    queryset = ClassModality.objects.all()
    serializer_class = ClassModalitySerializer

class ClassesViewSet(viewsets.ModelViewSet):
    queryset = Classes.objects.all()
    serializer_class = ClassesSerializer

class ClassScheduleViewSet(viewsets.ModelViewSet):
    queryset = ClassSchedule.objects.all()
    serializer_class = ClassScheduleSerializer

class UsersClassesViewSet(viewsets.ModelViewSet):
    queryset = UsersClasses.objects.all()
    serializer_class = UsersClassesSerializer
