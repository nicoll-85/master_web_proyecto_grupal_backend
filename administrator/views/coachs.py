from http import HTTPStatus

from rest_framework import viewsets
from django.contrib.auth.models import Group
from rest_framework.decorators import action

from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from authentication.models import User
from authentication.serializers.user import UserSerializer
from gym.models.activity_schedule import ActivitySchedule
from gym.serializers.activity_schedule import ActivityScheduleSerializer


class CoachAdminViewSet(viewsets.ViewSet):
    queryset = User.objects.filter(groups__name = 'Coach')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    @action(detail = False, methods = ['post'], url_path = 'create')
    def create_coach(self, request, *args, **kwargs):
        if not self.__validate_user_data(request.data):
            return Response(data = { 'msg': 'Invalid user data' }, status = HTTPStatus.BAD_REQUEST)
        try:
            user = User.objects.create_user(
                    first_name = request.data.get('first_name'),
                    last_name = request.data.get('last_name'),
                    username = request.data.get('username'),
                    email = request.data.get('email'),
                    password = request.data.get('password'),
                    phone = request.data.get('phone'),
                    title = request.data.get('title'),
                    description = request.data.get('description'),
                    )
            Group.objects.get(name = 'Coach').user_set.add(user)
        except Exception as e:
            return Response(data = { 'msg': 'User is already registered' }, status = HTTPStatus.BAD_REQUEST)
        return Response(status = HTTPStatus.CREATED)

    def __validate_user_data(self, user_data):
        cond = []
        cond.append(user_data.get('first_name') is not None)
        cond.append(user_data.get('last_name') is not None)
        cond.append(user_data.get('username') is not None)
        cond.append(user_data.get('email') is not None)
        cond.append(user_data.get('password') is not None)
        cond.append(user_data.get('phone') is not None)
        cond.append(user_data.get('title') is not None)
        return all(cond)

    @action(detail = False, methods = ['get'], url_path = '(?P<pk>[0-9]+)')
    def get_coach(self, request, pk):
        try:
            queryset = self.queryset.get(pk = pk)
            serializer = UserSerializer(queryset)
            return Response(data = serializer.data, status = HTTPStatus.OK)
        except User.DoesNotExist:
            return Response(status = HTTPStatus.NOT_FOUND)

    @action(detail = True, methods = ['get'], url_path = 'get-activity-schedule')
    def get_activity_schedule(self, request, pk):
        try:
            coach = self.queryset.get(pk = pk)
            activities_scheduled = ActivitySchedule.objects.filter(coach = coach)
            return Response(data = ActivityScheduleSerializer(activities_scheduled, many = True).data,
                            status = HTTPStatus.OK)
        except User.DoesNotExist:
            return Response(status = HTTPStatus.NOT_FOUND)

    @action(detail = True, methods = ['delete'], url_path = 'deactivate')
    def deactivate(self, request, pk):
        try:
            coach = self.queryset.get(pk = pk)
            coach.is_active = False
            coach.save()
            return Response(status = HTTPStatus.ACCEPTED)
        except User.DoesNotExist:
            return Response(status = HTTPStatus.NOT_FOUND)
