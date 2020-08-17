# Generated by Django 3.1 on 2020-08-10 05:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('log_reg_app', '0001_initial'),
        ('travel_frog_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='traveler',
        ),
        migrations.AddField(
            model_name='trip',
            name='creator',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='user_trips', to='log_reg_app.user'),
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=140)),
                ('description', models.CharField(max_length=140)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='user_plans', to='log_reg_app.user')),
            ],
        ),
        migrations.AddField(
            model_name='trip',
            name='trip_plans',
            field=models.ManyToManyField(related_name='trips_with_plan', to='travel_frog_app.Plan'),
        ),
    ]