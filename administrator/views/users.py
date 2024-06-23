from http import HTTPStatus

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response


class UsersViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated, IsAdminUser]

    #TODO: DEVOLVER LA DATA DE TODOS LOS USUARIOS DE UN ROL. api/admin/users/<role>
    @action(detail = False, methods = ['get'], url_path = '(?P<role>[Client|Coach]+)')
    def get_users(self, request, role):
        return Response(data = { 'msg': 'Not implemented yet "get_users"' }, status = HTTPStatus.NOT_IMPLEMENTED)

    # TODO: DEVOLVER LA DATA DE UN USUARIO. api/admin/users/<pk>
    @action(detail = False, methods = ['get'], url_path = '(?P<pk>[1-9]+)')
    def get_user(self, request, pk):
        return Response(data = { 'msg': 'Not implemented yet "get_user"' }, status = HTTPStatus.NOT_IMPLEMENTED)

