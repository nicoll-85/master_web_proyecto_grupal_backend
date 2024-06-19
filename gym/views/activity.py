from rest_framework import viewsets

from gym.models.activity import Activity
from gym.serializers.activity import ActivitySerializer


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
