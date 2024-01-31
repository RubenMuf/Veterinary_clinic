"""
Django settings for Veterinary_clinic project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@d#usd+)%cr9zu(r@-52_jr=u%mnb5z!sd^@udzmgdnjk^1ton'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1'] # это для вывода ошибки на страницу, если путь не прописан или какая-то ошибка в коде
INTERNAL_IPS = ['127.0.0.1'] # для джангодебага

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',# чтобы джанго подключал статические файлы и для джангодебага
    'django_extensions', # этот пакет упрощает работу в консоле, чтобы не писать команды на низком уровне и были подсказки в терминале как в пайчарме
    'clinic.apps.ClinicConfig',
    'users', # для регистрации на сайте
    # 'debug_toolbar' # для джангодебага


]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware', # по умолчанию присутствует, для аутентификации
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware', # по умолчанию присутствует, для аутентификации
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Veterinary_clinic.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'users.context_processors.get_pet_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'Veterinary_clinic.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'ru-Ru' # язык для администрации

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

MEDIA_ROOT = BASE_DIR / 'media' # путь куда сохраняются все скачиваемые файлы от пользователя, сама папка в проекте создается автоматически и в ней папка в uploads_model
MEDIA_URL = '/media/' # для сохранения в эту папку загружаемых файлов

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOGIN_REDIRECT_URL = 'home' # для перенаправления юзера после авторизации в системе на определенную страницу
LOGOUT_REDIRECT_URL = 'home' # после выхода открытие определенной страницы
LOGIN_URL = 'users:login' # переход неавторизированного пользователя на определенную страницу, если он хочет зайти на страницу которая доступна только для авторизированного пользователя


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' # отправка почтовых писем в консоль
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' # отправка почтовых писем на почту
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
EMAIL_HOST_USER = "rd.promiwka@yandex.ru"
EMAIL_HOST_PASSWORD = "bfumhqrcmhchuffg"



SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

AUTHENTICATION_BACKENDS = [ #
    'django.contrib.auth.backends.ModelBackend', # стандартный бекенд, делает авторизацию по логину и паролю
    'users.authentication.EmailAuthBackend' # свой бекенд который прописали в папке users в файле authenticationБ делает авторизацию по email
]