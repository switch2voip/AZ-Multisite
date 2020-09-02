from .local import *


ALLOWED_HOSTS = ['django.altotelecom.com', '127.0.0.1', 'localhost']

#INSTALLED_APPS += []


SITE_ID = 1

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static/flexor')]

print(STATICFILES_DIRS)