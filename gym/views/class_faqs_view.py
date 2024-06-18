from rest_framework import viewsets
from gym.models.class_faqs import Faqs
from gym.serializers.class_faq_serializers import FaqsSerializer


class FaqsViewSet(viewsets.ModelViewSet):
    queryset = Faqs.objects.all()
    serializer_class = FaqsSerializer
