from django.contrib import admin
from .models import Trip, Plan

# Register your models here.

class TripAdmin(admin.ModelAdmin):
    pass

admin.site.register(Trip, TripAdmin)

class PlanAdmin(admin.ModelAdmin):
    pass

admin.site.register(Plan, PlanAdmin)