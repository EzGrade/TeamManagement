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
    users = serializers.ListField(child=serializers.IntegerField(), required=False)

    class Meta:
        model = Team
        fields = ['pk', 'name', 'users']

    def create(self, validated_data):
        if Team.objects.filter(name=validated_data['name']).exists():
            raise serializers.ValidationError('Team with this name already exists')
        users = validated_data.pop('users', [])
        team = Team.objects.create(**validated_data)
        for user in users:
            user_obj = UserProfile.objects.get(pk=int(user))
            user_obj.team = team
            user_obj.save()
        return team

    def update(self, instance, validated_data):
        instance_name = validated_data.get('name', None)
        if instance_name and Team.objects.filter(name=instance_name).exclude(pk=instance.pk).exists():
            raise serializers.ValidationError('Team with this name already exists')

        instance.name = validated_data.get('name', instance.name)

        users = validated_data.get('users', [])
        if isinstance(users, list):
            users_list = UserProfile.objects.filter(team=instance)
            for user in users_list:
                user.team = None
                user.save()
        else:
            for user in users:
                instance.users.add(user)
        instance.save()
        return instance

    def to_representation(self, instance: Team):
        users = UserProfile.objects.filter(team=instance)
        users = UserSerializer(users, many=True).data
        return {
            "pk": instance.pk,
            "name": instance.name,
            "users": users
        }
