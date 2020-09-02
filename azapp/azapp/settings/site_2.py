from .local import *

ALLOWED_HOSTS = ['django.switch2voip.us', '127.0.0.1']

# Application definition


SITE_ID = 2

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static/youapps')]
