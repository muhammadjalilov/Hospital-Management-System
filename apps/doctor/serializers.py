from rest_framework.relations import HyperlinkedIdentityField
from rest_framework import serializers

from apps.doctor.models import Doctor, Specialities
from apps.hospital.serializers import DepartmentSerializer
from apps.users.serializers import UserSerializer


class SpecialitySerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)

    class Meta:
        model = Specialities
        fields = ['name', 'description', 'cost', 'department']


class SpecialitySerializerListRetrieve(serializers.ModelSerializer):
    class Meta:
        model = Specialities
        fields = ['name', 'description', 'cost']


class DoctorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Doctor
        exclude = ['status']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = UserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()
        doctor = Doctor.objects.create(user=user, **validated_data)
        return doctor


class DoctorDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    speciality = SpecialitySerializer(read_only=True)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        user_data = representation.pop('user', {})
        representation['first_name'] = user_data.get('first_name', '')
        representation['last_name'] = user_data.get('last_name', '')
        representation['address'] = user_data.get('address', '')
        representation['phone_number'] = user_data.get('phone_number', '')
        representation['gender'] = user_data.get('gender', '')
        representation.update(user_data)
        return representation

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)

        instance = super().update(instance, validated_data)

        if user_data:
            user = instance.user
            user_serializer = UserSerializer(user, data=user_data, partial=True)
            if user_serializer.is_valid():
                user_serializer.save()

        return instance

    class Meta:
        model = Doctor
        fields = ['user', 'experience', 'speciality']


class DoctorListSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    speciality = serializers.CharField(source="speciality.name")
    hospital = serializers.CharField(source="speciality.department.hospital.name")
    hospital_address = serializers.CharField(source="speciality.department.hospital.address")
    url = HyperlinkedIdentityField(view_name='doctor:doctor_retrieve', lookup_field='pk')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        user_data = representation.pop('user', {})
        representation['first_name'] = user_data.get('first_name', '')
        representation['last_name'] = user_data.get('last_name', '')
        return representation

    class Meta:
        model = Doctor
        fields = ['user', 'speciality', 'url', 'hospital', 'hospital_address']
