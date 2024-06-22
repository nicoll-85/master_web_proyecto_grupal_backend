from django.core.management import BaseCommand

from gym.management.commands.seeder_auth import Command as SeederAuthCommand
from gym.management.commands.seeder_activities import Command as SeederActivitiesCommand
from gym.management.commands.seeder_billing import Command as SeederBillingCommand


class Command(BaseCommand):
    help = "Seeder"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        print('Seeder - Started 🚀')
        SeederAuthCommand().handle()
        SeederActivitiesCommand().handle()
        SeederBillingCommand().handle()
        print('Seeder - Finished 🎉')