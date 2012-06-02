from haystack.indexes import *
from photo_manager.models import Photo, Album
from haystack import site

class PhotoIndex(SearchIndex):
    text = CharField(document=True, use_template=True)

    def index_queryset(self):
        """Used when the entire index for model is updated."""
        return Photo.objects.all()
        
site.register(Photo, PhotoIndex)

class AlbumIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    
    def index_queryset(self):
        return Album.objects.all()
        
site.register(Album, AlbumIndex)