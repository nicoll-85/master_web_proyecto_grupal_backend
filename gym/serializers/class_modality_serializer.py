from rest_framework import serializers
from gym.models.class_modality import ClassModality

class ClassModalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassModality
        fields = '__all__'
