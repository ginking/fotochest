from django.test import TestCase

from django.contrib.auth.models import User
from photo_manager.models import Photo, Album

class AlbumModelTestCase(TestCase):

    def test_album_creation(self):
        pass


class PhotoModelTestCase(TestCase):

    def test_can_create_photo(self):
        user = User.objects.create()
        album = Album.objects.create(user=user)
        Photo.objects.create(album=album, title='Hello World')
        response = self.client.get('/')

        self.assertIn('Hello World', response.content)
