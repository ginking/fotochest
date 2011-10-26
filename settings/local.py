from settings.common import *
import os

## Database Configurations

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': SITE_ROOT + '/dev.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(SITE_ROOT, 'uploads')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = 'http://localhost:8000/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = 'http://localhost:8000/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = 'http://localhost:8000/static_admin/'

PHOTO_DIRECTORY = os.path.join(SITE_ROOT, 'uploads/images')

TEMPLATE_DIRS = (
    #"/Users/Derek/Documents/code/personal/apps/fotochest/static/photo_manager/themes/default/templates"
    os.path.join(SITE_ROOT, 'static/photo_manager/themes/default/templates'),
    os.path.join(SITE_ROOT, 'templates')
)

DOMAIN_STATIC = 'http://localhost:8000/static/'

ENABLE_MULTI_USER = True

ROOT_URLCONF = 'urls.local'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    
    'photo_manager',
    # Everyone should be using south.  Seriously.
    'south',
    'sorl.thumbnail',
    'photo_admin',
    'locations',
    'profiles',
    #'tagging',

)