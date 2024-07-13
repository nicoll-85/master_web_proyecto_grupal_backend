
from rest_framework import viewsets
from authentication.models import User
from authentication.serializers.user import UserSerializer
from rest_framework.permissions import IsAuthenticated



class ClientsViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().select_related('billing_plan')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]








