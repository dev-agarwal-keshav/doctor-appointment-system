from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('submit', views.submit, name="submit"),
    path('about', views.about, name="about"),
    path('records', views.records, name="records"),
    path('schedule', views.schedule, name="schedule"),
]