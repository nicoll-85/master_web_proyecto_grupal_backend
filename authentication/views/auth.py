from http import HTTPStatus

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from authentication.models import User
from authentication.serializers.user import UserSerializer
from gym.models.billing_plan import BillingPlan


class AuthViewset(viewsets.ViewSet):

    @action(detail = False, methods = ['get'], url_path = 'me', permission_classes = [IsAuthenticated])
    def me(self, request):
        return Response(UserSerializer(request.user).data)

    @action(detail = False, methods = ['post'], url_path = 'login', permission_classes = [])
    def login(self, request):
        user = authenticate(
            username = request.data.get('username'),
            password = request.data.get('password'),
            )
        if user is None:
            return Response(data = { 'msg': 'Invalid credentials' }, status = HTTPStatus.UNAUTHORIZED)
        login(request, user)
        if user and user.is_authenticated:
            token, _ = Token.objects.get_or_create(user = user)
            return Response(data = { 'token': token.key }, status = HTTPStatus.OK)
        return Response(status = HTTPStatus.UNAUTHORIZED)

    @action(detail = False, methods = ['post'], url_path = 'logout', permission_classes = [IsAuthenticated])
    def logout(self, request):
        user = request.user
        if user and user.is_authenticated:
            Token.objects.filter(user = user).delete()
        logout(request)
        return Response(status = HTTPStatus.ACCEPTED)

    @action(detail = False, methods = ['post'], url_path = 'register', permission_classes = [])
    def register(self, request):
        if not self.__validate_user_data(request.data):
            return Response(data = { 'msg': 'Invalid user data' }, status = HTTPStatus.BAD_REQUEST)
        try:
            modality = request.data['modality']
            plan = request.data['plan']
            user = User.objects.create_user(
                    first_name= request.data.get('first_name'),
                    last_name = request.data.get('last_name'),
                    username = request.data.get('username'),
                    email = request.data.get('email'),
                    password = request.data.get('password'),
                    phone = request.data.get('phone'),
                    )
            Group.objects.get(name = 'Client').user_set.add(user)
            billing_plan = BillingPlan.objects.get(plan_id = plan, modality_id = modality)
            user.billing_plan = billing_plan
            user.save()
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
        return all(cond)
