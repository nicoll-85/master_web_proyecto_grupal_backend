from rest_framework import viewsets
from gym.models.billing_plan import BillingPlan
from gym.serializers.billing_plan import BillingPlanSerializer


class BillingPlanViewSet(viewsets.ModelViewSet):
    queryset = BillingPlan.objects.all()
    serializer_class = BillingPlanSerializer
