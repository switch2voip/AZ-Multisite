from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []




# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}




# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT =  os.path.join(BASE_DIR, 'static_root')

MEDIA_URL = '/media/'
MEDIA_ROOT = 'media'

# stripe settings

if DEBUG:
   # test key
    STRIPE_PUBLISHABLE_KEY = ''
    STRIPE_STRIPE_KEY = ''

else:
# live key
    STRIPE_PUBLISHABLE_KEY = 'YOUR STRIPE LIVE PUB KEY'
    STRIPE_STRIPE_KEY = 'YOUR STRIPE LIVE SECRET KEY'

