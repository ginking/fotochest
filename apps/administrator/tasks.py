from celery.task import task

__author__ = 'Derek Stegelman'
__date__ = '8/22/12'

@task()
def thumbnail_task(photo):
    # USe new regenerate method.
    photo.make_thumbnails()
    photo.thumbs_created = True
    photo.save()

@task()
def thumbnail_cleanup_task(photo):
    photo.clear_thumbnails()