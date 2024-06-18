from rest_framework import routers
from gym.views.class_modality_view import ClassModalityViewSet
from gym.views.class_plan_view import ClassPlanViewSet
from gym.views.classes_view import ClassesViewSet
from gym.views.class_schedule_view import ClassScheduleViewSet
from gym.views.users_classes_view import UsersClassesViewSet


router = routers.DefaultRouter()
router.register(r'class_plan', ClassPlanViewSet)
router.register(r'class_modality', ClassModalityViewSet)
router.register(r'classes', ClassesViewSet)
router.register(r'class_schedule', ClassScheduleViewSet)
router.register(r'users_classes', UsersClassesViewSet)

urlpatterns = router.urls
