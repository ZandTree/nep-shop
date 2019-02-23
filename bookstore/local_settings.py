import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        # 'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'delicat',
        'USER':'postgres',
        'PASSWORD':os.environ.get('PASS_DB'),
        'HOST':'localhost',
        'PORT':'5432',
        # "TEST":{
        # 'NAME':'test_db',
        # }
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR,'static'),]
