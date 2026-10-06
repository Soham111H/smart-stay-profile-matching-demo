from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# Safe public-repository defaults for local college/demo use.
# For real deployment, set SMART_STAY_SECRET_KEY in the environment.
SECRET_KEY = os.getenv(
    'SMART_STAY_SECRET_KEY',
    'django-insecure-smart-stay-local-demo-key'
)

DEBUG = os.getenv('SMART_STAY_DEBUG', 'True').lower() in ('1', 'true', 'yes', 'on')

_allowed_hosts = os.getenv('SMART_STAY_ALLOWED_HOSTS', '127.0.0.1,localhost')
ALLOWED_HOSTS = [host.strip() for host in _allowed_hosts.split(',') if host.strip()]

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'matching',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'smart_stay_demo.urls'

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [BASE_DIR / 'templates'],
    'APP_DIRS': True,
    'OPTIONS': {'context_processors': [
        'django.template.context_processors.debug',
        'django.template.context_processors.request',
    ]},
}]

WSGI_APPLICATION = 'smart_stay_demo.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # These defaults preserve the existing XAMPP MariaDB 10.4 setup.
        'NAME': os.getenv('SMART_STAY_DB_NAME', 'smart_stay'),
        'USER': os.getenv('SMART_STAY_DB_USER', 'root'),
        'PASSWORD': os.getenv('SMART_STAY_DB_PASSWORD', ''),
        'HOST': os.getenv('SMART_STAY_DB_HOST', '127.0.0.1'),
        'PORT': os.getenv('SMART_STAY_DB_PORT', '3306'),
        'OPTIONS': {'charset': 'utf8mb4'},
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
