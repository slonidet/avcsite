"""
Django settings for avcsite project.

Generated by 'django-admin startproject' using Django 1.9.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '85s(4mb_6_)uw8!j9rx_)39l)9)y-hbnjfv_f!(0di!o4ko5bf'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#ALLOWED_HOSTS = ['www.u54666.netangels.ru','u54666.netangels.ru']
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    
    'regionsmap',
    'homepage',
    'newsletter',
    'content',
    'events',
    'aboutpage',
    'mediacontent',
    'fes',
    'academy',
    
    
    
    'captcha',#https://github.com/praekelt/django-recaptcha
    'imagekit',#https://github.com/matthewwithanm/django-imagekit
    'ckeditor',#https://github.com/django-ckeditor/django-ckeditor/blob/master/README.rst
    'ckeditor_uploader',
    
    'content.templatetags.ext_filt', #custom filter for get ext file
    'newsletter.templatetags.text_filt',
    'mediacontent.templatetags.youtube_filt',
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'avcsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'avcsite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'u54666_avc',
        'USER': 'u54666',
        'PASSWORD': 'evhnbx9pgt',
        'HOST': 'localhost',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/


STATIC_URL = '/static/'

STATIC_ROOT = '/home/u54666/u54666.netangels.ru/www/static'



MEDIA_URL = '/media/'

MEDIA_ROOT = '/home/u54666/u54666.netangels.ru/www/media'

#ckeditor
CKEDITOR_UPLOAD_PATH = "uploads/"

#email settins

EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = "avchost@gmail.com"
EMAIL_HOST_PASSWORD = 'lhfueyjdf75'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


RECAPTCHA_PUBLIC_KEY = "6LcPXiMTAAAAAHcKoM9UgIfdMMEcXMJX96GSO0Bo"
RECAPTCHA_PRIVATE_KEY = "6LcPXiMTAAAAAA13EbnFT5qUySRtSXEDNJ_9tr1g"
NOCAPTCHA = True
RECAPTCHA_USE_SSL = True

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
    },
}
