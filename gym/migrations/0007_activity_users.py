# Generated by Django 5.0.6 on 2024-07-17 21:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("gym", "0006_classmodality_classplan_classes_classschedule_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="activity",
            name="users",
            field=models.ManyToManyField(
                blank=True, related_name="activities", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]