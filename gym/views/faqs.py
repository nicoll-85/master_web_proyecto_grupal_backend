from rest_framework import viewsets
from gym.models.faqs import Faqs
from gym.serializers.faq import FaqsSerializer


class FaqsViewSet(viewsets.ModelViewSet):
    queryset = Faqs.objects.all()
    serializer_class = FaqsSerializer
