from django.contrib.auth.models import AbstractUser
from django.core.validators import validate_email
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from apps.shared.models import BaseModel
from apps.users.choices import GenderChoices


class User(AbstractUser, BaseModel):
    email = models.EmailField(db_index=True, unique=True, validators=[validate_email], help_text='Email is required')
    birthdate = models.DateField()
    avatar = models.ImageField(upload_to='avatars/',default='avatars/default.jpg')
    gender = models.CharField(max_length=5,choices=GenderChoices.choices)
    address = models.CharField(max_length=512,blank=True, null=True)
    phone_number = PhoneNumberField(blank=True, null=True)
    is_verified = models.BooleanField(default=False)