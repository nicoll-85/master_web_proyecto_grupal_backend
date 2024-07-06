from http import HTTPStatus

from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from administrator.serializers.activity import ActivitySerializer
from gym.models.activity import Activity
from gym.models.activity_schedule import ActivitySchedule


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def create(self, request):
        name = request.data['name']
        description = request.data['description']
        plan = request.data['plan']
        modality = request.data['modality']
        day_week = request.data['day_week']
        start_time = request.data['start_time']
        end_time = request.data['end_time']
        try:
            activity = Activity.objects.create(
                name=name,
                description=description,
                plan=plan,
                modality=modality,
            )
            ActivitySchedule.objects.create(
                start_time=start_time,
                end_time=end_time,
                day_week=day_week,
                activity=activity,
            )            
        except Exception as e:
            return Response(status=HTTPStatus.BAD_REQUEST)
        return Response(status=HTTPStatus.OK)



    ''' 
        - Añadir una clase nueva que se conecta con activity schedule
        - Quitar un clase x defecto que se conecta con activity schedule
        - Asignar a un usuario a una clase --> do it        
    '''