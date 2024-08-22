from rest_framework import generics

from apps.hospital.models import Hospital, Department
from apps.hospital.serializers import HospitalSerializer, DepartmentSerializer


class HospitalListAPIView(generics.ListAPIView):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer


class DepartmentListAPIView(generics.ListAPIView):
    serializer_class = DepartmentSerializer

    def get_queryset(self):
        departments = Department.objects.all()
        seen = set()
        distinct_departments = []
        for dept in departments:
            if dept.name not in seen:
                seen.add(dept.name)
                distinct_departments.append(dept)
        return distinct_departments
