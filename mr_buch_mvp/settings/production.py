from django.conf import settings
import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG
DATABASES = settings.DATABASES

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] =  dj_database_url.config()



# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['www.mrbuch.com','mrbuch.com','*.mrbuch.com']

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

STATIC_URL = '/static/'

# Static root directory address
STATIC_ROOT = 'staticfiles'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR,"static_in_pro","our_static"),
    #'/var/www/static_in_pro/',
)
# for using oscar css
USE_LESS = True
COMPRESS_ENABLED = False
# Whitenoise settings for collectstatic in heroku
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'