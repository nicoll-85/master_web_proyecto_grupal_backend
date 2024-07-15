from rest_framework import serializers
from gym.models.activity import Activity
from gym.serializers.activity_modality import ActivityModalitySerializer
from gym.serializers.activity_plan import ActivityPlanSerializer
from gym.serializers.users_activities import UsersActivitiesClientSerializer


class ActivitySerializer(serializers.ModelSerializer):
    modality = ActivityModalitySerializer(read_only = True)
    plan = ActivityPlanSerializer(read_only = True)
    class Meta: 
        model = Activity
        fields = '__all__'


class ActivityWithClientsSerializer(serializers.ModelSerializer):
    my_clients = UsersActivitiesClientSerializer(many=True, read_only=True)

    class Meta:
        model = Activity
        fields = ['id', 'name', 'my_clients']
