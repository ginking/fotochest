# Django settings for your project.
import conf.environment
import os

SITE_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

import djcelery
djcelery.setup_loader()

BROKER_TRANSPORT = "django"
CELERY_ACKS_LATE = True
CELERYD_PREFETCH_MULTIPLIER = 1

MANAGERS = ADMINS

TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True


ENABLE_CELERY = True
ACTIVE_THEME = "default"
VERSION_NUMBER = "2.3"
AUTH_PROFILE_MODULE = "profiles.Profile"
CRISPY_TEMPLATE_PACK = 'bootstrap'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'bfg=rdjp)u^qhv&9jo@f$!*s6ar*o%4a0$4x#c&6weyq&9fcv4'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
    "photo_manager.context_processors.theme_files",
    "photo_manager.context_processors.locations_albums",
    "photo_manager.context_processors.version",
    "administrator.context_processors.settings",
) 

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)


ROOT_URLCONF = 'urls'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

HAYSTACK_SEARCH_ENGINE = 'whoosh'
HAYSTACK_SITECONF = 'search_sites'
HAYSTACK_WHOOSH_PATH = os.path.join(SITE_ROOT, "whoosh")

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

    'hadrian.contrib.locations',
    'hadrian.contrib.pomona',
    'tastypie',
    'photo_manager',
    'administrator',
    'api_docs',
    'taggit',
    # Everyone should be using south.  Seriously.
    'south',
    'crispy_forms',
    'sorl.thumbnail',
    'djcelery',
    'djkombu',
    'test_utils',
    'haystack',
    'django_extensions',
    )


