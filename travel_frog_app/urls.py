from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dashboard),
    path('trip/new', views.new_trip),
    path('trip/create', views.create_trip),
    path('trip/edit/<int:trip_id>', views.edit_trip),
    path('trip/update/<int:trip_id>', views.update_trip),
    path('trip/delete/<int:trip_id>', views.remove_trip),
    path('trip/<int:trip_id>', views.show_trip),
    path('trip/<int:trip_id>/new_plan', views.new_plan_for_trip),
    path('plan/create', views.create_plan),
    path('add/<int:plan_id>', views.add_plan),
    path('remove/<int:plan_id>', views.remove_plan),
    path('plan/edit/<int:plan_id>', views.edit_plan),
    path('plan/update/<int:plan_id>', views.update_plan),
    path('plan/delete/<int:plan_id>', views.delete_plan),
    path('plan/new', views.new_plan),
]