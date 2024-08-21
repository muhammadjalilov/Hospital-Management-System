from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from apps.patients.models import Patient
from apps.patients.serializers import PatientCreateSerializer


class PatientCreateAPIView(CreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientCreateSerializer