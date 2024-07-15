from rest_framework import viewsets

from gym.models.activity import Activity
from gym.serializers.activity import ActivitySerializer


class ActivityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

