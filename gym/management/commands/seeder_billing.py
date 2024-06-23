from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand

from authentication.models import User
from gym.models.activity_modality import ActivityModality
from gym.models.activity_plan import ActivityPlan
from gym.models.billing_period import BillingPeriod
from gym.models.billing_plan import BillingPlan


class Command(BaseCommand):
    help = "User seeder"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        print('Seeder billing - Started')
        self.__create_billing_plan()
        self.__create_billing_period()
        print('Seeder billing - Finished')

    def __create_billing_plan(self):
        print('Seeder billing - Creating billing plans')
        data_billing_plans = [
            {'name': 'Panteón', 'plan_id': 1, 'modality_id': 1, 'price': 40},
            {'name': 'Cumbre', 'plan_id': 2, 'modality_id': 1, 'price': 60},
            {'name': 'Olimpo', 'plan_id': 3, 'modality_id': 1, 'price': 90},
            {'name': 'Panteón', 'plan_id': 1, 'modality_id': 2, 'price': 30},
            {'name': 'Cumbre', 'plan_id': 2, 'modality_id': 2, 'price': 50},
            {'name': 'Olimpo', 'plan_id': 3, 'modality_id': 2, 'price': 80},
        ]
        for data in data_billing_plans:
            try:
                BillingPlan.objects.get(plan_id = data['plan_id'], modality_id = data['modality_id'])
                print(f'{data["name"]} already exists')
            except Exception as e:
                act_plan = ActivityPlan.objects.get(id=data['plan_id'])
                modality = ActivityModality.objects.get(id=data['modality_id'])
                BillingPlan.objects.create(
                    name=data['name'],
                    plan=act_plan,
                    modality=modality,
                    price=data['price']
                )

        users = User.objects.filter(groups__name='Client')
        billing_plan = BillingPlan.objects.get(plan_id=1, modality_id=1)
        for user in users:
            user.billing_plan = billing_plan
            user.save()

    def __create_billing_period(self):
        print('Seeder billing - Creating billing periods')
        data_billing_periods = [
            {'fee': 100, 'payment_date': '2021-01-01', 'user_id': 1},
            {'fee': 100, 'payment_date': '2021-02-01', 'user_id': 2},
            {'fee': 100, 'payment_date': '2021-03-01', 'user_id': 3},
        ]
        for data in data_billing_periods:
            try:
                BillingPeriod.objects.get(user_id=data['user_id'], payment_date=data['payment_date'])
                print(f'{data["user_id"]} - {data["payment_date"]} already exists')
            except Exception as e:
                BillingPeriod.objects.create(
                    fee=data['fee'],
                    payment_date=data['payment_date'],
                    client_id=data['user_id']
                )
