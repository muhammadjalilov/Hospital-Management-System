from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import CharField, IntegerField, ForeignKey, CASCADE, OneToOneField, ForeignObject, \
    PositiveSmallIntegerField
from phonenumber_field.modelfields import PhoneNumberField

from apps.shared.models import BaseModel
from apps.users.models import User


class Hospital(BaseModel):
    name = CharField(max_length=256)
    address = CharField(max_length=512, blank=True, null=True)
    phone_number = PhoneNumberField(blank=True, null=True)
    State = CharField(max_length=2, blank=True, default='UZ')
    zipcode = IntegerField(validators=[MaxValueValidator(999999), MinValueValidator(100000)], blank=True, null=True)

    def __str__(self):
        return self.name


class Department(BaseModel):
    name = CharField(max_length=256)
    hospital = ForeignKey(Hospital, on_delete=CASCADE, related_name='departments')

    def __str__(self):
        return f"{self.name}-{self.hospital.name}"


class Staff(BaseModel):
    user = OneToOneField(User, on_delete=CASCADE, related_name='staff')
