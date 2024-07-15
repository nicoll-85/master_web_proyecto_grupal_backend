from rest_framework import viewsets

from gym.models.activity_modality import ActivityModality
from gym.serializers.activity_modality import ActivityModalitySerializer


class ActivityModalityViewSet(viewsets.ModelViewSet):
    queryset = ActivityModality.objects.all()
    serializer_class = ActivityModalitySerializer
