from rest_framework import serializers
from .models import UserProfile, Team


class UserSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    team = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all(), required=False)

    class Meta:
        model = UserProfile
        fields = ['pk', 'first_name', 'last_name', 'email']

    def create(self, validated_data):
        if UserProfile.objects.filter(email=validated_data['email']).exists():
            raise serializers.ValidationError('User with this email already exists')

        return UserProfile.objects.create(**validated_data)

    def to_representation(self, instance: UserProfile):
        return {
            "pk": instance.pk,
            "first_name": instance.first_name,
            "last_name": instance.last_name,
            "email": instance.email
        }


class TeamSerializer(serializers.Serializer):
    pk = serializers.IntegerField(required=False)
    name = serializers.CharField()
    users = serializers.ListField(child=serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.all()),
                                  required=False)

    class Meta:
        model = Team
        fields = ['pk', 'name', 'users']

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
        return {
            "pk": instance.pk,
            "name": instance.name,
            "users": UserSerializer(instance.users.all(), many=True).data
        }
