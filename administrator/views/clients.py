
from rest_framework import viewsets
from authentication.models import User
from authentication.serializers.user import UserSerializer


class ClientsViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().select_related('billing_plan')
    serializer_class = UserSerializer
    








