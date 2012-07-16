from PIL import Image
from photo_manager.models import Photo
from django.conf import settings

def rotate_right(photo_id):
    photo = Photo.objects.get(pk=photo_id)
    im = Image.open("%s%s" % (settings.MEDIA_ROOT, photo.image))
    im.rotate(90)


def rotate_left(photo_id):
    photo = Photo.objects.get(pk=photo_id)
    im = Image.open("%s%s" % (settings.MEDIA_ROOT, photo.image))
    im.rotate(90)