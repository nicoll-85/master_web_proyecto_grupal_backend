from rest_framework import routers
from administrator.views.clients import ClientsViewSet
from administrator.views.users import UsersViewSet
from administrator.views.classes import ClassesViewSet
from administrator.views.employees import EmployeesViewSet
from administrator.views.classesSchedule import ClassScheduleViewSet

router = routers.DefaultRouter()
router.register(r'clients', ClientsViewSet),
router.register(r'users', UsersViewSet, basename = 'users'),
router.register(r'classes', ClassScheduleViewSet, basename = 'classes')
router.register(r'employees', EmployeesViewSet, basename = 'employees')
urlpatterns = router.urls


