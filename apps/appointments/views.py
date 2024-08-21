from django.shortcuts import render
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.appointments.models import Appointment
from apps.appointments.serializers import AppointmentSerializer, AppointmentListSerializer,AppointmentsForDoctors


class AppointmentCreateAPIView(CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(patient=self.request.user)
        else:
            raise ValidationError("User must be logged in to create an appointment.")


class AppointmentListAPIView(ListAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentListSerializer


class UnconfirmedAppointmentListAPIView(ListAPIView):
    serializer_class = AppointmentsForDoctors
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        return Appointment.objects.filter(doctor=self.request.user.doctor, status=False).all()

class ConfirmedAppointmentListAPIView(ListAPIView):
    serializer_class = AppointmentsForDoctors
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        return Appointment.objects.filter(doctor=self.request.user.doctor, status=True).all()
