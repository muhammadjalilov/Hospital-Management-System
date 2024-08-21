from rest_framework.generics import CreateAPIView

from apps.doctor.models import Doctor
from apps.doctor.serializers import DoctorSerializer


class DoctorRegisterAPIView(CreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
