
import os
import sys

path = os.path.expanduser('~/Project')
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'my_education.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()