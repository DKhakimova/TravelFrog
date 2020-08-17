from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create', views.create),
    path('login', views.login),
    path('logout', views.logout),
]