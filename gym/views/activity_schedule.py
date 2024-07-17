from http import HTTPStatus

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from authentication.models import User
from gym.models.activity import Activity
from gym.models.activity_schedule import ActivitySchedule
from gym.models.users_activities import UsersActivities
from gym.serializers.activity import ActivitySerializer, ActivityWithClientsSerializer
from gym.serializers.activity_schedule import ActivityScheduleSerializer
from gym.serializers.activity_schedule_coach import ActivityScheduleCoachSerializer


class ActivityScheduleViewSet(viewsets.ModelViewSet):
    queryset = ActivitySchedule.objects.all()
    serializer_class = ActivityScheduleSerializer
    permission_classes = [IsAuthenticated]


    """
     Mis alumnos x clase ->
        Nombre de la clase + Horario 
            - Nombre de los alumnos
        Clase Azúcar 12:00 - 13:00
            
    """
    @action(detail = False, methods = ['get'], url_path = 'me')
    def get_my_schedules(self, request):
        schedules = ActivitySchedule.objects.filter(coach = request.user)
        return Response(data = ActivityScheduleCoachSerializer(schedules, many = True).data, status = HTTPStatus.OK)

    @action(detail = False, methods = ['get'], url_path = 'my-clients')
    def get_my_clients(self, request):
        activities = Activity.objects.filter(activityschedule__coach = request.user).distinct()
        return Response(data = ActivityWithClientsSerializer(activities, many = True).data, status = HTTPStatus.OK)

