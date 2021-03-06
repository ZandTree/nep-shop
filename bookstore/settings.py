
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'az2%2a#1&%-gih^543upq-^)x2^#f#-pyq9eu)vq&l#-!^2%j='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*', '106f5bff.ngrok.io']
# ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.sessions',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    #third party modules
    'mptt',
    'bootstrap4',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'paypal.standard.ipn',
    'django_cleanup.apps.CleanupConfig',
    # custom apps
    'prods',
    'search',
    'tags',
    'orders',
    'profiles',
    'payments',
    'stripe'
]
WKHTMLTOPDF_CMD = 'C:/Users/tanja/Desktop/newDjango/venv/Lib/site-packages'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'bookstore.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates',],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                # my own function = in dir shop dir context_processors func list_categories
                'prods.context_processors.count_items_cart',
                'prods.context_processors.list_categories',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

WSGI_APPLICATION = 'bookstore.wsgi.application'

SITE_ID = 1
#paypal settings
PAYPAL_RECEIVER_EMAIL = 'verkoper@mail.com'   #os.environ.get("MY_EMAIL")
PAYPAL_TEST = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = None #"optional"
ACCOUNT_USERNAME_REQUIRED = False
LOGIN_URL= '/account/login'
LOGIN_URL_REDIRECT = "/"
ACCOUNT_EMAIL_SUBJECT_PREFIX = "My subject: "
# auto loggin in after confirmation(otherwise will be redirected to log-in)
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True

ACCOUNT_ADAPTER = 'adapter.AccountAdapter'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get("MY_EMAIL")
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR,'static'),]
#STATIC_ROOT = os.path.join(BASE_DIR,'static/')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')


STRIPE_PUBLISHABLE_KEY = 'pk_test_mSDotOmmYb8ZFsGhuKMpQ6pP00RndNmKhE'
SRTIPE_SECRET_KEY = os.environ.get('STRIPE_TEST_SECRET_KEY')
IDEAL_API = os.environ.get('IDEALWORD')
#print(IDEAL_API)

#
# try:
#     from .local_settings import *
# except ImportError:
#     from .prod_settings import *


INTERNAL_IPS = ['127.0.0.1']  #,'::1','0.0.0.0']
