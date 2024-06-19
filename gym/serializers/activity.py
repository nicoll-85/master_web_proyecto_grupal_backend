from rest_framework import serializers
from gym.models.activity import Activity


class ActivitySerializer(serializers.ModelSerializer):
    class Meta: 
        model = Activity
        fields = '__all__'
