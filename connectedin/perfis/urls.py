from django.contrib import admin
from django.urls import path
from perfis import views

urlpatterns = [
    path('', views.index),
]
