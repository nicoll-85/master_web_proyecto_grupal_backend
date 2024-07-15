from rest_framework import serializers
from gym.models.activity_modality import ActivityModality


class ActivityModalitySerializer(serializers.ModelSerializer):
    class Meta: 
        model = ActivityModality
        fields = '__all__'
