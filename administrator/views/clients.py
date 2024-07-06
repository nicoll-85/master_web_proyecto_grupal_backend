from http import HTTPStatus

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from authentication.models import User
from authentication.serializers.user import UserSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class ClientsViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().select_related('billing_plan')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    # TODO: Devolver data de un usuario. api/admin/clients/<pk> GET
    # TODO: Devolver clases de un usuario api/admin/clients/<pk>/activity-schedule GET
    # TODO: Update a un usuario. api/admin/clients/<pk>/update-billing-plan PUT
    # TODO: Add activity a un usuario api/admin/clients/<pk>/add-activity POST
    # TODO: Delete activity a un usuario api/admin/clients/<pk>/delete-activity PUT
    # TODO: Los pagos de un usuario. api/admin/clients/<pk>/payments GET
    # TODO: Dar de baja a un usuario. api/admin/clients/<pk>/deactivate DELETE

    @action(detail = True, methods = ['get'], url_path = '(?P<pk>[1-9]+)')
    def get_user(self, request, pk):
        try:
            queryset = User.objects.get(pk = pk)
            serializer = UserSerializer(queryset)
            return Response(data = serializer.data, status = HTTPStatus.OK)
        except User.DoesNotExist:
            return Response(status = HTTPStatus.NOT_FOUND)

    @action(detail = True, methods = ['get'], url_path = '(?P<pk>[1-9]+)/activity-schedule')
    def get_user_activity_schedule(self, request, pk):
        pass

    @action(detail = True, methods = ['put'], url_path = '(?P<pk>[1-9]+)/update-billing-plan')
    def update_billing_plan(self, request, pk):
        pass

    @action(detail = True, methods = ['post'], url_path = '(?P<pk>[1-9]+)/add-activity')
    def add_activity(self, request, pk):
        pass

    @action(detail = True, methods = ['put'], url_path = '(?P<pk>[1-9]+)/delete-activity')
    def delete_activity(self, request, pk):
        pass

    @action(detail = True, methods = ['get'], url_path = '(?P<pk>[1-9]+)/payments')
    def get_payments(self, request, pk):
        pass

    @action(detail = True, methods = ['delete'], url_path = '(?P<pk>[1-9]+)/deactivate')
    def deactivate(self, request, pk):
        pass

