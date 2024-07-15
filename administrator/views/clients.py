from http import HTTPStatus

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from administrator.serializers.activity import ActivitySerializer
from authentication.models import User
from authentication.serializers.user import UserSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from gym.models.activity import Activity
from gym.models.activity_schedule import ActivitySchedule
from gym.models.billing_plan import BillingPlan
from gym.serializers.billing_period import BillingPeriodSerializer
from gym.serializers.billing_plan import BillingPlanSerializer


class ClientsAdminViewSet(viewsets.ViewSet):
    queryset = User.objects.filter(groups__name = 'Client').select_related('billing_plan')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    # TODO: Devolver data de un usuario. api/admin/clients/<pk> GET
    # TODO: Devolver clases de un usuario api/admin/clients/<pk>/activity-schedule GET
    # TODO: Update a un usuario. api/admin/clients/<pk>/update-billing-plan PUT
    # TODO: Add activity a un usuario api/admin/clients/<pk>/add-activity POST
    # TODO: Delete activity a un usuario api/admin/clients/<pk>/delete-activity PUT
    # TODO: Los pagos de un usuario. api/admin/clients/<pk>/payments GET
    # TODO: Dar de baja a un usuario. api/admin/clients/<pk>/deactivate DELETE

    @action(detail = False, methods = ['get'], url_path = '(?P<pk>[0-9]+)')
    def get_user(self, request, pk):
        try:
            queryset = self.queryset.get(pk = pk)
            serializer = UserSerializer(queryset)
            return Response(data = serializer.data, status = HTTPStatus.OK)
        except User.DoesNotExist:
            return Response(status = HTTPStatus.NOT_FOUND)

    @action(detail = True, methods = ['get'], url_path = 'activity-schedule')
    def get_user_activity_schedule(self, request, pk):
        try:
            user = self.queryset.get(pk = pk)
            activities = [user_activity.activity for user_activity in user.usersactivities_set.select_related('activity').all()]
            return Response(data = ActivitySerializer(activities, many = True).data, status = HTTPStatus.OK)
        except User.DoesNotExist:
            return Response(status = HTTPStatus.NOT_FOUND)

    @action(detail = True, methods = ['put'], url_path = 'update-billing-plan')
    def update_billing_plan(self, request, pk):
        try:
            modality = request.data['modality']
            plan = request.data['plan']
            user = self.queryset.get(pk = pk)
            billing_plan = BillingPlan.objects.get(plan_id = plan, modality_id = modality)
            user.billing_plan = billing_plan
            user.save()
            return Response(data = UserSerializer(user).data, status = HTTPStatus.ACCEPTED)
        except User.DoesNotExist:
            return Response(status = HTTPStatus.NOT_FOUND)

    @action(detail = True, methods = ['post'], url_path = 'add-activity')
    def add_activity(self, request, pk):
        try:
            user = self.queryset.get(pk = pk)
            activities = Activity.objects.filter(id__in = request.data['activities'])
            for activity in activities:
                user.usersactivities_set.create(activity = activity)
            return Response(status = HTTPStatus.CREATED)
        except User.DoesNotExist:
            return Response(status = HTTPStatus.NOT_FOUND)

    @action(detail = True, methods = ['put'], url_path = 'delete-activity')
    def delete_activity(self, request, pk):
        try:
            user = self.queryset.get(pk = pk)
            activities = Activity.objects.filter(id__in = request.data['activities'])
            for activity in activities:
                user.usersactivities_set.delete(activity = activity)
            return Response(status = HTTPStatus.CREATED)
        except User.DoesNotExist:
            return Response(status = HTTPStatus.NOT_FOUND)

    @action(detail = True, methods = ['get'], url_path = 'billing-periods')
    def get_payments(self, request, pk):
        try:
            user = self.queryset.get(pk = pk)
            billing_periods = user.get_billing_periods()
            return Response(data = BillingPeriodSerializer(billing_periods, many = True).data, status = HTTPStatus.OK)
        except User.DoesNotExist:
            return Response(status = HTTPStatus.NOT_FOUND)

    @action(detail = False, methods = ['get'], url_path = 'filter')
    def filter_modality(self, request):
        try:
            users = self.queryset.filter(billing_plan__modality__name = request.data['modality'])
            return Response(data = UserSerializer(users, many = True).data, status = HTTPStatus.OK)
        except User.DoesNotExist:
            return Response(status = HTTPStatus.NOT_FOUND)

    @action(detail = True, methods = ['delete'], url_path = 'deactivate')
    def deactivate(self, request, pk):
        try:
            user = self.queryset.get(pk = pk)
            user.is_active = False
            user.save()
            return Response(status = HTTPStatus.ACCEPTED)
        except User.DoesNotExist:
            return Response(status = HTTPStatus.NOT_FOUND)

