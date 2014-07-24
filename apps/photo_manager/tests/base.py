from django.test import TestCase
from django.contrib.auth.models import User

from photo_manager.models import Photo, Album

from locations.models import Location


class BasePhotoTestClass(TestCase):

    def setUp(self):
        self.user = User.objects.create()
        self.location = Location.objects.create(city='Loveland', state='KS', country='USA', default_location=False)
        self.album = Album.objects.create(user=self.user, title='New Album')
        self.photo = Photo.objects.create(album=self.album, title='Hello World', location=self.location)
