from rest_framework import serializers
from gym.models.class_plan import ClassPlan

class ClassPlanSerializer(serializers.ModelSerializer):
    class Meta: 
        model = ClassPlan
        fields = '__all__'