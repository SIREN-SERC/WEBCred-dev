import dj_database_url
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = []

DEBUG = os.environ.get('DEBUG')

MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware'
]

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': ['templates'],
    'OPTIONS': {
        'libraries': {
            'filters': 'filters'
        }
    }
}]

STATIC_URL = '/static/'
STATIC_ROOT = 'static'

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'app.wsgi'

DATABASES = {
    'default': dj_database_url.parse(os.getenv('POSTGRES_URL'))
}
