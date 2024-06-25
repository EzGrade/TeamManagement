from django.contrib import admin

from team_management.models import UserProfile, Team


# Register your models here.
@admin.register(UserProfile)
class UserProfile(admin.ModelAdmin):
    list_display = ['pk', 'full_name', 'email', 'team']


@admin.register(Team)
class Team(admin.ModelAdmin):
    list_display = ['pk', 'name']
    filter_horizontal = ['users']
