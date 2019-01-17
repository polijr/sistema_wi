# -*- coding: utf-8 -*-

from .settings import *

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sistema_wi',
        'USER': 'sistema_wi',
        'PASSWORD': 'NSWFpj17',
        'HOST': '',
        'PORT': '',
    }
}

# Static files
STATICFILES_DIRS = (
    '/home/polijr/webapps/sistema_wi/si_sistema_wi/static/',
)

STATIC_ROOT = '/home/polijr/webapps/sistema_wi_static/'
# MEDIA_URL = '/media/'
# MEDIA_ROOT = '/home/polijr/webapps/flexmedia_media/'
