from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand

from authentication.models import User


class Command(BaseCommand):
    help = "User seeder"

    CLIENT_DATA = [
        { 'username': 'Antonio', "first_name": 'Antonio', "last_name": 'Fernandez', 'phone': '678451534',
          'email': 'antonio@client.com', 'password': 'qwerty' },
        { 'username': 'Maria', "first_name": 'Maria', "last_name": 'Gonzalez', 'phone': '674839201',
          'email': 'maria@client.com', 'password': 'asdfgh' },
        { 'username': 'Juan', "first_name": 'Juan', "last_name": 'Martinez', 'phone': '689204173',
          'email': 'juan@client.com', 'password': 'zxcvbn' },
        { 'username': 'Laura', "first_name": 'Laura', "last_name": 'Garcia', 'phone': '662738490',
          'email': 'laura@client.com', 'password': 'ytrewq' },
        ]

    COACH_DATA = [
        { 'username': 'JavierC', "first_name": 'Javier', "last_name": 'Mendoza', 'phone': '678451534',
          'email': 'javier.coach@coach.com', 'password': 'coach123' },
        { 'username': 'IsabelC', "first_name": 'Isabel', "last_name": 'Ortiz', 'phone': '674839201',
          'email': 'isabel.coach@coach.com', 'password': 'coach456' },
        { 'username': 'LuisC', "first_name": 'Luis', "last_name": 'Morales', 'phone': '689204173',
          'email': 'luis.coach@coach.com', 'password': 'coach789' },
        ]

    ADMIN_DATA = [
        {'username': 'Admin', 'first_name': 'Herafit', "last_name":'Center', 'phone': '672948302', 'email': 'admin@admin.com', 'password': 'qwerty'},
    ]

    def add_arguments(self, parser):
        pass


    def handle(self, *args, **options):
        print('Seeder auth - Started')
        self.__create_roles()
        self.__define_permissions()
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

    def __define_permissions(self):
        print('Seeder auth - Defining permissions')
        pass


    def __create_users(self):
        print('Seeder auth - Creating users')
        client_role = Group.objects.get(name = 'Client')
        coach_role = Group.objects.get(name = 'Coach')
        admin_role = Group.objects.get(name = 'Admin')

        list_users = []
        for user_data in self.CLIENT_DATA:
            try:
                list_users.append(User.objects.create_user(
                        username = user_data['username'],
                        email = user_data['email'],
                        first_name= user_data['first_name'],
                        last_name = user_data['last_name'],
                        phone = user_data['phone'],
                        password = user_data['password']
                        ))
                list_users[-1].groups.add(client_role)
            except Exception as e:
                print(f'{user_data["username"]} already exists')

        for user_data in self.COACH_DATA:
            try:
                list_users.append(User.objects.create_user(
                        username = user_data['username'],
                        email = user_data['email'],
                        first_name= user_data['first_name'],
                        last_name = user_data['last_name'],
                        phone = user_data['phone'],
                        password = user_data['password'],
                        is_staff = True
                        ))
                list_users[-1].groups.add(coach_role)
            except Exception as e:
                print(f'{user_data["username"]} already exists')

        for user_data in self.ADMIN_DATA:
            try:
                list_users.append(User.objects.create_user(
                        username = user_data['username'],
                        email = user_data['email'],
                        password = user_data['password'],
                        first_name= user_data['first_name'],
                        last_name = user_data['last_name'],
                        phone = user_data['phone'],
                        is_superuser = True
                        ))
                list_users[-1].groups.add(admin_role)
            except Exception as e:
                print(f'{user_data["username"]} already exists')
        print('\nList of users created:')
        for user in list_users:
            print(f'User {user.username} created')
        print('\n')
