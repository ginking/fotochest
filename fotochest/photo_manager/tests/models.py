from django.test import TestCase
from django.test.client import Client
from fotochest.photo_manager.models import *
from fotochest.photo_manager.tests.factories import AlbumFactory, PhotoFactory
from django.contrib.auth.models import User

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
        self.assertTrue(self.album.has_child_albums)
    
    def test_unicode(self):
        self.assertEqual(self.album.__unicode__(), "Roma")
            
    def test_get_album_cover(self):
        cover = self.album.get_album_cover()
        self.assertEqual(cover.title, u'Vatican')
        
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
        
        
    