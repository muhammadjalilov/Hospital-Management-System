from rest_framework import generics, permissions
from rest_framework.generics import ListAPIView

from apps.patients.models import Patient
from apps.patients.serializers import PatientCreateSerializer, PatientsListSerializer, PatientSerializer
from apps.shared.permissions import IsDoctor, IsPatientOrReadOnly


class PatientCreateAPIView(generics.CreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientCreateSerializer
    permission_classes = [permissions.AllowAny, ]


class PatientListAPIView(ListAPIView):
    serializer_class = PatientsListSerializer
    permission_classes = [IsDoctor, ]

    def get_queryset(self):
        return Patient.objects.filter(appointments__doctor=self.request.user.doctor,
                                      appointments__status=True).all().distinct()


class PatientRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsPatientOrReadOnly, ]
