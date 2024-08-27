from django.urls import path
from .views import VerifyEmail

app_name = 'shared'
urlpatterns = [
    path('email-verify/', VerifyEmail.as_view(), name='email-verify'),
]