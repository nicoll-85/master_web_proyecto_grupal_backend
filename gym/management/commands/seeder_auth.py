from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand

from authentication.models import User


class Command(BaseCommand):
    help = "User seeder"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        print('Seeder auth - Started')
        self.__create_roles()
        self.__create_users()
        print('Seeder auth - Finished')

    def __create_roles(self):
        print('Seeder auth - Creating roles')
        roles_data = [
            { 'name': 'Client' },
            { 'name': 'Coach' },
            { 'name': 'Admin' },
            ]

        list_roles = []
        for role_data in roles_data:
            try:
                list_roles.append(Group.objects.create(
                        name = role_data['name']
                        ))
            except Exception as e:
                print(f'{role_data["name"]} already exists')
        print('\nList of roles created:')
        for role in list_roles:
            print(f'Role {role.name} created')
        print('\n')

    def __create_users(self):
        print('Seeder auth - Creating users')
        client_data = [
            { 'username': 'Client1', 'email': 'client1@gmail.com', 'password': 'qwerty' },
            { 'username': 'Client2', 'email': 'client2@gmail.com', 'password': 'qwerty' },
            { 'username': 'Client3', 'email': 'client3@gmail.com', 'password': 'qwerty' },
            ]
        client_role = Group.objects.get(name = 'Client')
        coach_data = [
            { 'username': 'Coach1', 'email': 'Coach1@gmail.com', 'password': 'qwerty' },
            { 'username': 'Coach2', 'email': 'Coach2@gmail.com', 'password': 'qwerty' },
            { 'username': 'Coach3', 'email': 'Coach3@gmail.com', 'password': 'qwerty' },
            ]
        coach_role = Group.objects.get(name = 'Coach')
        admin_data = [
            { 'username': 'Admin1', 'email': 'admin1@gmail.com', 'password': 'qwerty' },
            ]
        admin_role = Group.objects.get(name = 'Admin')

        list_users = []
        for user_data in client_data:
            try:
                list_users.append(User.objects.create_user(
                        username = user_data['username'],
                        email = user_data['email'],
                        password = user_data['password']
                        ))
                list_users[-1].groups.add(client_role)
            except Exception as e:
                print(f'{user_data["username"]} already exists')

        for user_data in coach_data:
            try:
                list_users.append(User.objects.create_user(
                        username = user_data['username'],
                        email = user_data['email'],
                        password = user_data['password'],
                        is_staff = True
                        ))
                list_users[-1].groups.add(coach_role)
            except Exception as e:
                print(f'{user_data["username"]} already exists')

        for user_data in admin_data:
            try:
                list_users.append(User.objects.create_user(
                        username = user_data['username'],
                        email = user_data['email'],
                        password = user_data['password'],
                        is_staff = True
                        ))
                list_users[-1].groups.add(admin_role)
            except Exception as e:
                print(f'{user_data["username"]} already exists')
        print('\nList of users created:')
        for user in list_users:
            print(f'User {user.username} created')
        print('\n')
