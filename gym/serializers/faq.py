from rest_framework import serializers
from gym.models.faqs import Faqs


class FaqsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faqs
        fields = '__all__'

