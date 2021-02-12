from .base import *

DEBUG = False

POSTGRESQL_HOST = os.environ.get('DJANGO_POSTGRESQL_HOST') or 'localhost'
POSTGRESQL_PORT = os.environ.get('DJANGO_POSTGRESQL_PORT') or 5432
POSTGRESQL_DB = os.environ.get('DJANGO_POSTGRESQL_DB') or 'cassaby'
POSTGRESQL_USER = os.environ.get('DJANGO_POSTGRESQL_USER') or 'postgres'
POSTGRESQL_PASSWORD = os.environ.get('DJANGO_POSTGRESQL_PASSWORD')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': POSTGRESQL_DB,
        'USER': POSTGRESQL_USER,
        'PASSWORD': POSTGRESQL_PASSWORD,
        'HOST': POSTGRESQL_HOST,
        'PORT': POSTGRESQL_PORT,
    }
}