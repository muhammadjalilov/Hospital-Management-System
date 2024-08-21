from rest_framework.exceptions import ValidationError
from rest_framework.fields import HiddenField
from rest_framework.serializers import ModelSerializer

from apps.appointments.models import Appointment


class AppointmentSerializer(ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['doctor', 'datetime']

    def create(self, validated_data):
        doctor = validated_data['doctor']
        if Appointment.objects.filter(doctor=doctor, status=False).exists():
            raise ValidationError('The selected doctor has not confirmed the appointment.')
        return super().create(validated_data)


class AppointmentListSerializer(ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['doctor', 'created_at', 'datetime', 'status']


class AppointmentsForDoctors(ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['patient', 'datetime']

