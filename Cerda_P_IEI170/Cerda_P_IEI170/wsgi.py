import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Cerda_P_IEI170.settings')

application = get_wsgi_application()
