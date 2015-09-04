"""
Django settings for django_bulletin_demo project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

ADMINS = (
    ('Ben Stookey', 'ben@aashe.org'),
    ('Bob Erb', 'bob.erb@aashe.org'),
    ('Scott Johnson', 'scott@aashe.org'),
)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = str(os.environ.get('SECRET_KEY'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'registration',

    # AASHE Apps
    'bulletin',
    'bulletin.tools.plugins',
    'django_constant_contact',
    'python_constantcontact',
    'haystack',

    # required by bulletin
    'bootstrap3',
    'bootstrap_pagination',
    'datetimewidget',
    'django_bootstrap_breadcrumbs',
    'south',

    # required to configure on heroku
    'dj_static',
    'dj_database_url',
    'psycopg2',
    'gunicorn',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'django_bulletin_demo.urls'

WSGI_APPLICATION = 'django_bulletin_demo.wsgi.application'


import dj_database_url
DATABASES = {'default': dj_database_url.config()}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_URL = os.environ.get('STATIC_URL', '/static/')
STATIC_ROOT = os.environ.get('STATIC_ROOT',
                             os.path.join(BASE_DIR, STATIC_URL.strip('/')))
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'src/django-bulletin/bulletin/static/theme'),
                    os.path.join(BASE_DIR, 'src/django-bulletin/bulletin/static'),)

# Constant Contact secrets:
CONSTANT_CONTACT_API_KEY = str(os.environ.get('CONSTANT_CONTACT_API_KEY'))
CONSTANT_CONTACT_ACCESS_TOKEN = str(os.environ.get('CONSTANT_CONTACT_ACCESS_TOKEN'))
CONSTANT_CONTACT_FROM_EMAIL = str(os.environ.get('CONSTANT_CONTACT_FROM_EMAIL'))
CONSTANT_CONTACT_REPLY_TO_EMAIL = str(os.environ.get('CONSTANT_CONTACT_REPLY_TO_EMAIL'))
CONSTANT_CONTACT_USERNAME = str(os.environ.get('CONSTANT_CONTACT_USERNAME'))
CONSTANT_CONTACT_PASSWORD = str(os.environ.get('CONSTANT_CONTACT_PASSWORD'))

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(BASE_DIR, '..', 'bulletin_index')
    },
}

HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

# Bulletin Settings:
NUM_POSTS_ON_FRONT_PAGE = 50

BULLETIN_CONTENT_TYPE_PLUGINS = (
    'event',
    'job',
    'newresource',
    'opportunity',
    'story',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

LOGIN_REDIRECT_URL = '/'

# try to load local_settings.py if it exists
try:
   from local_settings import *
except Exception as e:
   pass
