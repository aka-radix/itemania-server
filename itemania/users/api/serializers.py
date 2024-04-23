import django.contrib.auth.password_validation as password_validators
from rest_framework import serializers

from itemania.users.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def save(self, request) -> User:
        user_data = request.data
        user = User(username=user_data["username"])
        user.set_password(user_data["password"])
        user.save()
        return user

    def validate_password(self, password) -> None:
        """Run password validation."""

        password_validators.validate_password(password=password)
