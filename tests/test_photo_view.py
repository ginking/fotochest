from .base import BaseLiveTest

from django.contrib.auth.models import User
from photo_manager.models import Photo, Album


class TesPhotoViews(BaseLiveTest):

    def test_single_photo_page_view(self):
        """
        Test that the home page has a page with images
        :return:
        """

        # Need to make sure an image is on the page.
        user = User.objects.create()
        album = Album.objects.create(user=user, title='Test')
        photo = Photo.objects.create(album=album, title='Hello World')

        # User opens home page
        self.browser.visit(self.live_server_url + photo.get_absolute_url())

        self.assertTrue(self.browser.is_text_present('Hello World'))



s