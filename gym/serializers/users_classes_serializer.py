from rest_framework import serializers
from gym.models.users_classes import UsersClasses

class UsersClassesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = UsersClasses
        fields = '__all__'