import os
from django.contrib.messages import constants as messages
from django.contrib.messages import constants as message_constants
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)dj@=+rvt9!idx20$uy=bsuv+q_im=@i^8%v2op3zng3y+hl9h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'microposts',
    'bootstrap4',

]

BOOTSTRAP4 = {
   'include_jquery': True,
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sns.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'builtins': [
               'bootstrap4.templatetags.bootstrap4',
           ],
        },
    },
]

WSGI_APPLICATION = 'sns.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

PASSWORD_HASHERS = [
   'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
   'django.contrib.auth.hashers.BCryptPasswordHasher',
   'django.contrib.auth.hashers.PBKDF2PasswordHasher',
   'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
]

# 追加
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
# 追加 mediaを扱うための設定
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# 追加 メッセージタグの設定
MESSAGE_TAGS = {
   messages.ERROR: 'alert alert-danger',
   messages.WARNING: 'alert alert-warning',
   messages.SUCCESS: 'alert alert-success',
   messages.INFO: 'alert alert-info'
}

AUTH_USER_MODEL = 'accounts.User'

# login,logoutした時のURLを記述
LOGIN_URL = '/accounts/login'
LOGIN_REDIRECT_URL = '/accounts/userlist'
LOGOUT_REDIRECT_URL = '/accounts/login'