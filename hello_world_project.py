import os
from django.conf import settings
from django.urls import path
from django.core.management import execute_from_command_line
from django.http import HttpResponse

# Minimal Django settings
settings.configure(
    DEBUG=True,
    SECRET_KEY='django-insecure-secret-key-for-local-development-only',
    ROOT_URLCONF=__name__,
    TEMPLATES=[{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
    }],
    INSTALLED_APPS=[
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ],
)

# Simple view
def index_view(request):
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Django DevOps App</title>
        <style>
            body { font-family: Arial; background: #f4f4f9; text-align: center; padding: 50px; }
            .container { max-width: 600px; margin: 0 auto; background: #fff; padding: 20px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }
            h1 { color: #007bff; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Hello, World!</h1>
            <p>Your simple Django web application is running.</p>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html_content)

# URL patterns
urlpatterns = [path('', index_view, name='index')]

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hello_world_project")
    execute_from_command_line()

