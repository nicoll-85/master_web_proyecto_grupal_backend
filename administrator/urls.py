from rest_framework import routers
from administrator.views.clients import ClientsViewSet


router = routers.DefaultRouter()
router.register(r'clients', ClientsViewSet)
urlpatterns = router.urls


