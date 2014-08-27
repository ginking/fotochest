from fotochest.apps.photo_manager.models import Album

from .base import BasePhotoTestClass


class AlbumModelTestCase(BasePhotoTestClass):
    def test_preview_photos(self):
        self.assertTrue([photo for photo in [self.photo, self.photo_2, self.photo_3] if photo in self.album.preview_photos])

    def test_has_no_child_albums(self):
        self.assertFalse(self.album.child_albums)

    def test_has_child_albums(self):
        Album.objects.create(user=self.user, title='child', parent_album=self.album)

        self.assertTrue(self.album.child_albums)

    def test_photo_count(self):
        self.assertEqual(self.album.count, 3)

    def test_album_cover(self):
        self.assertEqual(self.album.album_cover, self.photo_3)


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


