from django.contrib import admin
from django.urls import path
from app import views
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("log_in", views.log_in, name="log_in"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("result", views.result, name="result"),
    path("log_out", views.log_out, name="log_out"),
    path('register', views.register, name='register')
]
