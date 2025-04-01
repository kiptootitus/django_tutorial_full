from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Flights, Profile


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']
        extra_kwargs = {
            'password': {'write_only': True},  # Password should not be returned
            'email': {'required': True, 'allow_blank': False},  # Ensure email is required
        }

    @staticmethod
    def validate_username(value):
        """ Ensure username is unique """
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError(f"This username {value.username} is already taken.")
        return value

    @staticmethod
    def validate_email(value):
        """ Ensure email is unique """
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(f"This email {value} is already in use.")
        return value

    def create(self, validated_data):
        """ Override create method to hash the password """
        user = User.objects.create_user(**validated_data)
        return user

    @staticmethod
    def get_full_name(obj):
        """ Get full name of the user """
        return f"{obj.first_name} {obj.last_name}"


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class FlightsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flights
        fields = '__all__'

    def create(self, validated_data):
        return super().create(validated_data)

    def save(self, **kwargs):
        return super().save(**kwargs)


class SigninSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        """ Authenticate user """
        username = data.get("username")
        password = data.get("password")

        user = authenticate(username=username, password=password)
        if not user:
            raise serializers.ValidationError("Invalid credentials. Please try again.")

        data["user"] = user  # Store authenticated user for use in views
        return data
