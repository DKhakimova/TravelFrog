# Generated by Django 3.1 on 2020-08-13 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel_frog_app', '0004_auto_20200810_0731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='plan_type',
            field=models.CharField(choices=[('Other', 'Other'), ('Activity', 'Activity'), ('Lodging', 'Lodging'), ('Dining', 'Dining')], default='Other', max_length=20),
        ),
    ]
