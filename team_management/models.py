from django.db import models


class UserProfile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    team = models.OneToOneField("Team", on_delete=models.SET_NULL, null=True, related_name='user_profile')

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Team(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
