from celery.task import Task
from celery.registry import tasks
from photo_manager.models import Photo

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