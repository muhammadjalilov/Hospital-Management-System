from rest_framework import generics

from apps.hospital.models import Hospital, Department
from apps.hospital.serializers import HospitalSerializer, HospitalRetrieveSerializer


class HospitalListAPIView(generics.ListAPIView):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer

class HospitalRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Hospital
    serializer_class = HospitalRetrieveSerializer
