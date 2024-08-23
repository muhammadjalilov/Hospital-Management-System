from rest_framework.exceptions import ValidationError
from rest_framework import fields
from rest_framework import serializers

from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    password = fields.CharField(write_only=True, required=True, style={'input_type': 'password'})
    confirm_password = fields.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'address', 'avatar', 'birthdate', 'gender',
                  'phone_number','password','confirm_password']
        ref_name = 'CustomUserSerializer'

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise ValidationError('Passwords should be match')
        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data.pop('confirm_password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
