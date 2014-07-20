from .base import BaseLiveTest

from django.contrib.auth.models import User
from photo_manager.models import Photo, Album


class TestHomePageView(BaseLiveTest):

    def test_home_view_has_images(self):
        """
        Test that the home page has a page with images
        :return:
        """

        # Need to make sure an image is on the page.
        user = User.objects.create()
        album = Album.objects.create(user=user)
        Photo.objects.create(album=album, title='Hello World')

        # User opens home page
        self.browser.visit(self.live_server_url)

        self.assertTrue(self.browser.find_by_css('.thumbnails'))



