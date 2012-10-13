from PIL import Image
from fotochest.photo_manager.models import Photo
from django.conf import settings
from fotochest.administrator.tasks import ThumbnailCleanupTask, ThumbnailTask

def rotate_right(photo_id):
    photo = Photo.objects.get(pk=photo_id)
    path = "%s/%s" % (settings.MEDIA_ROOT, photo.image)
    im = Image.open(path)
    im.rotate(270).save(path)
    ThumbnailCleanupTask.delay(photo_id)
    ThumbnailTask.delay(photo_id)

def rotate_left(photo_id):
    photo = Photo.objects.get(pk=photo_id)
    path = "%s/%s" % (settings.MEDIA_ROOT, photo.image)
    im = Image.open(path)
    im.rotate(90).save(path)
    ThumbnailCleanupTask.delay(photo_id)
    ThumbnailTask.delay(photo_id)