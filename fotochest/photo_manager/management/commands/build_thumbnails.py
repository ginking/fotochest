from django.core.management.base import BaseCommand

from fotochest.photo_manager.models import Photo


class Command(BaseCommand):
    """
    Rebuilds thumbnails for all photos.
    """
    def handle(self, *args, **options):
        for photo in Photo.objects.all():
            photo.make_thumbnails()