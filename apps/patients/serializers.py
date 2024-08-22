from rest_framework import serializers

from apps.appointments.models import Appointment
from apps.appointments.serializers import AppointmentsForDoctors
from apps.patients.models import Patient
from apps.users.models import User
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
        patient = Patient.objects.create(user=user)
        patient.total_cost = patient.get_total_cost_invoices()
        patient.save()

        return patient


class PatientsListSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    appointments = serializers.PrimaryKeyRelatedField(many=True,read_only=True)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        user_data = representation.pop('user')
        representation['first_name'] = user_data.get('first_name')
        representation['last_name'] = user_data.get('last_name')

        doctor = self.context['request'].user.doctor

        if 'appointments' in representation and len(representation['appointments']) > 0:
            for appointment in [i for i in representation['appointments'] if i.get('doctor')==doctor.id]:
                representation['datetime'] = appointment.get('datetime')
                representation['status'] = appointment.get('status')

        representation.pop('appointments')
        return representation

    class Meta:
        model = Patient
        fields = ['user', 'appointments']
