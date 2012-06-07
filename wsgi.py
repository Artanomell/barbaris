"""
WSGI config for barbaris project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.

"""
import os, sys

HOME = '/home/djbaldey'
PYTHON = 'python2.7'
ENV = os.path.join(HOME, 'env-django1.4')
PACKAGES = os.path.join(ENV, 'lib', PYTHON, 'site-packages')

sys.path.insert(0, PACKAGES)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "barbaris.settings")

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)
