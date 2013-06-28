from celery.task import task

#
# @task()
# def thumbnail_task(photo):
#     # USe new regenerate method.
#     photo.make_thumbnails()
#     photo.thumbs_created = True
#     photo.save()
#
# @task()
# def thumbnail_cleanup_task(photo):
#     photo.clear_thumbnails()


@task(name='fotochest.photo_manager.clear_thumbnails')
def clear_thumbnails(photo):
    photo._clear_thumbnails()

@task(name='fotochest.photo_manager.build_thumbnails')
def build_thumbnails(photo):
    photo.make_thumbnails()