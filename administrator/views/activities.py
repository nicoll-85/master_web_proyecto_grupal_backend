from http import HTTPStatus
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from administrator.serializers.activity import ActivitySerializer
from authentication.models import User
from gym.models.activity import Activity

class ActivitiesAdminViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    """
    - Crear una actividad con nombre + entrenador + plan + modalidad + seleccionar día(s) + seleccionar hora
    - Asignar una actividad a un empleado 
    - Modificar una actividad + asignar a un empleado
    - Eliminar una actividad
    - Ver todas las clases - horario
    """
    def create(self, request, *args, **kwargs):
        try:
            coach = User.objects.get(groups__name = 'Coach', pk = request.data['coach'])
        except User.DoesNotExist:
            return Response(status = HTTPStatus.NOT_FOUND)
        schedules = request.data.pop('schedules')
        activity = Activity.objects.create(
            name = request.data['name'],
            plan_id = request.data['plan'],
            modality_id = request.data['modality']
        )
        self.__process_schedules(activity, schedules, coach)
        return Response(data = ActivitySerializer(activity).data, status = HTTPStatus.CREATED)

    def update(self, request, *args, **kwargs):
        try:
            try:
                activity = self.queryset.get(pk = kwargs['pk'])
                coach = User.objects.get(groups__name = 'Coach', pk = request.data['coach'])
            except User.DoesNotExist or Activity.DoesNotExist:
                return Response(status = HTTPStatus.NOT_FOUND)
            schedules = request.data.pop('schedules')
            activity.name = request.data['name']
            activity.description = request.data['description']
            activity.plan_id = request.data['plan']
            activity.modality_id = request.data['modality']
            activity.save()
            self.__process_schedules(activity, schedules, coach)
            return Response(data = ActivitySerializer(activity).data, status = HTTPStatus.ACCEPTED)
        except Activity.DoesNotExist:
            return Response(status = HTTPStatus.NOT_FOUND)

    def __process_schedules(self, activity, schedules_data, coach):
        schedules_id = list(activity.schedules.values_list('id', flat = True))
        for schedule in schedules_data:
            if schedule.get('id'):
                sched = activity.schedules.get(pk = schedule['id'])
                sched.start_time = schedule['start_time']
                sched.end_time = schedule['end_time']
                sched.coach = coach
                sched.save()
                schedules_id.remove(schedule['id'])
            else:
                activity.schedules.create(
                    start_time = schedule['start_time'],
                    end_time = schedule['end_time'],
                    day_week = schedule['day_week'],
                    coach = coach,
                    activity = activity
                )
        for schedule in activity.schedules.filter(id__in = schedules_id):
            schedule.delete()

    @action(detail = True, methods = ['post'], url_path = 'assign-coach')
    def assign_coach(self, request, pk):
        try:
            activity = self.queryset.get(pk = pk)
            coach = User.objects.get(groups__name = 'Coach', pk = request.data['coach'])
            for activity_schedule in activity.schedules:
                activity_schedule.coach = coach
                activity_schedule.save()
            return Response(data = ActivitySerializer(activity).data, status = HTTPStatus.ACCEPTED)
        except Activity.DoesNotExist:
            return Response(status = HTTPStatus.NOT_FOUND)
