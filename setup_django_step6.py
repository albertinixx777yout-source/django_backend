import os

# 1. Update views.py with permission_required
views_path = r'C:\Users\Administrator\Desktop\django_backend\dashboard\views.py'
with open(views_path, 'r', encoding='utf-8') as f:
    views_content = f.read()

views_content = views_content.replace(
    'from django.contrib.auth.decorators import login_required',
    'from django.contrib.auth.decorators import login_required, permission_required'
)
views_content = views_content.replace(
    '@login_required\ndef index(request):',
    "@login_required\n@permission_required('dashboard.index_viewer', raise_exception=True)\ndef index(request):"
)
with open(views_path, 'w', encoding='utf-8') as f:
    f.write(views_content)

# 2. Update models.py with DashboardModel and permissions
models_path = r'C:\Users\Administrator\Desktop\django_backend\dashboard\models.py'
with open(models_path, 'w', encoding='utf-8') as f:
    f.write('''from django.db import models

class DashboardModel(models.Model):
    class Meta:
        permissions = [
            ("index_viewer", "Can show to index view (function-based)"),
        ]
''')

# 3. Update settings.py for MySQL
settings_path = r'C:\Users\Administrator\Desktop\django_backend\backend_data_server\settings.py'
with open(settings_path, 'r', encoding='utf-8') as f:
    settings_content = f.read()

if 'pymysql' not in settings_content:
    import_block = '''import os
import pymysql
pymysql.install_as_MySQLdb()
'''
    settings_content = settings_content.replace('import os\n', import_block)

    sqlite_db_config = """DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}"""
    
    mysql_db_config = """DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('MYSQLDATABASE', 'security'),
        'USER': os.environ.get('MYSQLUSER', 'root'),
        'PASSWORD': os.environ.get('MYSQLPASSWORD', 'root'),
        'HOST': os.environ.get('MYSQLHOST', 'localhost'),
        'PORT': os.environ.get('MYSQLPORT', '3306'),
    }
}"""
    settings_content = settings_content.replace(sqlite_db_config, mysql_db_config)
    
    with open(settings_path, 'w', encoding='utf-8') as f:
        f.write(settings_content)

print("Autorizacion models and views updated! MySQL settings prepared.")
