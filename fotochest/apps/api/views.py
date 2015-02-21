"""
fotochest.apps.api.views
~~~~~~~~~~~~~~~~~~~~~~~~

:license: MIT, see LICENSE for more details.
"""

from rest_framework import viewsets


from fotochest.apps.photo_manager.models import Photo, Album
from fotochest.apps.api.serializers import PhotoSerializer, AlbumSerializer


class PhotoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class AlbumViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
