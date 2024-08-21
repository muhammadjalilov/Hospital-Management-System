from django.contrib.auth.models import AbstractUser
from django.core.validators import validate_email
from django.db.models import EmailField, DateField, ImageField, CharField
from phonenumber_field.modelfields import PhoneNumberField

from apps.shared.models import BaseModel
from apps.users.choices import GenderChoices


class User(AbstractUser, BaseModel):
    email = EmailField(db_index=True, unique=True, validators=[validate_email], help_text='Email is required')
    birthdate = DateField()
    avatar = ImageField(upload_to='avatars/',default='avatars/default.jpg')
    gender = CharField(max_length=5,choices=GenderChoices.choices)
    address = CharField(max_length=512,blank=True, null=True)
    phone_number = PhoneNumberField(blank=True, null=True)
