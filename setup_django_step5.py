import os

# 1. Update header.html
header_path = r'C:\Users\Administrator\Desktop\django_backend\templates\dashboard\partials\header.html'
with open(header_path, 'r', encoding='utf-8') as f:
    header_content = f.read()

header_content = '''<div class="flex justify-between items-center w-full mb-6">
    <h1 class="text-center text-4xl font-bold">Dashboard App</h1>
    <ul class="flex items-center space-x-4">
        <!-- Profile menu -->
        <li class="relative">
            {% if user.is_authenticated %}
                <span class="mr-4 font-semibold text-gray-700">Bienvenido, {{ user.username }}</span>
            {% endif %}
            
            <!-- START - Block Logout -->
            <form method="post" action="{% url 'logout' %}" class="inline">
                {% csrf_token %}
                <button type="submit" class="bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded">
                    Cerrar Sesión
                </button>
            </form>
            <!-- END - Block Logout -->
        </li>
    </ul>
</div>
'''

with open(header_path, 'w', encoding='utf-8') as f:
    f.write(header_content)

# 2. Update login.html to handle errors
login_path = r'C:\Users\Administrator\Desktop\django_backend\templates\security\login.html'
with open(login_path, 'r', encoding='utf-8') as f:
    login_content = f.read()

if 'form.non_field_errors' not in login_content:
    error_block = '''
        <div class="w-full mb-4">
            {% if form.non_field_errors %}
                <div id="password_error_cl" class="flex items-center justify-center py-3 bg-red-100 border-l-4 border-red-500 text-red-700 dark:border-red-400 dark:text-red-500" role="alert">
                    Invalid username or password.
                </div>
            {% endif %}
        </div>
'''
    login_content = login_content.replace('<form method="post"', error_block + '        <form method="post"')
    with open(login_path, 'w', encoding='utf-8') as f:
        f.write(login_content)

# 3. Add db.sqlite3 to .gitignore
gitignore_path = r'C:\Users\Administrator\Desktop\django_backend\.gitignore'
if os.path.exists(gitignore_path):
    with open(gitignore_path, 'r', encoding='utf-8') as f:
        gitignore_content = f.read()
    if 'db.sqlite3' not in gitignore_content:
        with open(gitignore_path, 'a', encoding='utf-8') as f:
            f.write('\n# SQLite database\ndb.sqlite3\n')
else:
    with open(gitignore_path, 'w', encoding='utf-8') as f:
        f.write('\n# SQLite database\ndb.sqlite3\n')

print("Final templates and gitignore updated successfully!")
