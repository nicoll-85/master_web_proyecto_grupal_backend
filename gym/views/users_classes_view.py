from rest_framework import viewsets
from gym.models.users_classes import UsersClasses
from gym.serializers.users_classes_serializer import UsersClassesSerializer

class UsersClassesViewSet(viewsets.ModelViewSet):
    queryset = UsersClasses.objects.all()
    serializer_class = UsersClassesSerializer