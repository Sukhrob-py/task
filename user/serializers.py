from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers

from .models import User


class RegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class LoginSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]
