from django.contrib import admin
from .models import User


class UserFilters(admin.ModelAdmin):
    search_fields = ['id', 'email']
    pass


admin.site.register(User)