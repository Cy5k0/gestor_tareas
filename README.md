# GESTOR DE TAREAS

## PASO A PASO

### Paso 1: Crear un entorno virtual y configurar Django

1. **Crear el entorno virtual**:

Abre una terminal en la carpeta donde deseas crear el proyecto y ejecuta:

```bash
python3 -m venv gestor_tareas_env
```

Esto creará un entorno virtual llamado `gestor_tareas_env`.

2. **Activar el entorno virtual**:

- En Linux/macOS:

```bash
source gestor_tareas_env/bin/activate
```

- En Windows:

```bash
gestor_tareas_env\Scripts\activate
```

1. **Instalar Django**:

Con el entorno virtual activado, instala Django:

```bash
pip install django
```

2. **Crear el proyecto de Django**:

Ahora vamos a crear el proyecto. En la terminal, ejecuta:

```bash
django-admin startproject gestor_tareas
cd gestor_tareas
```

### Paso 2: Configurar PostgreSQL

1. **Instalar psycopg2**:

Django necesita `psycopg2` para conectarse a PostgreSQL, así que instálalo con:

```bash
pip install psycopg2-binary
```

2. **Modificar el archivo `settings.py`**:

Abre el archivo `settings.py` y busca la configuración de `DATABASES`. Reemplázala con la siguiente para conectarte a PostgreSQL:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'gestor_tareas_db',
        'USER': 'gestor_user',
        'PASSWORD': 'tu_contraseña_segura',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

3. **Crear la base de datos en PostgreSQL**:

Abre una terminal y ejecuta el siguiente comando para ingresar al shell de PostgreSQL:

```bash
sudo -u postgres psql
```

Dentro del shell de PostgreSQL, crea la base de datos y el usuario con los siguientes comandos:

```sql
CREATE DATABASE gestor_tareas_db;
CREATE USER gestor_user WITH PASSWORD 'tu_contraseña_segura';
ALTER ROLE gestor_user SET client_encoding TO 'utf8';
ALTER ROLE gestor_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE gestor_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE gestor_tareas_db TO gestor_user;
```

Luego, escribe `\q` para salir del shell.

### Paso 3: Aplicar migraciones iniciales en Django

1. **Aplicar las migraciones iniciales**:

Django necesita crear sus tablas predeterminadas para la autenticación y otras funcionalidades básicas. Ejecuta:

```bash
python manage.py migrate
```

2. **Iniciar el servidor de desarrollo**:

Asegúrate de que todo está funcionando bien. Inicia el servidor:

```bash
python manage.py runserver
```

Ve a tu navegador y accede a `http://127.0.0.1:8000`. Si ves la página de bienvenida de Django, ¡todo está funcionando correctamente!

### Paso 4: Configuración de autenticación de usuarios

#### 4.1 Configurar URLs y vistas para la autenticación

Django ya incluye un sistema de autenticación listo para usar. Usaremos las vistas predeterminadas para manejar el registro, inicio de sesión y cierre de sesión.

1. **Crear una nueva aplicación para gestionar usuarios**:

Primero, vamos a crear una aplicación para manejar todo lo relacionado con usuarios. En tu terminal, ejecuta:

```bash
python manage.py startapp usuarios
```

2. **Añadir la aplicación al proyecto**:

Abre el archivo `settings.py` y añade la nueva aplicación `usuarios` en la lista `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    'usuarios',
    'django.contrib.auth',
    'django.contrib.messages',
]
```

3. **Configurar las URLs de autenticación**:

En el archivo `urls.py` del proyecto principal (`gestor_tareas/urls.py`), añade las rutas para manejar la autenticación:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Añadimos las URLs de autenticación
    path('', include('usuarios.urls')),  # Nuestra app de usuarios
]
```

Las URLs de autenticación que añade Django incluyen:

- `/accounts/login/`: Página de inicio de sesión.
- `/accounts/logout/`: Página de cierre de sesión.
- `/accounts/password_change/`: Cambio de contraseña.

4. **Crear URLs para la app de usuarios**:

Crea un archivo `urls.py` dentro de la carpeta `usuarios/` y añade las siguientes rutas:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.Registro.as_view(), name='registro'),
]
```

#### 4.2 Crear la vista para el registro de usuarios

1. **Crear la vista basada en clases para el registro**:

Dentro del archivo `views.py` de la aplicación `usuarios`, vamos a crear una vista para registrar nuevos usuarios usando el formulario predeterminado de Django (`UserCreationForm`):

```python
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm

class Registro(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')  # Redirige al login después del registro
    template_name = 'registration/registro.html'
```

2. **Crear la plantilla para el registro**:

Crea un directorio llamado `templates` dentro de la carpeta `usuarios` y dentro de él un subdirectorio `registration`. Luego, dentro de este directorio, crea el archivo `registro.html` con el siguiente contenido:

```html
{% extends 'base_generic.html' %} {% block content %}
<div class="container mt-4">
  <h2>Registro de Usuario</h2>
  <form method="post">
    {% csrf_token %} {{ form.as_p }}
    <button type="submit" class="btn btn-primary">Registrarse</button>
  </form>
</div>
{% endblock %}
```

No olvides crear una plantilla base (`base_generic.html`) si aún no la tienes, que será la estructura principal de tu sitio.

#### 4.3 Probar la autenticación

1. **Migrar las tablas necesarias**:

Asegúrate de que se migren las tablas necesarias para la autenticación:

```bash
python manage.py migrate
```

2. **Crear un superusuario**:

Si deseas acceder al panel de administración de Django, puedes crear un superusuario:

```bash
python manage.py createsuperuser
```

3. **Probar el registro e inicio de sesión**:

Ahora puedes iniciar el servidor y acceder a `http://127.0.0.1:8000/accounts/login/` para probar el inicio de sesión y a `http://127.0.0.1:8000/accounts/logout/` para el cierre de sesión. El registro estará disponible en `http://127.0.0.1:8000/registro/`.
