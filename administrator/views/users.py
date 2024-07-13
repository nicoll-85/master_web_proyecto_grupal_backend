from http import HTTPStatus

from django.contrib.auth.models import Group
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from authentication.models import User
from authentication.serializers.user import UserSerializer


class UsersViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated, IsAdminUser]

    @action(detail = False, methods = ['get'], url_path = '(?P<role>[Client|Coach]+)')
    def get_users(self, request, role):
        groups = Group.objects.get(name=role)
        users = User.objects.filter(groups=groups)
        serializer = UserSerializer(users, many=True)
        return Response(data = serializer.data, status = HTTPStatus.OK)

    # TODO: DEVOLVER LA DATA DE UN USUARIO. api/admin/users/<pk>
    @action(detail = False, methods = ['get'], url_path = '(?P<pk>[1-9]+)')
    def get_user(self, request, pk):
        return Response(data = { 'msg': 'Not implemented yet "get_user"' }, status = HTTPStatus.NOT_IMPLEMENTED)

