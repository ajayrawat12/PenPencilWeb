"""
Django settings for penPencil project.

Generated by 'django-admin startproject' using Django 1.8.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(9z32duv=yk&4wl7qikq5u_m4nd6&@2b29$4o1#l%^^c9toy8a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social.apps.django_app.default',
    'apps.student',
    'apps.tutor',
    'apps.website',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'penPencil.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [

                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.i18n',  #from here on below added for oauth
                'django.core.context_processors.media',
                'django.core.context_processors.static',
                'django.core.context_processors.tz',
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',

            ],
        },
    },
]

# below added for Oauth

AUTHENTICATION_BACKENDS = (
   'social.backends.facebook.FacebookOAuth2',
   'social.backends.google.GoogleOAuth2',
   'social.backends.twitter.TwitterOAuth',
   'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_FACEBOOK_KEY = '143498379411581'
SOCIAL_AUTH_FACEBOOK_SECRET = '08e4aaea6f98691b553b85c01b7de605'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '764865092890-kiuaipd46j60akbrskdaghp3hj38r4dc.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'VwUCzUU4w2qsEXMu9GfGZNRZ'


SOCIAL_AUTH_TWITTER_KEY = 'YJMJ3An3o1n2VRMYcyTCaW43r'
SOCIAL_AUTH_TWITTER_SECRET = 'Om639lhqbp6eAjRoP6RhGSuzVUzeNcptGalOEj8kwjzbpWuyWl'



LOGIN_REDIRECT_URL = '/'

WSGI_APPLICATION = 'penPencil.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pen2pencil',
        'USER': 'postgres',
        'PASSWORD': 'database',
        'HOST': 'localhost',
        'PORT': '',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

STATIC_ROOT = BASE_DIR + '/static_root/'

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR + '/media/'

