from django.contrib import admin

from team_management.models import UserProfile, Team


# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'full_name',
        'email',
        'team'
    ]


class UserProfileInline(admin.TabularInline):
    model = UserProfile


@admin.register(Team)
class Team(admin.ModelAdmin):
    list_display = [
        'pk',
        'name'
    ]
    inlines = [
        UserProfileInline
    ]
