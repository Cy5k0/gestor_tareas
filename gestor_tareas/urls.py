from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),  # URLs de autenticación
    path("registro/", include("usuarios.urls")),  # URL de registro
    path("tareas/", include("tareas.urls")),  # URLs de tareas
    path("", include("tareas.urls")),  # Ruta raíz muestra las tareas
]
