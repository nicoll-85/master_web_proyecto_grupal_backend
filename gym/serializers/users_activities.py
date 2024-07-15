from rest_framework import serializers
from gym.models.users_activities import UsersActivities


class UsersActivitiesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = UsersActivities
        fields = '__all__'


class UsersActivitiesClientSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(source='client.first_name', read_only=True)

    class Meta:
        model = UsersActivities
        fields = ['client_name']

