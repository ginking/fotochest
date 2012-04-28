from django.test import TestCase
from django.test.client import Client
from photo_manager.models import *
from django.core.urlresolvers import reverse
# Test Views, Model Managers, Methods


class ViewTest(TestCase):
    
    fixtures = ['photo_manager_test_data.json']
    urls = 'urls.local'
    
    def setUp(self):
        self.client = Client()
        

class AlbumModelTest(TestCase):
    fixtures = ['photo_manager_test_data.json']
    urls = 'photo_manager.urls'
    
    def setUp(self):
        self.client = Client()
    
    def test_quick(self):
        self.assertEqual(1 + 1, 2)
            