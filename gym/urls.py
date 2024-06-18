from rest_framework import routers
from gym.views.class_modality_view import ClassModalityViewSet
from gym.views.class_plan_view import ClassPlanViewSet
from gym.views.classes_view import ClassesViewSet
from gym.views.class_schedule_view import ClassScheduleViewSet
from gym.views.users_classes_view import UsersClassesViewSet
from gym.views.class_faqs_view import FaqsViewSet
from gym.views.class_work_calendar_view import WorkCalendarViewSet
from gym.views.class_billingPeriod_view import ClassbillingPeriodViewSet
from gym.views.class_billingPlan_view import ClassbillingPlanViewSet


router = routers.DefaultRouter()
router.register(r'class_plan', ClassPlanViewSet)
router.register(r'class_modality', ClassModalityViewSet)
router.register(r'classes', ClassesViewSet)
router.register(r'class_schedule', ClassScheduleViewSet)
router.register(r'users_classes', UsersClassesViewSet)
router.register(r'class_billingPeriod', ClassbillingPeriodViewSet)
router.register(r'class_billingPlan', ClassbillingPlanViewSet)
router.register(r'faqs', FaqsViewSet)
router.register(r'work_calendar', WorkCalendarViewSet)

urlpatterns = router.urls
