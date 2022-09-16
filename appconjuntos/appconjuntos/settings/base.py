from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
BASE_FILES = Path('../front_vue/public').resolve()

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--beje9j=(i-r^+d@8v@j$+jtoya(h7ea!+a)a=h1pm3t%1)ygl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
#ALLOWED_HOSTS = []
#ALLOWED_HOSTS = ['192.168.0.2', '192.168.0.2:8000', 'localhost', '127.0.0.1']


# Application definition

BASE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LOCAL_APPS = [
    'apps.users',
    'apps.conjunto',
    'apps.propiedad',
    'apps.parqueadero',
    'apps.tipo_parqueadero',
    'apps.tipo_vehiculo',
    'apps.person',
    'apps.vehiculo',
    'apps.vehiculo_parqueadero',
    'apps.visitante',
    'apps.noticia',
    'apps.auditoria_pedido',
    'apps.tipo_aviso',
    'apps.aviso',
    'apps.casillero',
]

THIRD_APPS = [
    'simple_history',
    'corsheaders',
    'ninja'
]

INSTALLED_APPS = BASE_APPS + LOCAL_APPS + THIRD_APPS
#INSTALLED_APPS = BASE_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
]

ROOT_URLCONF = 'appconjuntos.urls'

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

WSGI_APPLICATION = 'appconjuntos.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

#cors
CORS_ALLOWED_ORIGINS = [
    "http://192.168.0.2:3000",
    "http://localhost:3000",
]
#metdo de autenticación
AUTH_USER_MODEL = 'users.User'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

#DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
MEDIA_ROOT = os.path.join(BASE_FILES, 'media')

MEDIA_URL = '/media/'