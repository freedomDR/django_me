"""
WSGI config for me project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os, sys

sys.path.append("~/.virtualenvs/djangotest/lib/python3.6/site-packages")
sys.path.append("/mnt/sdb/python3_code/django_projects/me")

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "me.settings")

application = get_wsgi_application()
