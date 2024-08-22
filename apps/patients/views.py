from rest_framework import generics
from rest_framework.generics import ListAPIView

from apps.patients.models import Patient
from apps.patients.serializers import PatientCreateSerializer, PatientsListSerializer


class PatientCreateAPIView(generics.CreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientCreateSerializer

class PatientListAPIView(ListAPIView):
    serializer_class = PatientsListSerializer

    def get_queryset(self):
        return Patient.objects.filter(appointments__doctor=self.request.user.doctor,appointments__status=True).all()