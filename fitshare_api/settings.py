from pathlib import Path
import os
import dj_database_url
from urllib.parse import urlparse

if os.path.exists('env.py'):
    import env

# Cloudinary Storage Configuration
CLOUDINARY_STORAGE = {
    'CLOUDINARY_URL': os.environ.get('CLOUDINARY_URL')
}
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings
SECRET_KEY = os.getenv('SECRET_KEY', 'unsafe-default-secret-key')

# Enable DEBUG mode based on environment
DEBUG = 'DEV' in os.environ

# Hosts and dynamic Gitpod workspace handling
ALLOWED_HOSTS = [
    os.environ.get('ALLOWED_HOST'),
    'localhost',
    '127.0.0.1',
    'https://fitshare-d428ae7f1a9f.herokuapp.com',  # Replace with deployed URL
    '8000-mabdillahi8-fitshareapi-ageqqbs7o91.ws.codeinstitute-ide.net',  # Gitpod workspace
    'mabdillahi8-fitshareapi-ageqqbs7o91.ws.codeinstitute-ide.net',
]

# Dynamically add Gitpod workspace URL
if 'GITPOD_WORKSPACE_URL' in os.environ:
    workspace_url = os.environ['GITPOD_WORKSPACE_URL']
    parsed_url = urlparse(workspace_url)
    ALLOWED_HOSTS.append(parsed_url.netloc)

print("ALLOWED_HOSTS:", ALLOWED_HOSTS)

# CSRF Trusted Origins
CSRF_TRUSTED_ORIGINS = [
    'https://fitshare-d428ae7f1a9f.herokuapp.com',  # Replace with deployed URL
    'http://127.0.0.1:8000',  # Local development
    'https://8000-mabdillahi8-fitshareapi-ageqqbs7o91.ws.codeinstitute-ide.net',
    'https://mabdillahi8-fitshareapi-ageqqbs7o91.ws.codeinstitute-ide.net',
]

if 'GITPOD_WORKSPACE_URL' in os.environ:
    workspace_url = os.environ['GITPOD_WORKSPACE_URL']
    parsed_url = urlparse(workspace_url)
    CSRF_TRUSTED_ORIGINS.append(f"https://{parsed_url.netloc}")

# CORS Allowed Origins
CORS_ALLOWED_ORIGINS = [
    'https://fitshare-d428ae7f1a9f.herokuapp.com',  # Replace with deployed URL
    'https://8000-mabdillahi8-fitshareapi-ageqqbs7o91.ws.codeinstitute-ide.net',
    'https://mabdillahi8-fitshareapi-ageqqbs7o91.ws.codeinstitute-ide.net',
]

# Installed Applications
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'cloudinary',
    'rest_framework',
    'django_filters',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
    'rest_framework_simplejwt.token_blacklist',
    'corsheaders',
    'profiles',
    'posts',
    'comments',
    'likes',
    'followers',
]
SITE_ID = 1

# Middleware
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

# URL Configuration
ROOT_URLCONF = 'fitshare_api.urls'

# Templates
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

# WSGI Application
WSGI_APPLICATION = 'fitshare_api.wsgi.application'

# Database Configuration
if 'DEV' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
    }

# Password Validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static and Media Files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# REST Framework Configuration
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication'
        if 'DEV' in os.environ
        else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DATETIME_FORMAT': '%d %b %Y',
}

if 'DEV' not in os.environ:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = [
        'rest_framework.renderers.JSONRenderer',
    ]

REST_USE_JWT = True
JWT_AUTH_SECURE = True
JWT_AUTH_COOKIE = 'my-app-auth'
JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token'
JWT_AUTH_SAMESITE = 'None'

REST_AUTH = {
    'USE_JWT': True,
    'JWT_AUTH_HTTPONLY': False,
    'JWT_AUTH_COOKIE': 'auth-token',
    'JWT_AUTH_REFRESH_COOKIE': 'refresh-token',
    'JWT_AUTH_SECURE': True,
    'JWT_AUTH_SAMESITE': 'None',
}

REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'fitshare_api.serializers.CurrentUserSerializer'
}

# Email Backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# CORS Configuration
CORS_ALLOW_CREDENTIALS = True
