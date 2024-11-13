from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('surveys/', include('encuestas.urls')),  # Registrar las URLs de la app de encuestas
]
