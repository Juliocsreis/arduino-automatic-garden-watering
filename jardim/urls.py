from django.urls import path
from . import views


app_name = 'jardim'

urlpatterns = [
    path("dashboard/", views.dashboardView, name="dashboardView")
]