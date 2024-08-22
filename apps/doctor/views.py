from rest_framework import generics, permissions

from apps.doctor.models import Doctor
from apps.doctor.serializers import DoctorSerializer, DoctorListSerializer, DoctorDetailSerializer
from apps.shared.permissions import IsDoctorOrReadOnly


class DoctorRegisterAPIView(generics.CreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.AllowAny,]

class DoctorListAPIView(generics.ListAPIView):
    queryset = Doctor.objects.filter(status=True).all()
    serializer_class = DoctorListSerializer


class DoctorRetrieveAPIView(generics.RetrieveUpdateAPIView):
    queryset = Doctor.objects.filter(status=True).all()
    serializer_class = DoctorDetailSerializer
    permission_classes = [IsDoctorOrReadOnly,]

