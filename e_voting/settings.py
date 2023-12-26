from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = '%6lp_p!%r$7t-2ql5hc5(r@)8u_fc+6@ugxcnz=h=b(fn#3$p9'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'account.apps.AccountConfig',
    'voting.apps.VotingConfig',
    'administrator.apps.AdministratorConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'account.middleware.AccountCheckMiddleWare',
]

ROOT_URLCONF = 'e_voting.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['voting/templates', 'administrator/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'voting.context_processors.ElectionTitle'
            ],
        },
    },
]

WSGI_APPLICATION = 'e_voting.wsgi.application'

DATABASES = {
    #   You can use this :
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

AUTH_USER_MODEL = 'account.CustomUser'
AUTHENTICATION_BACKENDS = ['account.email_backend.EmailBackend']

ELECTION_TITLE_PATH = os.path.join(
    BASE_DIR, 'election_title.txt')

SEND_OTP = False
