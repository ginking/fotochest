from photo_manager.models import Photo, Album

from .base import BasePhotoTestClass


class AlbumModelTestCase(BasePhotoTestClass):
    def test_preview_photos(self):
        self.assertIn(self.photo_2 or self.photo_3, self.album.preview_photos)

    def test_has_no_child_albums(self):
        self.assertFalse(self.album.has_child_albums)

    def test_has_child_albums(self):
        Album.objects.create(user=self.user, title='child', parent_album=self.album)

        self.assertTrue(self.album.has_child_albums)

    def test_photo_count(self):
        self.assertEqual(self.album.count, 3)


class PhotoModelTestCase(BasePhotoTestClass):

    def test_photo_absolute_url(self):
        self.assertEqual(self.photo.get_absolute_url(), '/photos/%s/%s/' % (self.album.slug, self.photo.slug))

    def test_get_next(self):
        self.assertEqual(self.photo_2.get_next(), self.photo.get_absolute_url())

    def test_get_previous(self):
        self.assertEqual(self.photo_2.get_previous(), self.photo_3.get_absolute_url())

    def test_author(self):
        self.assertEqual(self.photo.author, 'John Doe')

    def test_get_fullscreen_url(self):
        self.assertEqual(self.photo.get_fullscreen(), '/photos/new-album/hello-world/fullscreen/')


