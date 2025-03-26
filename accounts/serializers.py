from . models import Profile
from django.contrib.auth.models import User
from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']
        extra_kwargs = {
            'password': {'write_only': True},  # Password should not be returned
            'email': {'required': True, 'allow_blank': False},  # Ensure email is required
        }

    def validate_username(self, value):
        """ Ensure username is unique """
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("This username is already taken.")
        return value

    def validate_email(self, value):
        """ Ensure email is unique """
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value

    def create(self, validated_data):
        """ Override create method to hash the password """
        user = User.objects.create_user(**validated_data)  # Automatically hashes the password
        return user

class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = Profile
    fields = '__all__'
