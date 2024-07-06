from rest_framework import routers
from administrator.views.clients import ClientsViewSet
from administrator.views.users import UsersViewSet

router = routers.DefaultRouter()
router.register(r'clients', ClientsViewSet, basename = 'clients')
router.register(r'users', UsersViewSet, basename = 'users')
urlpatterns = router.urls


