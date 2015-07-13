"""
WSGI config for duafi project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os, sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "duafi.settings")
sys.path.append('/duafi/django/duafi')
sys.path.append('/duafi/django')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()



