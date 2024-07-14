from rest_framework import routers

from administrator.views.activities import ActivitiesViewSet
from administrator.views.clients import ClientsViewSet
from administrator.views.coachs import CoachViewSet
from administrator.views.users import UsersViewSet

router = routers.DefaultRouter()

router.register(r'clients', ClientsViewSet, basename = 'clients'),
router.register(r'users', UsersViewSet, basename = 'users'),
router.register(r'coaches', CoachViewSet, basename = 'coaches')
router.register(r'activities', ActivitiesViewSet, basename = 'activities')


urlpatterns = router.urls


