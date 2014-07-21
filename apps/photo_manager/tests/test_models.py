from django.test import TestCase

from django.contrib.auth.models import User
from photo_manager.models import Photo, Album

class AlbumModelTestCase(TestCase):
    def test_preview_photos(self):
        user = User.objects.create()
        album = Album.objects.create(user=user, title='Test')
        p = Photo.objects.create(album=album, title='Hello World')
        p2 = Photo.objects.create(album=album, title='Hellow World Again')
        self.assertIn(p, album.preview_photos)
        self.assertIn(p2, album.preview_photos)

    def test_has_no_child_albums(self):
        user = User.objects.create()
        album = Album.objects.create(user=user, title='Test')

        self.assertFalse(album.has_child_albums)

    def test_has_child_albums(self):
        user = User.objects.create()
        album = Album.objects.create(user=user, title='Test')
        Album.objects.create(user=user, title='child', parent_album=album)

        self.assertTrue(album.has_child_albums)

    def test_photo_count(self):
        user = User.objects.create()
        album = Album.objects.create(user=user, title='Test')
        Photo.objects.create(album=album, title='He')

        self.assertEqual(album.count, 1)


    def test_album_cover(self):
        self.fail("Fix Me")




class PhotoModelTestCase(TestCase):

    def test_photo_absolute_url(self):
        user = User.objects.create()
        album = Album.objects.create(user=user)
        p = Photo.objects.create(album=album, title='Hello World')

        self.assertEqual(p.get_absolute_url(), '/photos/%s/%s/' % (album.slug, p.slug))


