from settings.common import *
import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG
THUMBNAIL_DEBUG = DEBUG


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
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

WSGI_APPLICATION = 'wsgi.application'

STATICFILES_DIRS = (
    os.path.join(SITE_ROOT, 'themes/default/static'),
    os.path.join(SITE_ROOT, 'themes/twitter/static'),
    os.path.join(SITE_ROOT, 'static'),
)

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '%sadmin/' % STATIC_URL

PHOTO_DIRECTORY = os.path.join(SITE_ROOT, 'uploads/images')

WSGI_APPLICATION = 'wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT, 'themes/default/templates'),
    os.path.join(SITE_ROOT, 'themes/twitter/templates'),
    os.path.join(SITE_ROOT, 'templates'),
)

DOMAIN_STATIC = '/static/'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)
INTERNAL_IPS = ('127.0.0.1',)

ROOT_URLCONF = 'urls.local'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.comments',
    #'grappelli',
    'django.contrib.admin',
    'debug_toolbar',
    'hadrian.contrib.locations',
    'hadrian.contrib.pomona',
    'tastypie',
    'photo_manager',
    'administrator',
    'api_docs',
    # Everyone should be using south.  Seriously.
    'south',
    'crispy_forms',
    'sorl.thumbnail',
    'djcelery',
    'djkombu',
    'test_utils',
    'haystack',
    #'photo_admin',
    
    #'profiles',
    #'tagging',

)