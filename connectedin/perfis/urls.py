from django.contrib import admin
from django.urls import path,re_path
from perfis import views

urlpatterns = [
    path('', views.index),
    re_path(r'^perfis/(?P<perfil_id>\d+)/$', views.exibir)
]
