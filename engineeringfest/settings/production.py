  
import os

import dj_database_url

from settings.base import *

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['essaypro360.herokuapp.com', '127.0.0.1']

DATABASES = {
    'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'