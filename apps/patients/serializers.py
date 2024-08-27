from django.core.cache import cache
from django.utils.crypto import get_random_string
from rest_framework import serializers

from apps.patients.models import Patient
from apps.shared.tasks import send_activation_email

from apps.users.serializers import UserSerializer


class PatientCreateSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Patient
        fields = ['user']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = UserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()
        user.save()
        patient = Patient.objects.create(user=user)
        # patient.total_cost = patient.get_total_cost_invoices()
        patient.save()

        return patient


class PatientsListSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        user_data = representation.pop('user')
        representation['first_name'] = user_data.get('first_name')
        representation['last_name'] = user_data.get('last_name')
        return representation

    class Meta:
        model = Patient
        fields = ['user']


class PatientSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    total_cost = serializers.ReadOnlyField()

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        user_data = representation.pop('user')
        representation['first_name'] = user_data.get('first_name')
        representation['last_name'] = user_data.get('last_name')
        representation['address'] = user_data.get('address')
        representation['avatar'] = user_data.get('avatar')
        representation['birthdate'] = user_data.get('birthdate')
        representation['phone_number'] = user_data.get('phone_number')
        representation['gender'] = user_data.get('gender')
        representation.update(user_data)
        return representation

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)

        instance = super().update(instance, validated_data)

        if user_data:
            user = instance.user
            user_serializer = UserSerializer(user, data=user_data, partial=True)
            if user_serializer.is_valid():
                user_serializer.save()

        return instance

    class Meta:
        model = Patient
        fields = ['user', 'total_cost']
