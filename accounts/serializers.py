from rest_framework import serializers
from .models import CustomUser
from django.core.exceptions import ValidationError


class CustomUserSerializer(serializers.ModelSerializer):
    # Write-only password field to ensure it is not included in API responses
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'password']

    def validate_password(self, value):
        # Ensure password length is at least 8 characters
        if len(value) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        return value

    def create(self, validated_data):
        # Check if the email already exists
        if CustomUser.objects.filter(email=validated_data['email']).exists():
            raise serializers.ValidationError({"email": "This email is already in use."})

        # Check if the username already exists
        if CustomUser.objects.filter(username=validated_data['username']).exists():
            raise serializers.ValidationError({"username": "This username is already in use."})

        # Create the user using the CustomUser manager
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user
