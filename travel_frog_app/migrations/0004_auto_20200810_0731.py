# Generated by Django 3.1 on 2020-08-10 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel_frog_app', '0003_plan_plan_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plan',
            old_name='destination',
            new_name='name',
        ),
    ]
