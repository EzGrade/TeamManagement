from rest_framework import serializers
from .models import UserProfile, Team


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['pk', 'first_name', 'last_name', 'email']

    def create(self, validated_data):
        return UserProfile.objects.create(**validated_data)

    def to_representation(self, instance: UserProfile):
        return {
            "pk": instance.pk,
            "first_name": instance.first_name,
            "last_name": instance.last_name,
            "email": instance.email
        }


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['pk', 'name', 'users']

    def create(self, validated_data):
        if Team.objects.filter(name=validated_data.get('name')).exists():
            raise serializers.ValidationError("Team with this name already exists")
        users = validated_data.pop('users', [])
        team = Team.objects.create(**validated_data)
        team.users.set(users)
        return team

    def update(self, instance: Team, validated_data):
        if Team.objects.filter(name=validated_data.get('name')).exists() and instance.name != validated_data.get(
                'name'):
            raise serializers.ValidationError("Team with this name already exists")
        instance.name = validated_data.get('name', instance.name)
        users = validated_data.pop('users', None)
        instance = super().update(instance, validated_data)
        if users is not None:
            instance.users.set(users)
        return instance

    def to_representation(self, instance: Team):
        users = instance.users
        users = UserSerializer(users, many=True).data
        return {
            "pk": instance.pk,
            "name": instance.name,
            "users": users
        }
