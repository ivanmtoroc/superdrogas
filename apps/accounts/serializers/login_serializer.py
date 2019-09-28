"""
Login serializer

Serializer to user and client login
"""

# Django
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError

# Django Rest Framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token

# Accounts models
from apps.accounts.models import User


class LoginSerializer(serializers.Serializer):
    """
    Login serializer

    To user and client login
    """
    username = serializers.CharField()
    password = serializers.CharField()
    is_staff = serializers.BooleanField()

    def validate_username(self, value):
        """
        validate_username confirms if the user exists and is active
        """
        try:
            user = User.objects.get(username=value)
        except User.DoesNotExist:
            raise ValidationError('User does not exist.')

        if not user.is_active:
            raise ValidationError('User is not active.')

        self.context['user'] = user

        return value

    def validate(self, attrs):
        """
        validate confirm if the credentials are correct
        """
        user = authenticate(username=attrs['username'], password=attrs['password'])
        is_staff = attrs['is_staff']

        if not user:
            raise serializers.ValidationError({'password': ['Invalid credentials.']})

        if (is_staff and user.rol == 'CM') or (not is_staff and user.rol != 'CM'):
            raise ValidationError({'username': ['User does not exist.']})

        return attrs

    def create(self, validated_data):
        """
        create obtains or generates the user's token
        """
        token, _ = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key
