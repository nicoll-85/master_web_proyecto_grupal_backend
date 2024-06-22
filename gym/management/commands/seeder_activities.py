from django.core.management.base import BaseCommand

from authentication.models import User
from gym.models.activity_modality import ActivityModality
from gym.models.activity_plan import ActivityPlan
from gym.models.activity_schedule import ActivitySchedule
from gym.models.activity import Activity
from gym.models.users_activities import UsersActivities


class Command(BaseCommand):
    help = "User seeder"

    DATA_CLASSES = [
        {'name': 'Class1', 'description': 'Description1', 'modality_id': 1, 'plan_id': 1},
        {'name': 'Class2', 'description': 'Description2', 'modality_id': 2, 'plan_id': 2},
        {'name': 'Class3', 'description': 'Description3', 'modality_id': 1, 'plan_id': 3},
    ]
    DATA_SCHEDULES = [
        {'class__name': 'Class1', 'user__coach': 'Coach1', 'day_week': 'Monday', 'start_time': '08:00', 'end_time': \
            '09:00'},
        {'class__name': 'Class2', 'user__coach': 'Coach2', 'day_week': 'Tuesday', 'start_time': '09:00',
         'end_time': '10:00'},
        {'class__name': 'Class3', 'user__coach': 'Coach3', 'day_week': 'Wednesday', 'start_time': '10:00',
         'end_time': '11:00'},
    ]
    DATA_USERS = [
        {'class': 'Class1', 'username': ['Client1', 'Client3']},
        {'class': 'Class2', 'username': ['Client2', 'Client3']},
        {'class': 'Class3', 'username': ['Client1', ]},
    ]

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        print('Seeder classes - Started')
        self.__create_related_info()
        self.__create_classes()
        print('Seeder classes - Finished')

    def __create_related_info(self):
        print('Seeder classes - Create related info')
        data_activity_plans = [
            {'name': 'Panteón', 'description': 'Plan básico'},
            {'name': 'Cumbre', 'description': 'Plan intermedio'},
            {'name': 'Olimpo', 'description': 'Plan avanzado'},
        ]
        data_activity_modalities = [
            {'name': 'Presencial'},
            {'name': 'Virtual'},
        ]
        for data in data_activity_plans:
            try:
                ActivityPlan.objects.create(
                    name=data['name'],
                    description=data['description']
                )
            except:
                print(f'{data["name"]} already exists')
        for data in data_activity_modalities:
            try:
                ActivityModality.objects.create(
                    name=data['name']
                )
            except:
                print(f'{data["name"]} already exists')


    def __create_classes(self):
        print('Seeder classes - Creating classes')
        for data in self.DATA_CLASSES:
            try:
                Activity.objects.get(name=data['name'])
                print(f'{data["name"]} already exists')
            except:
                Activity.objects.create(
                    name=data['name'],
                    description=data['description'],
                    modality_id=data['modality_id'],
                    plan_id=data['plan_id']
                )

        for data in self.DATA_SCHEDULES:
            user = User.objects.get(username=data['user__coach'])
            gclass = Activity.objects.get(name=data['class__name'])
            try:
                ActivitySchedule.objects.get(activity=gclass, day=data['day'])
                print(f'{gclass.name} - {data["day"]} already exists')
            except:
                ActivitySchedule.objects.create(
                    activity=gclass,
                    day_week=data['day_week'],
                    start_time=data['start_time'],
                    end_time=data['end_time'],
                    coach=user
                )

        for data in self.DATA_USERS:
            activity = Activity.objects.filter(name=data['class']).first()
            for username in data['username']:
                user = User.objects.get(username=username)
                UsersActivities.objects.create(
                    client=user,
                    activity=activity
                )
