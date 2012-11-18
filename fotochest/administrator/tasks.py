from celery.task import task

__author__ = 'Derek Stegelman'
__date__ = '8/22/12'

@task()
def thumbnail_task(photo):
    photo.make_thumbnails()
    photo.thumbs_created = True
    photo.save()

@task()
def thumbnail_cleanup_task(photo):
    from sorl.thumbnail import delete
    delete(photo.image, delete_file=False)
    photo.thumbs_created = False
    photo.save()