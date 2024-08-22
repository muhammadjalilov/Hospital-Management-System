from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.doctor.models import Doctor, Specialities
from apps.doctor.serializers import DoctorSerializer, DoctorListSerializer, DoctorDetailSerializer, SpecialitySerializer


class DoctorRegisterAPIView(generics.CreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class DoctorListAPIView(generics.ListAPIView):
    queryset = Doctor.objects.filter(status=True).all()
    serializer_class = DoctorListSerializer
    # permission_classes = [IsAuthenticated,]


class DoctorRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Doctor.objects.filter(status=True).all()
    serializer_class = DoctorDetailSerializer
    # permission_classes = [IsAuthenticated, ]

