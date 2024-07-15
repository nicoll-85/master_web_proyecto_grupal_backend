# gym/urls.py
from rest_framework.routers import DefaultRouter
from gym.views.class_plan_view import ClassPlanViewSet
from gym.views.class_modality_view import ClassModalityViewSet
from gym.views.classes_view import ClassesViewSet
from gym.views.class_schedule_view import ClassScheduleViewSet
from gym.views.users_classes_view import UsersClassesViewSet

router = DefaultRouter()
router.register(r'class_plans', ClassPlanViewSet)
router.register(r'class_modalities', ClassModalityViewSet)
router.register(r'classes', ClassesViewSet)
router.register(r'class_schedules', ClassScheduleViewSet)
router.register(r'users_classes', UsersClassesViewSet)

urlpatterns = router.urls
