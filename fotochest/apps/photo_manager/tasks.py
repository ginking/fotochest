"""
fotochest.apps.photo_manager.tasks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:license: MIT, see LICENSE for more details.
"""


from celery import shared_task


@shared_task()
def clear_thumbnails(photo):
    """ @todo - Add Comments
    """

    photo._clear_thumbnails()


@shared_task()
def build_thumbnails(photo):
    """ @todo - Add Comments
    """

    photo.make_thumbnails()