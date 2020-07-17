from settings.base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'engineeringfest',
        'USER': 'engineeringfestadmin',
        'PASSWORD': '@IEEEku2020',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}