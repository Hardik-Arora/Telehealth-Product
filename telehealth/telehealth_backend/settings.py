"""
Django settings for telehealth_backend project.

Generated by 'django-admin startproject' using Django 3.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path
import os
# from .Appointment.views import AppointmentView
from google.oauth2 import service_account

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-n2m(3*!&n#yz#lh%#irqo5%0^%0np!mypyfbcv%--i3tc4%ofj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    # 'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'accounts.apps.AccountsConfig',
    'doctor.apps.DoctorConfig',
    'Patient.apps.PatientConfig',
    'video_chat.apps.VideoChatConfig',
    'rest_framework_swagger',
    'django_crontab',
    'cronJob.apps.CronJobConfig',
    'Appointment.apps.AppointmentConfig',
    'sslserver'
]

# SMS_BACKEND = 'sms.backends.twilio.SmsBackend'
# TWILIO_ACCOUNT_SID = 'ACe617f1ddd362000dfed3fc2eb3aee8f8'
# TWILIO_AUTH_TOKEN = '98128f89f4dc3b16c19aeb635956d9da'

# SMS_BACKEND = 'sms.backends.messagebird.SmsBackend'
# MESSAGEBIRD_ACCESS_KEY = 'sVlKc5S8ymCxTMcg9sJPOGZxf'

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'telehealth_backend.urls'

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
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'telehealth_backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default':{
#       'ENGINE':'django.db.backends.postgresql_psycopg2',
#       'NAME':'test_db',
#       'USER':'postgres',
#       'PASSWORD':'123',
#       'HOST':'localhost',
#       'PORT':'5432',
#    }
# }

# DATABASES = {
#     'default':{
#       'ENGINE':'django.db.backends.postgresql_psycopg2',
#       'NAME':'d5vqjm5jsc4lvf',
#       'USER':'klyvypwfwjspgp',
#       'PASSWORD':'b8f5114f0270474709371d693f8976bbc516326b3ce26deac50568620328ac9a',
#       'HOST':'ec2-34-193-113-223.compute-1.amazonaws.com',
#       'PORT':'5432',
#    }
# }

DATABASES = {
    'default':{
      'ENGINE':'django.db.backends.postgresql_psycopg2',
      'NAME':'postgres',
      'USER':'postgres',
      'PASSWORD':'G4fpDF8ei3gAq53D',
      'HOST':'35.200.133.211',
      'PORT':'5432',
      }
   }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field



EMAIL_USE_TLS = True
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = "caretelehealth@gmail.com"
EMAIL_HOST_PASSWORD="telehealth@123"

#CRON
# CRONJOBS = [
#     ('*/2 * * * *', 'telehealth.cron.my_cron_job')
# ]
# FAILED_RUNS_CRONJOB_EMAIL_PREFIX = "[Server check]:"


#**********************************************

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'accounts.User'

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
GS_BUCKET_NAME = 'priyam_in2021261_telehealth'
GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
    "telehealth_backend/service-account.json"
)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "telehealth.settings")
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"