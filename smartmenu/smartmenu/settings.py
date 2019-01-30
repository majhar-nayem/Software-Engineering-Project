import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%ow3^&r8$)ca5iid5&r3%gm3xb!6q7u2=4(e#-*t2^46+zun(j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    #'django.contrib.auth.backends.ModelBackendsocial_core',
    #'django.contrib.auth.backends',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'food.apps.FoodConfig',
    'accounts.apps.AccountsConfig',
    'api.apps.ApiConfig',
    'crispy_forms',
    'rest_framework',
    'social_django',
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend'
   # 'social_core.backends.open_id.OpenIdAuth',
   # 'social_core.backends.google.GoogleOpenId'
    'social_core.backends.google.GoogleOAuth2'
   # 'social_core.backends.google.GoogleOAuth',
  #  'social_core.backends.twitter.TwitterOAuth',
   # 'social_core.backends.yahoo.YahooOpenId',


]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'smartmenu.urls'

SILENCED_SYSTEM_CHECKS = [
    'django_mysql.W002',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'smartmenu.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'smartmenu',
        'HOST': '',
        'USER': 'root',
        'PASSWORD': '',
        'PORT': '3306',
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = 'base-home'

SOCIAL_AUTH_GOOGLE_0AUTH2_KEY= '824661736648-fph77anifi53juu4fdogo4k717hloekr.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_0AUTH2_SECRET= 'ogMdHpJhLdWhzYeJ6FiYKJH6'

SOCIAL_AUTH_FACEBOOK_0AUTH2_KEY='285808282047383'
SOCIAL_AUTH_FACEBOOK_0AUTH2_SECRECT='32aed97e572ea6cb1c0f145796853cb6'
