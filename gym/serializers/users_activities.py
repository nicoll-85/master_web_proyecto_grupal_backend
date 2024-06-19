from rest_framework import serializers
from gym.models.users_activities import UsersActivities


class UsersActivitiesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = UsersActivities
        fields = '__all__'
