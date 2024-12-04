from rest_framework import serializers
from .models import CustomUser, Costume


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'password']

    def create(self, validated_data):
        # Use the CustomUser manager to create a user
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user


class CostumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Costume
        fields = ['id', 'title', 'description', 'price_per_day', 'size', 'category', 'available', 'date_listed', 'owner']
        read_only_fields = ['id', 'date_listed', 'owner']
