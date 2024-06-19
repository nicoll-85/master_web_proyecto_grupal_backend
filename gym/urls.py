from rest_framework import routers

from gym.views.activity import ActivityViewSet
from gym.views.activity_modality import ActivityModalityViewSet
from gym.views.activity_plan import ActivityPlanViewSet
from gym.views.activity_schedule import ActivityScheduleViewSet
from gym.views.billing_period import BillingPeriodViewSet
from gym.views.billing_plan import BillingPlanViewSet
from gym.views.faqs import FaqsViewSet
from gym.views.work_calendar import WorkCalendarViewSet

router = routers.DefaultRouter()
router.register(r'activity', ActivityViewSet)
router.register(r'activity_plan', ActivityPlanViewSet)
router.register(r'activity_schedule', ActivityScheduleViewSet)
router.register(r'activity_modality', ActivityModalityViewSet)
router.register(r'billing_period', BillingPeriodViewSet)
router.register(r'billing_plan', BillingPlanViewSet)
router.register(r'faqs', FaqsViewSet)
router.register(r'work_calendar', WorkCalendarViewSet)




urlpatterns = router.urls
