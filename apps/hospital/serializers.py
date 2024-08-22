from rest_framework.fields import SerializerMethodField
from rest_framework import serializers
from rest_framework.relations import HyperlinkedIdentityField

from apps.hospital.models import Department, Hospital


class DepartmentSerializer(serializers.ModelSerializer):
    specialities = SerializerMethodField(read_only=True)

    class Meta:
        model = Department
        fields = ['name', 'specialities']

    def get_specialities(self, obj):
        return [speciality.name for speciality in obj.specialities.all()]


class HospitalSerializer(serializers.ModelSerializer):
    url = HyperlinkedIdentityField(view_name='hospital:hospital',lookup_field='pk')
    class Meta:
        model = Hospital
        fields = ['name', 'address', 'phone_number','url']


class HospitalRetrieveSerializer(serializers.ModelSerializer):
    departments = serializers.SerializerMethodField()

    class Meta:
        model = Hospital
        fields = ['name', 'address', 'phone_number', 'departments']

    def get_departments(self,obj):
        departments = obj.departments.all()
        return DepartmentSerializer(departments,many=True).data
