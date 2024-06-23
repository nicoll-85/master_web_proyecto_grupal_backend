from rest_framework import routers

from administrator.views.users import UsersViewSet

router = routers.DefaultRouter()
router.register(r'users', UsersViewSet, basename = 'users')
router.urlpatterns = router.urls
