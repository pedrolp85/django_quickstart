from django_quickstart.settings.base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'django_quickstart_db',
        'USER': 'userdev',
        'PASSWORD':'passdev',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}