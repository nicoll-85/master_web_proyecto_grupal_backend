# Generated by Django 5.0.6 on 2024-07-12 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("administrator", "0005_alter_employee_identification"),
    ]

    operations = [
        migrations.CreateModel(
            name="Employees",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=100)),
                ("phone", models.CharField(max_length=15)),
                ("address", models.TextField()),
                ("date_of_birth", models.DateField()),
                ("date_of_joining", models.DateField()),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="employees/"),
                ),
            ],
            options={
                "verbose_name": "employee",
                "verbose_name_plural": "employees",
                "ordering": ["first_name"],
            },
        ),
        migrations.DeleteModel(
            name="Employee",
        ),
    ]
