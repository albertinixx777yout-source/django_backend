import re

settings_path = r'C:\Users\Administrator\Desktop\django_backend\backend_data_server\settings.py'
with open(settings_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Buscamos reemplazar el bloque de DATABASES actual
# Que incluye SQLite y la versión de MySQL comentada.

start_marker = "DATABASES = {"
end_marker = "# Password validation"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_db = '''DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('MYSQLDATABASE', 'security'),
        'USER': os.environ.get('MYSQLUSER', 'root'),
        'PASSWORD': os.environ.get('MYSQLPASSWORD', ''),
        'HOST': os.environ.get('MYSQLHOST', 'localhost'),
        'PORT': os.environ.get('MYSQLPORT', '3306'),
    }
}

'''
    content = content[:start_idx] + new_db + content[end_idx:]
    with open(settings_path, 'w', encoding='utf-8') as f:
        f.write(content)
