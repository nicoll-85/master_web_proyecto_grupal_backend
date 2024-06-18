from rest_framework import viewsets
from gym.models.classes import Classes
from gym.serializers.classes_serializer import ClassesSerializer

class ClassesViewSet(viewsets.ModelViewSet):
    queryset = Classes.objects.all()
    serializer_class = ClassesSerializer