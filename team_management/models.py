from django.db import models


class UserProfile(models.Model):
    first_name = models.CharField(
        max_length=100,
        verbose_name='First Name'
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name='Last Name'
    )
    email = models.EmailField(
        unique=True,
        verbose_name='Email'
    )
    team = models.ForeignKey(
        'Team',
        on_delete=models.SET_NULL,
        null=True,
        related_name='users',
        editable=False,
        verbose_name='Team'
    )

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'
        ordering = [
            'first_name',
            'last_name',
            'email'
        ]

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Team(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Team Name'
    )

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'
        ordering = [
            'name'
        ]

    @property
    def users(self):
        return self.user.all()

    def __str__(self):
        return self.name
