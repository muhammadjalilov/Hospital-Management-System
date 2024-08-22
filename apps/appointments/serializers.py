from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import serializers

from apps.appointments.models import Appointment, Prescription, Invoice


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['doctor', 'datetime', 'bunk']

    def create(self, validated_data):
        doctor = validated_data['doctor']
        if Appointment.objects.filter(doctor=doctor, status=False).exists():
            return Response('The selected doctor has not confirmed the appointment.',
                            status=status.HTTP_400_BAD_REQUEST)
        return super().create(validated_data)


class AppointmentsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['datetime', 'status']

    def update(self, instance, validated_data):
        if 'status' in validated_data:
            instance.status = validated_data['status']
            instance.save()
        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        first_name = instance.patient.user.first_name
        last_name = instance.patient.user.last_name
        first_name_d = instance.doctor.user.first_name
        last_name_d = instance.doctor.user.last_name
        representation['Patient'] = f"{first_name} {last_name}"
        representation['Doctor'] = f"{first_name_d} {last_name_d}"
        return representation


class PrescriptionSerializer(serializers.ModelSerializer):
    doctor = serializers.ReadOnlyField(source='doctor.id')

    class Meta:
        model = Prescription
        fields = ['patient', 'doctor', 'medication_name', 'advice', 'pharmacy']

    def create(self, validated_data):
        patient = validated_data['patient']
        doctor = self.context['request'].user.doctor
        if not Appointment.objects.filter(patient=patient, doctor=doctor, status=True).exists():
            raise ValidationError('You cannot write a prescription for this patient.')
        return super().create(validated_data)


class InvoiceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['service_description', 'paid', 'cost']
