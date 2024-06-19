from rest_framework import viewsets
from gym.models.billing_period import BillingPeriod
from gym.serializers.billing_period import BillingPeriodSerializer


class BillingPeriodViewSet(viewsets.ModelViewSet):
    queryset = BillingPeriod.objects.all()
    serializer_class = BillingPeriodSerializer
