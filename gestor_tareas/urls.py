from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "accounts/", include("django.contrib.auth.urls")
    ),  # Incluimos las rutas de autenticación predeterminadas
    path(
        "", include("usuarios.urls")
    ),  # Incluimos las rutas de nuestra app de usuarios
]
