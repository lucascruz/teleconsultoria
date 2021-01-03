from teleconsultoria.settings import *
import dj_database_url

DEBUG = False

ALLOWED_HOSTS = ['telessaude-ac.herokuapp.com',]

db_from_env = dj_database_url.config()

DATABASES['default'].update(db_from_env)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'teleconsultoria',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

