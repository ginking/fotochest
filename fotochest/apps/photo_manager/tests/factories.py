import factory
from photo_manager.models import Album, Photo


# Album Factory
class AlbumFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Album
    
    title = "Roma"
    description = "Rome travel trip."
        

# Photo Factory
class PhotoFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Photo
