import os
from pathlib import Path
import dj_database_url

if os.path.exists('env.py'):
    import env

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings
SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = 'DEV' in os.environ

ALLOWED_HOSTS = [
    os.environ.get('ALLOWED_HOST'),
    'localhost',
    '127.0.0.1',
    'fitshare-d428ae7f1a9.herokuapp.com',
]

# Dynamically handle Gitpod workspace hosts
if 'GITPOD_WORKSPACE_URL' in os.environ:
    gitpod_url = os.environ['GITPOD_WORKSPACE_URL']
    host = gitpod_url.replace('https://', '8000-')
    ALLOWED_HOSTS.append(host)

# CSRF Trusted Origins
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:3000",
    "https://fitshare-d428ae7f1a9.herokuapp.com",
    "https://3000-mabdillahi88-fitshare-yf826mfdqxj.ws.codeinstitute-ide.net",
]

if 'GITPOD_WORKSPACE_URL' in os.environ:
    gitpod_origin = os.environ['GITPOD_WORKSPACE_URL'].replace('https://', 'https://8000-')
    CSRF_TRUSTED_ORIGINS.append(gitpod_origin)

INSTALLED_APPS = [
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'cloudinary',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'corsheaders',
    'profiles',
    'posts',
    'comments',
    'likes',
    'followers',
    'rest_framework',
    'django_filters',
    'rest_framework_simplejwt',
    'dj_rest_auth',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Must be at the top
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'fitshare_api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # Required by allauth
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'fitshare_api.wsgi.application'

# Database configuration
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

# Password validation
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

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Media files
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Cloudinary configuration
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.getenv('CLOUDINARY_URL').split('@')[-1],
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# REST framework configuration
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

# DJ Rest Auth and Allauth Configuration
SITE_ID = 1
REST_USE_JWT = True
JWT_AUTH_COOKIE = 'my-app-auth'
JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token'
JWT_AUTH_SAMESITE = 'None'

# CORS configuration
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "https://fitshare-d428ae7f1a9.herokuapp.com",
    "https://3000-mabdillahi88-fitshare-yf826mfdqxj.ws.codeinstitute-ide.net",
]
CORS_ALLOW_CREDENTIALS = True

# Optionally, specify allowed headers if needed
from corsheaders.defaults import default_headers
CORS_ALLOW_HEADERS = list(default_headers) + [
    'x-csrftoken',
    'authorization',
    'content-type',
]

# Allauth email configurations
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_AUTHENTICATION_METHOD = 'username'
ACCOUNT_EMAIL_REQUIRED = False
