from .common import *

DEBUG = False
## Database Configurations

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.xx', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'xx',                      # Or path to database file if using sqlite3.
        'USER': 'xx',                      # Not used with sqlite3.
        'PASSWORD': 'xx',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(SITE_ROOT, 'upload')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

PHOTO_DIRECTORY = MEDIA_ROOT

TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT, 'templates'),
)

DOMAIN_STATIC = '/static/'

BROKER_URL = 'redis://localhost:6379/0'
ALLOWED_HOSTS = ['example.com']
APP_NAME = 'photos.stegelman.com'
