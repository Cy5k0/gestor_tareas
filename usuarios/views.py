from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm


class Registro(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy(
        "login"
    )  # Redirige a la página de inicio de sesión después del registro
    template_name = "registration/registro.html"
