"""
Django settings for organilab project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

from django.urls import reverse_lazy
import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY',
                       '8sko4lo%ca!0e^-i%7@6hnzxmc7l0^m040n%jy99z_e8cvmta)')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', 'True')
FULL_APPS = True

if os.getenv('ALLOWED_HOSTS', ''):
    ALLOWED_HOSTS = [c for c in os.getenv('ALLOWED_HOSTS', '').split(',')]
else:
    ALLOWED_HOSTS = []

# Application definition

SITE_ID = 1
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'presentation',
    'django_ajax',
    'laboratory',
    'authentication',
    'academic',
    "bootstrapform",
    "djreservation",
    "celery",
    'ajax_select',
    'crispy_forms',
    'cruds_adminlte',
    'location_field.apps.DefaultConfig',
    'mptt',
    'constance',
    'constance.backends.database',
    'rest_framework',
    'rest_framework.authtoken',
    'snowpenguin.django.recaptcha2',
    'msds',
    'sga',
    'monitarize',
    'async_notifications',
    'ckeditor',
    'fontawesome',
    'django_comments',
    'tagging',
    'zinnia',
    'zinnia_ckeditor',
    'ckeditor_uploader',
    #    'debug_toolbar',
    'mapwidgets',
    'guardian',
    'risk_management'
]
if FULL_APPS:
    INSTALLED_APPS += [
        'api',
        'demoQA'
    ]

    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.authentication.SessionAuthentication',
        ),
        'DEFAULT_PERMISSION_CLASSES': (
            'rest_framework.permissions.IsAuthenticated',
        ),
        'DEFAULT_PARSER_CLASSES': (
            'rest_framework.parsers.JSONParser',
        ),
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
        'PAGE_SIZE': 50,
        'TEST_REQUEST_DEFAULT_FORMAT': 'json'
    }

RECAPTCHA_PRIVATE_KEY = os.getenv(
    'RECAPTCHA_PRIVATE_KEY', '6LdxAmAUAAAAAMxAz4s9em2TgxXUb7MGCZMGRE8l')
RECAPTCHA_PUBLIC_KEY = os.getenv(
    'RECAPTCHA_PUBLIC_KEY', '6LdxAmAUAAAAAH2R-6v5EZUALYcqs8AJyrlkqo7_')

CRISPY_TEMPLATE_PACK = 'bootstrap3'
IMAGE_CROPPING_JQUERY_URL = None
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #  'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'djreservation.middleware.ReservationMiddleware'
]

ROOT_URLCONF = 'organilab.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.contrib.messages.context_processors.messages',
                'constance.context_processors.config',
            ],
        },
    },
]

WSGI_APPLICATION = 'organilab.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DBNAME', 'organilab'),
        'USER': os.getenv('DBUSER', 'organilab_user'),
        'PASSWORD': os.getenv('DBPASSWORD', '0rg4n1l4b'),
        'HOST': os.getenv('DBHOST', '127.0.0.1'),
        'PORT': os.getenv('DBPORT', '5432'),
    }
}

# TEST - DJANGO:GUARDIAN

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  # default
    'guardian.backends.ObjectPermissionBackend',
)

# END TEST

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Costa_Rica'

USE_I18N = True

USE_L10N = False

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = os.getenv('STATIC_URL', '/static/')
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATIC_CRAWL = os.path.join(BASE_DIR, 'static/')

MEDIA_URL = os.getenv('MEDIA_URL', '/media/')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
# Authentication settings
LOGIN_REDIRECT_URL = reverse_lazy('index')
LOGOUT_REDIRECT_URL = reverse_lazy('index')

# Email development settings
DEFAULT_FROM_EMAIL = os.getenv(
    'DEFAULT_FROM_EMAIL', "site@organilab.org")
#EMAIL_HOST = "localhost"
#EMAIL_PORT = "1025"

#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS')
EMAIL_HOST = os.getenv('EMAIL_HOST', 'localhost')  # mail service smtp
EMAIL_PORT = os.getenv('EMAIL_PORT', '1025')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', None)  # a real email
# the password of the real email
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', None)
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Celery settings
BROKER_URL = os.getenv(
    'BROKER_URL', 'amqp://guest:guest@localhost:5672/organilabvhost')
CELERY_TIMEZONE = TIME_ZONE
CELERY_MODULE = "organilab.celery"
CELERY_RESULT_BACKEND = os.getenv(
    'CELERY_RESULT_BACKEND', 'amqp://guest:guest@localhost:5672/organilabvhost')
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

GOOGLE_MAPS_API_KEY = os.getenv(
    'GOOGLE_MAPS_API_KEY', 'AIzaSyAcsEpjMLRGe752wNzZ6fE-ovBbyLw7gFU')

LOCATION_FIELD = {
    'map.provider': 'google',
    'map.zoom': 15,
    'search.provider': 'google',
    'provider.google.api': '//maps.google.com/maps/api/js?sensor=false',
    'provider.google.api_key': GOOGLE_MAPS_API_KEY,
    'provider.google.map.type': 'ROADMAP',
}

# TEST

MAP_WIDGETS = {
    "GooglePointFieldWidget": (
        ("zoom", 8),
        ("mapCenterLocationName", "Costa_Rica"),
    ),
    "GOOGLE_MAP_API_KEY": GOOGLE_MAPS_API_KEY
}


# END TEST

CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'
CONSTANCE_CONFIG = {
    'GROUP_ADMIN_PK': (1, 'User perms Group with complete access on laboratory, '
                       'User Administrator of labotatory', int),
    'GROUP_LABORATORIST_PK': (2, 'User perms Group with access controlling to laboratory '
                       'User Laboratorist/Professor of labotatory', int),
    'GROUP_STUDENT_PK': (3, 'User perms Group with low access to laboratory '
                       'User Student of labotatory', int),
    'ADSENSE_ACTIVE': (True, 'Active the Ads', bool),
    'ADSENSE_PUB_TOKEN': ('ca-pub-1539451676311396', 'Google adsense public key'
                          'for monitarize the website', str),
}

CONSTANCE_CONFIG_FIELDSETS = {
    'Default Groups': ('GROUP_ADMIN_PK', 'GROUP_LABORATORIST_PK',
                       'GROUP_STUDENT_PK', 'ADSENSE_ACTIVE',
                       'ADSENSE_PUB_TOKEN'),
}

ACCOUNT_ACTIVATION_DAYS = 2
CKEDITOR_UPLOAD_PATH = 'editoruploads/'
DATASETS_SUPPORT_LANGUAGES = {
    'es': '//cdn.datatables.net/plug-ins/1.10.19/i18n/Spanish.json'
}

ASYNC_NOTIFICATION_TEXT_AREA_WIDGET = 'ckeditor.widgets.CKEditorWidget'

from celery.schedules import crontab

CELERY_MODULE='organilab.celery'

CELERYBEAT_SCHEDULE = {
    # execute 12:30 pm
    'send_daily_emails': {
        'task': 'async_notifications.tasks.send_daily',
        'schedule': crontab(minute=2, hour=0),
    },
    'check_product_limits': {
        'task': 'laboratory.tasks.notify_about_product_limit_reach',
        'schedule': crontab(minute=10, hour=0),
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
        'organilab': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
    },
}

INTERNAL_IPS = ('127.0.0.1',)
CKEDITOR_IMAGE_BACKEND = 'pillow'
