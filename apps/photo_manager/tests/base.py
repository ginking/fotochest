from django.test import TestCase
from django.contrib.auth.models import User

from photo_manager.models import Photo, Album


class BasePhotoTestClass(TestCase):

    def setUp(self):
        self.user = User.objects.create()
        self.album = Album.objects.create(user=self.user, title='Album Name')
        self.photo = Photo.objects.create(album=self.album, title='Hello World')
