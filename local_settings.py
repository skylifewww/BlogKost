from settings import PROJECT_ROOT, SITE_ROOT
import os

DEBUG = True
TEMPLATE_DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'blogkost',
        'USER': 'skylife',
        'PASSWORD': 'skywww123',
        "HOST": "localhost",
        "PORT": "5432",
    }
}