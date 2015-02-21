"""
fotochest.apps.administrator.tasks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:license: MIT, see LICENSE for more details.
"""


from celery import shared_task


@shared_task()
def thumbnail_task(photo):
    # USe new regenerate method.
    photo.make_thumbnails()
    photo.thumbs_created = True
    photo.save()

@shared_task()
def thumbnail_cleanup_task(photo):
    photo.clear_thumbnails()