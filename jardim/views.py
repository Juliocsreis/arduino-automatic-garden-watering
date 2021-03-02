from django.shortcuts import render
from .models import HumidityData, Watering


def dashboardView(request):
    if request.method == "GET":
        last_humidity = HumidityData.objects.latest("time_stamp")
        humidity = last_humidity.humidity
        time = last_humidity.time_stamp
        last_watering = Watering.objects.latest("time_stamp")
        context = {"humidity": humidity, "time": time, "last_watering_time": last_watering.time_stamp,
                   "last_watering_pre_humidity": last_watering.pre_soil_humidity}
        return render(request, "base_app.html", context)
