from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsDoctor(BasePermission):
    message = 'You must be a doctor to access this resource.'

    def has_permission(self, request, view):
        user = request.user
        return hasattr(user, 'doctor')


class IsPatient(BasePermission):
    message = 'You must be a patient to access this resource.'

    def has_permission(self, request, view):
        user = request.user
        return hasattr(user, 'patient')


class IsDoctorOrReadOnly(BasePermission):
    message = 'You must be a doctor to access this resource.'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if hasattr(request.user,'doctor'):
            return obj == request.user.doctor
        return False


