from django.conf import settings


import defaults


def is_using_celery():
    """ Simply return if the user is using
    Celery for task queuing or not.
    """

    return getattr(settings, 'FOTOCHEST_ENABLE_CELERY', defaults.FOTOCHEST_ENABLE_CELERY)