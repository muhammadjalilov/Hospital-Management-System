from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from apps.hospital.models import Department
from apps.shared.models import BaseModel
from apps.users.models import User


class Specialities(BaseModel):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True, default=name)
    department = models.ForeignKey(Department, related_name='specialities', on_delete=models.CASCADE, null=True)
    cost = models.DecimalField(max_digits=10,decimal_places=2,validators=[MinValueValidator(0)], default=50)
    bunk_cost = models.DecimalField(max_digits=10,decimal_places=2,validators=[MinValueValidator(0)], default=0)

    def __str__(self):
        return self.name


class Doctor(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor')
    experience = models.PositiveSmallIntegerField(default=0)
    speciality = models.ForeignKey(Specialities, on_delete=models.CASCADE, related_name='doctors')
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
