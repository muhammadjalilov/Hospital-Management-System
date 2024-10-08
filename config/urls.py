"""
URL configuration for ff project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from debug_toolbar.toolbar import debug_toolbar_urls
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/doctor/", include('apps.doctor.urls')),
    path("api/shared/", include('apps.shared.urls')),
    path("api/patients/", include('apps.patients.urls')),
    path("api/hospitals/", include('apps.hospital.urls')),
    path("api/appointments/", include('apps.appointments.urls')),
    path('api/v1/auth/', include('djoser.urls')),  # URL for Djoser
    path('api/v1/auth/', include('djoser.urls.jwt')),  # URL for JWT
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
] + debug_toolbar_urls()
