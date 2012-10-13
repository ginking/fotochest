from celery.task import Task
from celery.registry import tasks

from fotochest.photo_manager.models import Photo

__author__ = 'Derek Stegelman'
__date__ = '8/22/12'

class ThumbnailTask(Task):
    def run(self, photo_id, **kwargs):
        photo = Photo.objects.get(pk=photo_id)
        photo.make_thumbnails()
        photo.thumbs_created = True
        photo.save()

tasks.register(ThumbnailTask)

class ThumbnailCleanupTask(Task):
    def run(self, photo_id, **kwargs):
        photo = Photo.objects.get(pk=photo_id)
        from sorl.thumbnail import delete
        delete(photo.image, delete_file=False)
        photo.thumbs_created = False
        photo.save()
        
tasks.register(ThumbnailCleanupTask)