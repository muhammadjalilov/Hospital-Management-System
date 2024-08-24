from django.template.context_processors import request
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework import generics
from rest_framework.generics import ListCreateAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.appointments.models import Appointment, Invoice, Prescription
from apps.appointments.serializers import AppointmentSerializer, \
    PrescriptionSerializer, InvoiceListSerializer, AppointmentsListSerializer
from apps.patients.models import Room
from apps.shared.permissions import IsPatient, IsDoctor


class AppointmentCreateAPIView(generics.CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsPatient, ]

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(patient=self.request.user.patient)
        else:
            raise ValidationError("User must be logged in to create an appointment.")


class AppointmentListAPIView(generics.ListAPIView):
    serializer_class = AppointmentsListSerializer

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'doctor'):
            return Appointment.objects.filter(doctor=user.doctor).all().select_related('patient__user','doctor__user')
        elif hasattr(user, 'patient'):
            return Appointment.objects.filter(patient=user.patient).all().select_related('patient__user','doctor__user')


class UnconfirmedAppointmentListAPIView(generics.ListAPIView):
    serializer_class = AppointmentsListSerializer
    permission_classes = [IsDoctor, ]

    def get_queryset(self):
        return Appointment.objects.filter(doctor=self.request.user.doctor, status=False).all()


class ConfirmedAppointmentListAPIView(generics.ListAPIView):
    serializer_class = AppointmentsListSerializer
    permission_classes = [IsDoctor, ]

    def get_queryset(self):
        return Appointment.objects.filter(doctor=self.request.user.doctor, status=True).all()


class ChangeStatusAppointments(generics.RetrieveUpdateAPIView):
    serializer_class = AppointmentsListSerializer
    permission_classes = [IsDoctor,]

    def get_queryset(self):
        return Appointment.objects.filter(doctor=self.request.user.doctor, status=False).all()

    def update(self, request, *args, **kwargs):
        appointment = self.get_object()
        patient_data = appointment.patient
        doctor_data = self.request.user.doctor
        if appointment.doctor != doctor_data:
            return Response({'detail': 'You do not have permission to change this appointment.'},
                            status=status.HTTP_403_FORBIDDEN)

        serializer = self.get_serializer(appointment, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        cost = doctor_data.speciality.cost
        if appointment.bunk:
            cost = doctor_data.speciality.cost + doctor_data.speciality.bunk_cost
        Invoice.objects.create(
            patient=patient_data,
            cost=cost
        )
        appointment.patient.total_cost += cost
        Room.objects.assign_room(
            patient=patient_data,
            doctor=doctor_data
        )
        appointment.patient.save()
        self.perform_update(serializer)

        return Response(serializer.data)


class PrescriptionCreateListAPIView(ListCreateAPIView):
    serializer_class = PrescriptionSerializer

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'doctor'):
            return Prescription.objects.filter(doctor=self.request.user.doctor).select_related('doctor')
        elif hasattr(user, 'patient'):
            return Prescription.objects.filter(patient=self.request.user.patient).select_related('doctor')
        else:
            return Prescription.objects.none()

    def perform_create(self, serializer):
        user = self.request.user
        if hasattr(user, 'doctor'):
            serializer.save(doctor=user.doctor)
        else:
            raise ValidationError('Only doctors can write prescription')


class InvoiceListAPIView(generics.ListAPIView):
    serializer_class = InvoiceListSerializer

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'patient'):
            return Invoice.objects.filter(patient=user.patient).all().order_by('-created_at')
