from celery.task import task

@task()
def thumbnail_task(photo):
    photo.make_thumbnails()
    photo.thumbs_created = True
    photo.save()
