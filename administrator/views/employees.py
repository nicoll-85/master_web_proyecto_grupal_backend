from rest_framework import viewsets
from administrator.models.Employees import Employees
from rest_framework.permissions import IsAuthenticated
from administrator.serializers.Employees import EmployeesSerializer


class EmployeesViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer
    permission_classes = [IsAuthenticated]

    def __str__(self):
        return self.name