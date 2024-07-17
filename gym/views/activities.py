from http import HTTPStatus
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from gym.models.activity import Activity
from administrator.serializers.activity import ActivitySerializer

class ActivitiesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'], url_path='register_classes')
    def register_classes(self, request, pk=None):
        try:
            activity = self.queryset.get(pk=pk)
            user = request.user

            if activity.users.filter(pk=user.pk).exists():
                return Response({'message': 'Te has registrado en la clase'}, status=HTTPStatus.BAD_REQUEST)

            activity.users.add(user)
            return Response({'message': 'Registro realizado correctamente'}, status=HTTPStatus.OK)

        except Activity.DoesNotExist:
            return Response(status=HTTPStatus.NOT_FOUND)

    def list(self, request):
        user = request.user
        modality = user.billing_plan.modality
        plan = user.billing_plan.plan
        queryset = self.queryset.filter(modality=modality, plan=plan)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
