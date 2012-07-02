from django.test import LiveServerTestCase
from django.contrib.auth.models import User
from photo_manager.tests.factories import *
from selenium import webdriver
from administrator.tests.factories import SettingsFactory
from django.conf import settings


class PhotoManagerServerTests(LiveServerTestCase):

    def setUp(self):
        print "Setting Live Tests"
        super(PhotoManagerServerTests, self).setUp()
        self.user = User.objects.create_user(username="derek", email="bob@email.com", password="pass")
        self.user.is_superuser = True
        self.user.is_staff = True
        self.user.save()
        self.settings = SettingsFactory.create()
        settings.DEBUG = True    
    
    @classmethod
    def setUpClass(cls):
        cls.selenium = webdriver.Firefox()
        super(PhotoManagerServerTests, cls).setUpClass()
    
    @classmethod
    def tearDownClass(cls):
        super(PhotoManagerServerTests, cls).tearDownClass()
        cls.selenium.quit()
        
    def test_login(self):
        self.selenium.get("%s%s" % (self.live_server_url, "/admin/"))
    
        
    def test_initial(self):
        self.selenium.get("%s%s" % (self.live_server_url, "/"))
        
    
     
