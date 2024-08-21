from rest_framework.serializers import ModelSerializer

from apps.doctor.models import Doctor
from apps.users.serializers import UserSerializer


class DoctorSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Doctor
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer().create(validated_data=user_data)
        doctor = Doctor.objects.create(user=user, **validated_data)
        return doctor
