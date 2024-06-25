from rest_framework import serializers
from .models import UserProfile, Team


class UserSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()

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
