from rest_framework import serializers
from administrator.models.Employees import Employees


class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'

