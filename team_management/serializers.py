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
        fields = ['pk', 'name']

    def create(self, validated_data):
        if Team.objects.filter(name=validated_data['name']).exists():
            raise serializers.ValidationError('Team with this name already exists')

        users = validated_data.pop('users', [])
        team = Team.objects.create(**validated_data)
        for user in users:
            team.users.add(user)
        return team

    def update(self, instance, validated_data):
        instance_name = validated_data.get('name', None)
        if instance_name and Team.objects.filter(name=instance_name).exclude(pk=instance.pk).exists():
            raise serializers.ValidationError('Team with this name already exists')

        instance.name = validated_data.get('name', instance.name)

        users = validated_data.get('users', [])
        if isinstance(users, list):
            instance.users.clear()
        for user in users:
            instance.users.add(user)
        instance.save()
        return instance

    def to_representation(self, instance: Team):
        users = UserProfile.objects.filter(team=instance)
        return {
            "pk": instance.pk,
            "name": instance.name,
            "users": UserSerializer(users.all(), many=True).data
        }
