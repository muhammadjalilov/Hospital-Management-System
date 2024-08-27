from django.core.cache import cache
from rest_framework import generics, permissions, status
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.patients.models import Patient
from apps.patients.serializers import PatientCreateSerializer, PatientsListSerializer, PatientSerializer
from apps.shared.permissions import IsDoctor, IsPatientOrReadOnly


class PatientCreateAPIView(generics.CreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientCreateSerializer
    permission_classes = [permissions.AllowAny, ]

    def perform_create(self, serializer):
        serializer.save()
        return Response({'message': 'Check email for activation your account'})

class PatientListAPIView(ListAPIView):
    serializer_class = PatientsListSerializer
    permission_classes = [IsDoctor, ]

    def get_queryset(self):
        return Patient.objects.filter(appointments__doctor=self.request.user.doctor,
                                      appointments__status=True).all().select_related('user').prefetch_related(
            'appointments__doctor', 'appointments').distinct()


class PatientRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Patient.objects.all().select_related('user')
    serializer_class = PatientSerializer
    permission_classes = [IsPatientOrReadOnly, ]
