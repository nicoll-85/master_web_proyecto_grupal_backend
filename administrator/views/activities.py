from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from gym.models.activity import Activity
from gym.serializers.activity import ActivitySerializer


class ActivitiesViewSet(viewsets.ViewSet):
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