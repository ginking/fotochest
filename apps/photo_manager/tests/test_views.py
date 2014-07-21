from django.test import TestCase
import unittest

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

    @unittest.skip('skipping')
    def test_short_single_photo_view(self):
        user = User.objects.create()
        album = Album.objects.create(user=user)
        p = Photo.objects.create(album=album, title='Hello World')
        response = self.client.get('/f/%s/' % p.id)

        self.assertIn('Hello World', response.content)

    def test_fullscreen_view(self):
        user = User.objects.create()
        album = Album.objects.create(user=user)
        p = Photo.objects.create(album=album, title='Hellow World')
        response = self.client.get(p.get_absolute_url() + 'fullscreen/')

        self.assertTrue(response.status_code, 200)


class FeedViewTestCase(TestCase):
    def test_feed_view(self):
        user = User.objects.create()
        album = Album.objects.create(user=user)
        Photo.objects.create(album=album, title='Test')

        response = self.client.get('/feed/')
        self.assertIn('Test', response.content)

    def test_album_feed(self):
        user = User.objects.create()
        album = Album.objects.create(user=user)
        Photo.objects.create(album=album, title='Test')

        response = self.client.get('/album/%s/feed/' % album.slug)
        self.assertIn('Test', response.content)


class AlbumViewTestCase(TestCase):

    def test_album_view(self):
        user = User.objects.create()
        album = Album.objects.create(user=user, title='test')

        response = self.client.get('/album/%s/' % album.slug)
        self.assertIn('test', response.content)

    def test_albums_view(self):
        user = User.objects.create()
        Album.objects.create(user=user, title='test')

        response = self.client.get('/albums/')
        self.assertIn('test', response.content)


class MapsTestViewCase(TestCase):
    def test_maps_page(self):
        response = self.client.get('/map/')
        self.assertEqual(response.status_code, 200)