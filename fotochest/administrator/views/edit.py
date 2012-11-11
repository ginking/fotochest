from django.conf import settings

from PIL import Image

from fotochest.photo_manager.models import Photo
from fotochest.administrator.tasks import ThumbnailCleanupTask, ThumbnailTask

def rotate(photo_id, right=True):
    """ Rotate a photo, save it, and execute
     the cleanup task.
    """
    photo = Photo.objects.get(pk=photo_id)
    path = "%s/%s" % (settings.MEDIA_ROOT, photo.image)
    im = Image.open(path)
    if right:
        im.rotate(270).save(path)
    else:
        im.rotate(90).save(path)
    ThumbnailCleanupTask.delay(photo_id)
    ThumbnailTask.delay(photo_id)