from rest_framework.serializers import ModelSerializer

from apps.patients.models import Patient
from apps.users.serializers import UserSerializer


class PatientCreateSerializer(ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Patient
        fields = ['user']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = UserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()
        patient = Patient.objects.create(user=user)
        patient.total_cost = patient.get_total_cost_invoices()
        patient.save()

        return patient

