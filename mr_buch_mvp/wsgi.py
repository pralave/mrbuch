"""
WSGI config for mr_buch_alpha project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mr_buch_alpha.settings")


from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from whitenoise.django import DjangoWhiteNoise
application = DjangoWhiteNoise(application)

try:
    from dj_static import Cling
    application = Cling(get_wsgi_application())

except:
    pass
