import unittest

from photo_manager.models import Photo, Album
from django.contrib.auth.models import User


from .base import BasePhotoTestClass

class PhotoViewTestCase(BasePhotoTestClass):

    def test_home_page_photo(self):
        response = self.client.get('/')

        self.assertIn('Hello World', response.content)


    @unittest.skip("Skipping For now")
    def test_single_photo_view(self):
        user = User.objects.create()
        album = Album.objects.create(user=user)
        p = Photo.objects.create(album=album, title='Hello World')
        response = self.client.get(p.get_absolute_url())

        self.assertIn('Hello World', response.content)

    @unittest.skip('skipping')
    def test_short_single_photo_view(self):
        user = User.objects.create()
        album = Album.objects.create(user=user)
        p = Photo.objects.create(album=album, title='Hello World')
        response = self.client.get('/f/%s/' % p.id)

        self.assertIn('Hello World', response.content)

    def test_fullscreen_view(self):
        response = self.client.get(self.photo.get_absolute_url() + 'fullscreen/')

        self.assertTrue(response.status_code, 200)


class FeedViewTestCase(BasePhotoTestClass):
    def test_feed_view(self):

        response = self.client.get('/feed/')
        self.assertIn('Hello World', response.content)

    def test_album_feed(self):

        response = self.client.get('/album/%s/feed/' % self.album.slug)
        self.assertIn('Hello World', response.content)


class AlbumViewTestCase(BasePhotoTestClass):

    def test_album_view(self):
        response = self.client.get('/album/%s/' % self.album.slug)
        self.assertIn('New Album', response.content)

    def test_albums_view(self):

        response = self.client.get('/albums/')
        self.assertIn('New Album', response.content)


class MapsTestViewCase(BasePhotoTestClass):
    def test_maps_page(self):
        response = self.client.get('/map/')
        self.assertEqual(response.status_code, 200)