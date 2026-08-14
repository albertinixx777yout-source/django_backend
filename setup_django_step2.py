import os

# 1. Update backend_data_server/urls.py to use root path '' instead of 'homepage/'
urls_path = r'C:\Users\Administrator\Desktop\django_backend\backend_data_server\urls.py'
with open(urls_path, 'r', encoding='utf-8') as f:
    urls_content = f.read()
urls_content = urls_content.replace("'homepage/'", "''")
with open(urls_path, 'w', encoding='utf-8') as f:
    f.write(urls_content)

# 2. Update settings.py for templates and static files
settings_path = r'C:\Users\Administrator\Desktop\django_backend\backend_data_server\settings.py'
with open(settings_path, 'r', encoding='utf-8') as f:
    settings_content = f.read()

if 'import os' not in settings_content:
    settings_content = 'import os\n' + settings_content

settings_content = settings_content.replace(
    "'DIRS': [],",
    "'DIRS': [os.path.join(BASE_DIR, 'templates')],"
)

if 'STATICFILES_DIRS' not in settings_content:
    settings_content += '\nSTATICFILES_DIRS = [\n    os.path.join(BASE_DIR, \'static\'),\n]\n'

with open(settings_path, 'w', encoding='utf-8') as f:
    f.write(settings_content)

# 3. Create directories
os.makedirs(r'C:\Users\Administrator\Desktop\django_backend\templates\homepage', exist_ok=True)
os.makedirs(r'C:\Users\Administrator\Desktop\django_backend\static\img', exist_ok=True)

# 4. Create index.html
html_content = '''{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Homepage</title>
</head>
<body>
    <h1>¡Bienvenido a la aplicación Django!</h1>
    <img aria-hidden="true" class="object-cover w-full h-full dark:hidden" src="{% static 'img/team.jpg' %}" alt="Office" />
    <img aria-hidden="true" class="hidden object-cover w-full h-full dark:block" src="{% static 'img/team.jpg' %}" alt="Office" />
</body>
</html>'''
with open(r'C:\Users\Administrator\Desktop\django_backend\templates\homepage\index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

# 5. Update views.py
views_path = r'C:\Users\Administrator\Desktop\django_backend\homepage\views.py'
with open(views_path, 'w', encoding='utf-8') as f:
    f.write('''from django.shortcuts import render

def index(request):
    return render(request, 'homepage/index.html')''')

print('Django templates and static config updated successfully!')
