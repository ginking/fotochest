from .base import BasePhotoTestClass


class PhotoViewTestCase(BasePhotoTestClass):

    def test_home_page_photo(self):
        response = self.client.get('/')

        self.assertContains(response, 'Hello World')

    def test_single_photo_view(self):
        response = self.client.get(self.photo.get_absolute_url())

        self.assertContains(response, 'Hello World')

    def test_short_single_photo_view(self):
        response = self.client.get('/f/%s/' % self.photo.id)

        self.assertContains(response, 'Hello World')

    def test_fullscreen_view(self):
        response = self.client.get(self.photo.get_absolute_url() + 'fullscreen/')
        self.assertTrue(response.status_code, 200)


class FeedViewTestCase(BasePhotoTestClass):
    def test_feed_view(self):

        response = self.client.get('/feed/')
        self.assertContains(response, 'Hello World')

    def test_album_feed(self):

        response = self.client.get('/album/%s/feed/' % self.album.slug)
        self.assertContains(response, 'Hello World')


class AlbumViewTestCase(BasePhotoTestClass):

    def test_album_view(self):
        response = self.client.get('/album/%s/' % self.album.slug)
        self.assertContains(response, 'New Album')

    def test_albums_view(self):

        response = self.client.get('/albums/')
        self.assertContains(response, 'New Album')


class MapsTestViewCase(BasePhotoTestClass):
    def test_maps_page(self):
        response = self.client.get('/map/')
        self.assertEqual(response.status_code, 200)