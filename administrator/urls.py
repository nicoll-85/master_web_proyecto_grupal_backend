from rest_framework import routers

from administrator.views.activities import ActivitiesAdminViewSet
from administrator.views.clients import ClientsAdminViewSet
from administrator.views.coachs import CoachAdminViewSet
from administrator.views.users import UsersAdminViewSet

router = routers.DefaultRouter()

router.register(r'clients', ClientsAdminViewSet, basename = 'clients'),
router.register(r'users', UsersAdminViewSet, basename = 'users'),
router.register(r'coaches', CoachAdminViewSet, basename = 'coaches')
router.register(r'activities', ActivitiesAdminViewSet, basename = 'activities')


urlpatterns = router.urls


