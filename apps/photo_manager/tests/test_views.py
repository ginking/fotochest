from django.test import TestCase


from photo_manager.models import Photo, Album
from django.contrib.auth.models import User

class PhotoViewTestCase(TestCase):

    def test_home_page_photo(self):
        user = User.objects.create()
        album = Album.objects.create(user=user)
        Photo.objects.create(album=album, title='Hello World')
        response = self.client.get('/')

        self.assertIn('Hello World', response.content)

    def test_single_photo_view(self):
        user = User.objects.create()
        album = Album.objects.create(user=user)
        p = Photo.objects.create(album=album, title='Hello World')
        response = self.client.get(p.get_absolute_url())

        self.assertIn('Hello World', response.content)

class AlbumViewTestCase(TestCase):

    def test_album_view(self):
        user = User.objects.create()
        album = Album.objects.create(user=user, title='test')

        response = self.client.get('/album/%s/' % album.slug)
        self.assertIn('test', response.content)