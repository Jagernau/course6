from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer, UserCreateSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ("email", "first_name", "last_name", "password", "phone")


class UserCurrentSerializer(serializers.ModelSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        model = User
        fields = "__all__"
