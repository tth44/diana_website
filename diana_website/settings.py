"""
Django settings for diana_website project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.conf import global_settings
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


ALLOWED_HOSTS = ['*']
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES ={}
DATABASES['default']= dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')



# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+gan&czjo@c3cfsg*k#zid)14rww(2*72&87$*akrq86*y7#x@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False




# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
    'main_app',
    'portfolio',
    'cv',
    'collectfast',
    
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'diana_website.urls'

WSGI_APPLICATION = 'diana_website.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

#----------------------------------------------------------------- DATABASES = {
    #-------------------------------------------------------------- 'default': {
        #------------------------------- 'ENGINE': 'django.db.backends.sqlite3',
        #------------------------- 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    #------------------------------------------------------------------------- }
#----------------------------------------------------------------------------- }

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = False

USE_L10N = True

USE_TZ = True



#context processor
TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
                              'main_app.context_processors.cats',
                              'main_app.context_processors.contactCat',
                              )
                              


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
#STATIC_ROOT = os.path.join(BASE_DIR,'static','www') 

#reportory outside of any application (at top-level)
STATICFILES_DIRS = (("www",os.path.join(BASE_DIR, "static")),
)                   


#media file

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

#S3 config
USE_S3 = True
if USE_S3:
    AWS_PRELOAD_METADATA = True
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    
    S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
    DEFAULT_FILE_STORAGE = 'diana_website.s3utils.MediaRootS3BotoStorage'
    STATICFILES_STORAGE = 'diana_website.s3utils.StaticRootS3BotoStorage'
    MEDIA_URL = S3_URL + 'media/'
    STATIC_URL = S3_URL + 'static/'


#templates
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]


#TinyMCE

#email
EMAIL_HOST = os.environ.get('MAILGUN_SMTP_SERVER')#'smtp.mailgun.org'
EMAIL_PORT = os.environ.get('MAILGUN_SMTP_PORT')#'587'
EMAIL_HOST_USER = os.environ.get('MAILGUN_SMTP_LOGIN')#'postmaster@app28365878.mailgun.org'
EMAIL_HOST_PASSWORD = os.environ.get('MAILGUN_SMTP_PASSWORD')#'57iimb4jyfj1'#

EMAIL_USE_TLS =False


