from django.urls import path
from . import viewsets

urlpatterns = [
    path('esp8266/', viewsets.test_post),
]