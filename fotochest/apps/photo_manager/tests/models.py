from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User

from fotochest.apps.photo_manager.tests.factories import AlbumFactory, PhotoFactory


class AlbumModelTest(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="derekst", email="bob@email.com", password="pass")
        self.user.is_staff = True
        self.user.is_superuser = True
        self.user.save()
        self.album = AlbumFactory.create(user=self.user)
        self.child_album = AlbumFactory.create(user=self.user, parent_album=self.album, title="Saint Peters")
        self.photo_1 = PhotoFactory.create(user=self.user, album=self.album, title="Vatican")

    def test_slugify(self):
        self.assertEqual(self.album.slug, "roma")
        
    def test_child_albums(self):
        self.assertEqual(self.album.child_albums[0].title, 'Saint Peters')
    
    def test_unicode(self):
        self.assertEqual(self.album.__unicode__(), "Roma")

        
class PhotoModelTest(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="derekst", email="bob@email.com", password="pass")
        self.user.is_staff = True
        self.user.is_superuser = True
        self.user.save()
        self.album = AlbumFactory.create(user=self.user)
        self.child_album = AlbumFactory.create(user=self.user, parent_album=self.album, title="Saint Peters")
        self.photo_1 = PhotoFactory.create(user=self.user, album=self.album, title="Vatican", image="images/99209831093.jpg")
        self.photo_2 = PhotoFactory.create(user=self.user, album=self.album, title="Saint Peters", image="images/20e93748.jpg")
        
    def test_filename(self):
        self.assertEqual(self.photo_1.filename, "99209831093.jpg")