from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from apps.doctor.models import Doctor
from apps.hospital.models import Department, Hospital


class HospitalSerializer(ModelSerializer):
    class Meta:
        model = Hospital
        fields = ['name', 'address', 'phone_number']


class DepartmentSerializer(ModelSerializer):
    specialities = SerializerMethodField(read_only=True)
    class Meta:
        model = Department
        fields = ['name','specialities']

    def get_specialities(self,obj):
        if isinstance(obj,Department):
            return [speciality.name for speciality in obj.specialities.all()]