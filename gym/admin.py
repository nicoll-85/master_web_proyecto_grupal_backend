from django.contrib import admin

from gym.models.activity import Activity
from gym.models.activity_modality import ActivityModality
from gym.models.activity_plan import ActivityPlan
from gym.models.activity_schedule import ActivitySchedule
from gym.models.billing_period import BillingPeriod
from gym.models.billing_plan import BillingPlan
from gym.models.faqs import Faqs
from gym.models.users_activities import UsersActivities
from gym.models.work_calendar import WorkCalendar


admin.register({Activity,
                ActivityModality,
                ActivityPlan,
                ActivitySchedule,
                BillingPeriod,
                BillingPlan,
                Faqs,
                UsersActivities,
                WorkCalendar})
