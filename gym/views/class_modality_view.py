from rest_framework import viewsets
from gym.models.class_modality import ClassModality
from gym.serializers.class_modality_serializer import ClassModalitySerializer

class ClassModalityViewSet(viewsets.ModelViewSet):
    queryset = ClassModality.objects.all()
    serializer_class = ClassModalitySerializer
