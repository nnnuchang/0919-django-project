"""
WSGI config for django_test project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import sys

sys.path.append('/home/nnnuchang/django_prj/django_test/')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_test.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
