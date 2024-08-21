from django.contrib import admin

from apps.doctor.models import Specialities, Doctor

admin.site.register(Specialities)
admin.site.register(Doctor)