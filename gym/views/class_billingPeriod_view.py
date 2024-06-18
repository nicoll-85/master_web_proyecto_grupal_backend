from django.shortcuts import render

from rest_framework import viewsets
from gym.models.class_billingPeriod import  BillingPeriod
from gym.serializers.class_billingPeriod_serializer import BillingPeriodSerializer


class ClassBillingPeriodViewSet(viewsets.ModelViewSet):
    queryset = BillingPeriod.objects.all()
    serializer_class = BillingPeriodSerializer