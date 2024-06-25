from django.contrib import admin

from team_management.models import UserProfile


# Register your models here.
@admin.register(UserProfile)
class UserProfile(admin.ModelAdmin):
    pass
