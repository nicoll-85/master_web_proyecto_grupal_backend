from rest_framework import viewsets
from gym.models.class_plan import ClassPlan
from gym.serializers.class_plan_serializer import ClassPlanSerializer

class ClassPlanViewSet(viewsets.ModelViewSet):
    queryset = ClassPlan.objects.all()
    serializer_class = ClassPlanSerializer