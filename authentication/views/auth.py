from http import HTTPStatus

from django.contrib.auth import authenticate, login, logout
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from authentication.models import User
from authentication.serializers.user import UserSerializer


class AuthViewset(viewsets.ViewSet):

    @action(detail=False, methods=['get'], url_path = 'me', permission_classes=[IsAuthenticated])
    def me(self, request):
        return Response(UserSerializer(request.user).data)

    @action(detail=False, methods=['post'], url_path = 'login', permission_classes=[])
    def login(self, request):
        user = request.user
        if user and user.is_authenticated:
            return Response(status = HTTPStatus.ACCEPTED)
        else:
            user = authenticate(
                username=request.data.get('username'),
                password=request.data.get('password'),
            )
            if user is None:
                return Response(data = {'msg': 'Invalid credentials'}, status = HTTPStatus.UNAUTHORIZED)
            login(request, user)
        return Response(status = HTTPStatus.ACCEPTED)

    @action (detail = False , methods = [ 'post' ] , url_path = 'logout' , permission_classes=[IsAuthenticated])
    def logout ( self , request ) :
        logout(request)
        return Response(status = HTTPStatus.ACCEPTED)

    @action (detail = False, methods =['post'], url_path = 'register', permission_classes=[])
    def register(self, request):
        try:
            User.objects.create_user(
                username = request.data.get('username'),
                email = request.data.get('email'),
                password = request.data.get('password'),
            )
        except Exception as e:
            return Response(data = {'msg': 'User is already registered'}, status = HTTPStatus.BAD_REQUEST)
        return Response(status = HTTPStatus.CREATED)