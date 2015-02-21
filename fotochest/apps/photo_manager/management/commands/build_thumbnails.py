"""
fotochest.apps.photo_manager.management.commands.build_thumbnails
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:license: MIT, see LICENSE for more details.
"""


from django.core.management.base import BaseCommand

from fotochest.apps.photo_manager.models import Photo


class Command(BaseCommand):
    """
    Rebuilds thumbnails for all photos.
    """
    def handle(self, *args, **options):
        for photo in Photo.objects.all():
            photo.make_thumbnails()