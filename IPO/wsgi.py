"""
WSGI config for IPO project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""
import os
from django.core.wsgi import get_wsgi_application

# 👇 Auto-migrate workaround
import django
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IPO.settings')
django.setup()
try:
    call_command('migrate', interactive=False)
except Exception as e:
    print("Migration error:", e)

application = get_wsgi_application()
