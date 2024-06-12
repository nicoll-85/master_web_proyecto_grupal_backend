from rest_framework import routers

from authentication.views.auth import AuthViewset

router = routers.DefaultRouter()
router.register('', AuthViewset, basename = 'user')
router.urlpatterns = router.urls
