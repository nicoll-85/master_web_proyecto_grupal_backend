from rest_framework import viewsets

from gym.models.activity_plan import ActivityPlan
from gym.serializers.activity_plan import ActivityPlanSerializer


class ActivityPlanViewSet(viewsets.ModelViewSet):
    queryset = ActivityPlan.objects.all()
    serializer_class = ActivityPlanSerializer
