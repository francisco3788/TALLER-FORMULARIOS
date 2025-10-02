"""
URL configuration for taller_formularios_DANILO_FRANCISCO project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from asistencia import views as asistencia_views
from solicitudes import views as solicitudes_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Asistencia
    path('asistencia/', asistencia_views.registrar_asistencia, name='asistencia'),
    path('asistencia/confirmacion/', asistencia_views.confirmacion, name='asistencia_confirmacion'),

    # Solicitudes
    path('solicitudes/', solicitudes_views.registrar_solicitud, name='solicitud'),
    path('solicitudes/confirmacion/', solicitudes_views.confirmacion, name='solicitud_confirmacion'),
]

