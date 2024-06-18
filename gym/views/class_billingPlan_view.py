
from rest_framework import viewsets
from gym.models.class_billingPlan import BillingPlan
from gym.serializers.class_billinPlan_serializer import BillingPlanSerializer

class ClassBillingPlanViewSet(viewsets.ModelViewSet):
    queryset = BillingPlan.objects.all()
    serializer_class = BillingPlanSerializer

