from django.db import models
from log_reg_app.models import User
import enum

# Create your models here.

class TripManager(models.Manager):
    def validate(self, form_data):
        errors = {}
        if len(form_data['destination']) < 3:
            errors['destination'] = "Destination must be at least 3 characters"
        if len(form_data['description']) < 5:
            errors['description'] = "Description must be at least 5 characters"
        return errors

class PlanManager(models.Manager):
    def validate(self, form_data):
        errors = {}
        if len(form_data['name']) < 3:
                errors['name'] = "Name must be at least 3 characters"
        if len(form_data['destination']) < 3:
            errors['destination'] = "Location must be at least 3 characters"
        if len(form_data['description']) < 5:
            errors['description'] = "Description must be at least 5 characters"
        return errors

class Plan(models.Model):
    DEFAULT = 'Other'
    ACTIVITY = 'Activity'
    LODGING = 'Lodging'
    DINING = 'Dining'
    PLAN_TYPES = (
        (DEFAULT, "Other"),
        (ACTIVITY, "Activity"),
        (LODGING, "Lodging"),
        (DINING, "Dining"),
    )

    name = models.CharField(max_length=140)
    description = models.CharField(max_length=140)
    destination = models.CharField(max_length=140)
    plan_type = models.CharField(choices=PLAN_TYPES, default=DEFAULT, max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, related_name='user_plans', on_delete=models.CASCADE, default='')

    objects = PlanManager()

class Trip(models.Model):
    destination = models.CharField(max_length=140)
    description = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, related_name='user_trips', on_delete=models.CASCADE, default='')
    trip_plans = models.ManyToManyField(Plan, related_name="trips_with_plan")

    objects = TripManager()


    