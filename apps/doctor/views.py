from rest_framework import generics, permissions
from rest_framework.response import Response

from apps.doctor.models import Doctor
from apps.doctor.serializers import DoctorSerializer, DoctorListSerializer, DoctorDetailSerializer
from apps.shared.permissions import IsDoctorOrReadOnly


class DoctorRegisterAPIView(generics.CreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.AllowAny, ]

    def perform_create(self, serializer):
        serializer.save()
        return Response({'message': 'Check email for activation your account'})


class DoctorListAPIView(generics.ListAPIView):
    queryset = Doctor.objects.filter(status=True).all().select_related('user', 'speciality__department__hospital')
    serializer_class = DoctorListSerializer


class DoctorRetrieveAPIView(generics.RetrieveUpdateAPIView):
    queryset = Doctor.objects.filter(status=True).all().select_related('user')
    serializer_class = DoctorDetailSerializer
    permission_classes = [IsDoctorOrReadOnly, ]
