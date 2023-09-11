from django.contrib import admin
from django.urls import path

from mysite.post import views

urlpatterns = [
    path("", views.index, name='index'),
]
