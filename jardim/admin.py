from django.contrib import admin
from .models import esp8266Test


class espAdmin(admin.ModelAdmin):
    readonly_fields = ('time_stamp',)


admin.site.register(esp8266Test, espAdmin)