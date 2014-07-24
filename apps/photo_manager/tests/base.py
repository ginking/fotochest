from django.test import TestCase


from photo_manager.tests.factories import PhotoFactory


class BasePhotoTestClass(TestCase):
    def setUp(self):

        self.photo = PhotoFactory()
        self.user = self.photo.user
        self.album = self.photo.album
        self.location = self.photo.location

        self.photo_2 = PhotoFactory.create(user=self.user, album=self.album, title='second photo', location=self.location)
        self.photo_3 = PhotoFactory.create(user=self.user, album=self.album, title='third photo', location=self.location)