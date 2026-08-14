import os

# 1. Modificar settings.py
settings_path = r'C:\Users\Administrator\Desktop\django_backend\backend_data_server\settings.py'
with open(settings_path, 'r', encoding='utf-8') as f:
    settings_content = f.read()

# Replace ALLOWED_HOSTS
import re
settings_content = re.sub(r"ALLOWED_HOSTS = \[\]", 'ALLOWED_HOSTS = ["*"]', settings_content)

if 'CSRF_TRUSTED_ORIGINS' not in settings_content:
    settings_content += '''
CSRF_TRUSTED_ORIGINS = [
    "https://*.app.github.dev",
    "https://localhost:8000",
    "http://127.0.0.1:8000"
]
'''

if 'LOGIN_URL' not in settings_content:
    settings_content += '''
# Fallo: acceso sin autenticación
LOGIN_URL = '/login/'

# Éxito: luego de autenticación exitosa
LOGIN_REDIRECT_URL = '/'
'''

with open(settings_path, 'w', encoding='utf-8') as f:
    f.write(settings_content)

# 2. Modificar urls.py
urls_path = r'C:\Users\Administrator\Desktop\django_backend\backend_data_server\urls.py'
with open(urls_path, 'r', encoding='utf-8') as f:
    urls_content = f.read()

if 'auth_views' not in urls_content:
    urls_content = urls_content.replace(
        'from django.urls import path, include',
        'from django.urls import path, include\nfrom django.contrib.auth import views as auth_views'
    )
    urls_content = urls_content.replace(
        ']',
        "    path('login/', auth_views.LoginView.as_view(template_name='security/login.html'), name='login'),\n    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),\n]"
    )
    with open(urls_path, 'w', encoding='utf-8') as f:
        f.write(urls_content)

# 3. Modificar views.py (añadir login_required)
views_path = r'C:\Users\Administrator\Desktop\django_backend\dashboard\views.py'
with open(views_path, 'r', encoding='utf-8') as f:
    views_content = f.read()

if 'login_required' not in views_content:
    views_content = 'from django.contrib.auth.decorators import login_required\n' + views_content
    views_content = views_content.replace('def index(request):', '@login_required\ndef index(request):')
    with open(views_path, 'w', encoding='utf-8') as f:
        f.write(views_content)

# 4. Crear login.html
os.makedirs(r'C:\Users\Administrator\Desktop\django_backend\templates\security', exist_ok=True)
login_html_path = r'C:\Users\Administrator\Desktop\django_backend\templates\security\login.html'
with open(login_html_path, 'w', encoding='utf-8') as f:
    f.write('''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Iniciar Sesión</title>
</head>
<body>
    <h2>Iniciar Sesión</h2>
    <form method="post" action="{% url 'login' %}">
        {% csrf_token %}
        <div>
            <label for="username">Usuario:</label>
            <input type="text" id="username" name="username" required>
        </div>
        <div>
            <label for="password">Contraseña:</label>
            <input type="password" id="password" name="password" required>
        </div>
        <button type="submit">Login</button>
    </form>
</body>
</html>''')

# 5. Script para crear usuarios
create_users_script = r'C:\Users\Administrator\Desktop\django_backend\create_users.py'
with open(create_users_script, 'w', encoding='utf-8') as f:
    f.write('''import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_data_server.settings')
django.setup()

from django.contrib.auth.models import User

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
if not User.objects.filter(username='usuario01').exists():
    User.objects.create_user('usuario01', 'u1@example.com', 'usuario123')
if not User.objects.filter(username='usuario02').exists():
    User.objects.create_user('usuario02', 'u2@example.com', 'usuario123')
print("Usuarios creados con éxito.")
''')
