import os
import random

from django.contrib.sites.shortcuts import get_current_site
from django.core.cache import cache
from django.utils.crypto import get_random_string
from rest_framework.exceptions import ValidationError
from rest_framework import fields
from rest_framework import serializers
from rest_framework.reverse import reverse
from rest_framework_simplejwt.tokens import RefreshToken
from dotenv import load_dotenv

from apps.shared.tasks import send_activation_email
from apps.users.models import User

load_dotenv()


class UserSerializer(serializers.ModelSerializer):
    password = fields.CharField(write_only=True, required=True, style={'input_type': 'password'})
    confirm_password = fields.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'address', 'avatar', 'birthdate', 'gender',
                  'phone_number', 'password', 'confirm_password']
        ref_name = 'CustomUserSerializer'

    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')

        if password != confirm_password:
            raise ValidationError('Passwords should match')

        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data.pop('confirm_password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        # generate JWT
        token = RefreshToken.for_user(user).access_token

        # make link
        current_site = os.getenv('DOMAIN_NAME')
        relativeLink = reverse('shared:email-verify')
        abs_url = 'http://'+ current_site+relativeLink+'?token='+str(token)

        # handle celery task
        send_activation_email.delay(user.email, abs_url,user.username)

        return user
