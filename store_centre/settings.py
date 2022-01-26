"""
Django settings for store_centre project.

Generated by 'django-admin startproject' using Django 2.2.24.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from pathlib import Path
from decouple import config,Csv
import cloudinary
import cloudinary.uploader
import cloudinary.api
import django_heroku

MODE=config("MODE", default="dev")

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
DEBUG = os.environ.get('DEBUG', True)


ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'store',
    'transport',
    'units',
    'analytics',
    'bootstrap4',
    'cloudinary',
    'crispy_forms',
    'rest_framework.authtoken',
    'widget_tweaks',
    'mathfilters',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'social_django',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'store_centre.urls'

AUTH_USER_MODEL = 'store.User'

AUTH_PROFILE_MODULE = 'accounts.UserProfile'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [Path(BASE_DIR,"templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'store_centre.wsgi.application'

#configure cloudinary
cloudinary.config(
    cloud_name = config('CD_NAME'),
    api_key= config('CD_API'),
    api_secret=config('CD_SECRET'),
)

#GOOGLE API
GOOGLE_API_KEY= config('GOOGLE_API_KEY')
BASE_COUNTRY='KE'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD':config('DB_PASSWORD'),
        
    }
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    )
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/


STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),

]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
CRISPY_TEMPLATE_PACK = 'bootstrap4'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
django_heroku.settings(locals())

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = config('S_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = config('S_SECRET')

LOGIN_REDIRECT_URL = 'index'

AUTHENTICATION_BACKENDS = [
  
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'social_core.backends.google.GoogleOAuth2',

   
]
#jazzmin settings
JAZZMIN_SETTINGS = {
      # title of the window (Will default to current_admin_site.site_title if absent or None)
   "site_title": "Store-admin",
# Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "store",
     # Welcome text on the login screen
    "welcome_sign": "Welcome to the store-centre",
    # Copyright on the footer
    "copyright": "store_centre ltd @2022",
    # The model admin to search from the search bar, search bar omitted if excluded
    "search_model": "auth.User",
     "topmenu_links": [

        # Url that gets reversed (Permissions can be added)
        {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},

        # external url that opens in a new window (Permissions can be added)

        {"name": "Staff ", "url": "/staff_register", "new_window": True},

        {"name": "View Website", "url": "/", "new_window": True},


        # model admin to link to (Permissions checked against model)
        {"model": "auth.User"},

        # App with dropdown menu to all its models pages (Permissions checked against models)
        {"app": "store"},
    ],
     "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
    "custom_links": {
    "books": [{
        
             
    }]
},
}
