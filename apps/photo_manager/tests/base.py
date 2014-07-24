from django.test import TestCase
from django.contrib.auth.models import User

from photo_manager.models import Photo, Album

from locations.models import Location


class BasePhotoTestClass(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='john', first_name='John', last_name='Doe')
        self.location = Location.objects.create(city='Loveland', state='KS', country='USA', default_location=False)
        self.album = Album.objects.create(user=self.user, title='New Album')
        self.photo = Photo.objects.create(user=self.user, album=self.album, title='Hello World', location=self.location)
        self.photo_2 = Photo.objects.create(user=self.user, album=self.album, title='second photo', location=self.location)
        self.photo_3 = Photo.objects.create(user=self.user, album=self.album, title='third photo', location=self.location)