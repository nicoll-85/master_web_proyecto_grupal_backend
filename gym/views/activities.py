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

    @action(detail=False, methods=['post'], url_path='register_activities')
    def register_classes(self, request, pk=None):
        user = request.user
        activity_ids = request.data.get('activities', [])
        activities = self.queryset.filter(pk__in=activity_ids)
        for activity in activities:
            if not user.get_signed_activities().filter(activity=activity).exists():
                user.usersactivities_set.create(activity=activity)
        return Response(status=HTTPStatus.CREATED)

    def list(self, request):
        user = request.user
        modality = user.billing_plan.modality
        plan = user.billing_plan.plan
        queryset = self.queryset.filter(modality=modality, plan=plan)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)