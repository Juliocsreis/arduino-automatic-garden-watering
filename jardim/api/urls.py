from django.urls import path
from . import viewsets

app_name = 'jardim_api'

urlpatterns = [
    path('sendHumidity/', viewsets.humidity, name='humidity'),
]