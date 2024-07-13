from rest_framework import viewsets

from gym.models.users_activities import UsersActivities
from gym.serializers.users_activities import UsersActivitiesSerializer


class UsersActivitiesViewSet(viewsets.ModelViewSet):
    queryset = UsersActivities.objects.all()
    serializer_class = UsersActivitiesSerializer
