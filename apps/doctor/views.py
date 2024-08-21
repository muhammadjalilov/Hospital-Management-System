from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from apps.doctor.models import Doctor, Specialities
from apps.doctor.serializers import DoctorSerializer, DoctorListSerializer, DoctorDetailSerializer, SpecialitySerializer


class DoctorRegisterAPIView(CreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class DoctorListAPIView(ListAPIView):
    queryset = Doctor.objects.filter(status=True).all()
    serializer_class = DoctorListSerializer
    # permission_classes = [IsAuthenticated,]


class DoctorRetrieveAPIView(RetrieveAPIView):
    queryset = Doctor.objects.filter(status=True).all()
    serializer_class = DoctorDetailSerializer
    # permission_classes = [IsAuthenticated, ]

