import os
import subprocess

# --- 1. Crear app dashboard y registrarla ---
subprocess.run(['python', 'manage.py', 'startapp', 'dashboard'], cwd=r'C:\Users\Administrator\Desktop\django_backend', check=False)

settings_path = r'C:\Users\Administrator\Desktop\django_backend\backend_data_server\settings.py'
with open(settings_path, 'r', encoding='utf-8') as f:
    settings_content = f.read()
if '"dashboard",' not in settings_content:
    settings_content = settings_content.replace('"homepage",', '"homepage",\n    "dashboard",')
if 'API_URL' not in settings_content:
    settings_content += "\nAPI_URL = 'https://jsonplaceholder.typicode.com/posts'\n"
with open(settings_path, 'w', encoding='utf-8') as f:
    f.write(settings_content)

urls_path = r'C:\Users\Administrator\Desktop\django_backend\backend_data_server\urls.py'
with open(urls_path, 'r', encoding='utf-8') as f:
    urls_content = f.read()
urls_content = urls_content.replace("path('', include('homepage.urls'))", "path('', include('dashboard.urls'))")
with open(urls_path, 'w', encoding='utf-8') as f:
    f.write(urls_content)

# --- 2. Crear urls.py y views.py de dashboard ---
dashboard_urls = r'C:\Users\Administrator\Desktop\django_backend\dashboard\urls.py'
with open(dashboard_urls, 'w', encoding='utf-8') as f:
    f.write('''from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
]''')

dashboard_views = r'C:\Users\Administrator\Desktop\django_backend\dashboard\views.py'
with open(dashboard_views, 'w', encoding='utf-8') as f:
    f.write('''from django.shortcuts import render
import requests
from django.conf import settings

def index(request):
    try:
        response = requests.get(settings.API_URL)
        posts = response.json()
        total_responses = len(posts)
    except Exception:
        total_responses = 0

    data = {
        "title": "Landing Page Dashboard",
        "total_responses": total_responses,
    }
    return render(request, "dashboard/index.html", data)''')

# --- 3. Crear templates de dashboard ---
os.makedirs(r'C:\Users\Administrator\Desktop\django_backend\templates\dashboard\partials', exist_ok=True)
os.makedirs(r'C:\Users\Administrator\Desktop\django_backend\templates\dashboard\content', exist_ok=True)

base_html = r'C:\Users\Administrator\Desktop\django_backend\templates\dashboard\base.html'
with open(base_html, 'w', encoding='utf-8') as f:
    f.write('''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Base Dashboard</title>
</head>
<body>
    {% block content %}
    <!-- START - Block content -->
    <div class="flex items-center justify-center h-screen bg-gray-100 w-full">
        <div class="p-6 bg-white shadow-md rounded">
            Block content
        </div>
    </div>
    <!-- END - Block content -->
    {% endblock %}
</body>
</html>''')

index_html = r'C:\Users\Administrator\Desktop\django_backend\templates\dashboard\index.html'
with open(index_html, 'w', encoding='utf-8') as f:
    f.write('''{% extends "dashboard/base.html" %}
{% block content %}
    <!-- START - Block content -->
    <div class="flex flex-col flex-1 justify-center w-full">
        {% include "./partials/header.html" %}
        {% include "./content/data.html" %}
    </div>
    <!-- END - Block content -->
{% endblock %}''')

header_html = r'C:\Users\Administrator\Desktop\django_backend\templates\dashboard\partials\header.html'
with open(header_html, 'w', encoding='utf-8') as f:
    f.write('''<h1 class="text-center text-6xl font-bold">Dashboard App</h1>''')

data_html = r'C:\Users\Administrator\Desktop\django_backend\templates\dashboard\content\data.html'
with open(data_html, 'w', encoding='utf-8') as f:
    f.write('''<h2 class="my-6 text-2xl font-semibold text-gray-700 dark:text-gray-200">
    <!-- START - titulo secundario -->
    {{ title }}
    <!-- END - titulo secundario -->
</h2>

<div>
    <p class="mb-2 text-sm font-medium text-gray-600 dark:text-gray-400">
        Número total de respuestas
    </p>
    <p class="text-lg font-semibold text-gray-700 dark:text-gray-200">
        <!-- START - valor del indicador 1 -->
        {{ total_responses }}
        <!-- END - valor del indicador 1 -->
    </p>
</div>''')

print("All setup complete!")
