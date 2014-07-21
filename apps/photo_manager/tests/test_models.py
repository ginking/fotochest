from django.test import TestCase

from django.contrib.auth.models import User
from photo_manager.models import Photo, Album

class AlbumModelTestCase(TestCase):
    pass



class PhotoModelTestCase(TestCase):

    def test_photo_absolute_url(self):
        user = User.objects.create()
        album = Album.objects.create(user=user)
        p = Photo.objects.create(album=album, title='Hello World')

        self.assertEqual(p.get_absolute_url(), '/photos/%s/%s/' % (album.slug, p.slug))

    def test_preview_photos(self):
        user = User.objects.create()
        album = Album.objects.create(user=user, title='Test')
        p = Photo.objects.create(album=album, title='Hello World')
        p2 = Photo.objects.create(album=album, title='Hellow World Again')
        self.assertIn(p, album.preview_photos)
        self.assertIn(p2, album.preview_photos)
