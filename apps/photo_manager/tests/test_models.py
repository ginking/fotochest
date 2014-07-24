from photo_manager.models import Photo, Album

from .base import BasePhotoTestClass


class AlbumModelTestCase(BasePhotoTestClass):
    def test_preview_photos(self):
        p2 = Photo.objects.create(album=self.album, title='Hellow World Again')
        self.assertIn(self.photo, self.album.preview_photos)
        self.assertIn(p2, self.album.preview_photos)

    def test_has_no_child_albums(self):
        self.assertFalse(self.album.has_child_albums)

    def test_has_child_albums(self):
        Album.objects.create(user=self.user, title='child', parent_album=self.album)

        self.assertTrue(self.album.has_child_albums)

    def test_photo_count(self):
        self.assertEqual(self.album.count, 1)


class PhotoModelTestCase(BasePhotoTestClass):

    def test_photo_absolute_url(self):
        self.assertEqual(self.photo.get_absolute_url(), '/photos/%s/%s/' % (self.album.slug, self.photo.slug))


