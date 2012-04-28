from django.test import TestCase
from django.test.client import Client
from photo_manager.models import *
from photo_manager.tests.factories import AlbumFactory, PhotoFactory
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class AlbumModelTest(TestCase):

    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="derekst", email="bob@email.com", password="pass")
        self.user.is_staff = True
        self.user.is_superuser = True
        self.user.save()
        self.album = AlbumFactory.create(user=self.user)
        self.child_album = AlbumFactory.create(user=self.user, parent_album=self.album, title="Saint Peters")

    def test_slugify(self):
        self.assertEqual(self.album.slug, "roma")
        
    def test_child_albums(self):
        self.assertTrue(self.album.has_child_albums)
    
    def test_unicode(self):
        self.assertEqual(self.album.__unicode__(), "Roma test tes")
            