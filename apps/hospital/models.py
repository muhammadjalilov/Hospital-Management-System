from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from apps.shared.models import BaseModel
from apps.users.models import User


class Hospital(BaseModel):
    name = models.CharField(max_length=256)
    address = models.CharField(max_length=512, blank=True, null=True)
    phone_number = PhoneNumberField(blank=True, null=True)
    State = models.CharField(max_length=2, blank=True, default='UZ')
    zipcode = models.IntegerField(validators=[MaxValueValidator(999999), MinValueValidator(100000)], blank=True, null=True)

    def __str__(self):
        return self.name


class Department(BaseModel):
    name = models.CharField(max_length=256)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='departments')

    def __str__(self):
        return f"{self.name}-{self.hospital.name}"

