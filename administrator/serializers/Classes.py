from rest_framework import serializers
from administrator.models.Classes import Classes


class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = '__all__'