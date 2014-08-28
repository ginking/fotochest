import factory

from django.contrib.auth.models import User
from fotochest.apps.photo_manager.models import Album, Photo

from locations.models import Location


class LocationFactory(factory.DjangoModelFactory):
    class Meta:
        model = Location

    city = 'Loveland'
    state = 'KS'
    country = 'USA'
    latitude = '12312'
    longitude = '123423'
    default_location = False


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User

    first_name = 'John'
    last_name = 'Doe'
    username = 'john'


class AlbumFactory(factory.DjangoModelFactory):
    class Meta:
        model = Album

    title = 'New Album'
    user = factory.SubFactory(UserFactory, username='johnsmith')


class PhotoFactory(factory.DjangoModelFactory):
    class Meta:
        model = Photo

    user = factory.SubFactory(UserFactory)
    location = factory.SubFactory(LocationFactory)
    album = factory.SubFactory(AlbumFactory)
    title = 'Hello World'