  
import os

import dj_database_url

from .base import *

DEBUG = os.environ.get('DEBUG', False)

SECRET_KEY = os.environ['SECRET_KEY']


DATABASES = {
    'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
}


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'