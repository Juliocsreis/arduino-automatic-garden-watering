from django.contrib import admin
from .models import HumidityData, Watering


class autoNowRead(admin.ModelAdmin):
    readonly_fields = ('time_stamp',)


admin.site.register(HumidityData, autoNowRead)
admin.site.register(Watering, autoNowRead)