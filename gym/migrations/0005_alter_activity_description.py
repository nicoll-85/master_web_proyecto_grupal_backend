# Generated by Django 5.0.6 on 2024-07-14 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0004_alter_activityschedule_coach'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
