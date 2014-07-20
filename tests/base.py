from django.test.testcases import LiveServerTestCase

from splinter import Browser


class BaseLiveTest(LiveServerTestCase):

    def setUp(self):
        self.browser = Browser()

    def tearDown(self):
        self.browser.quit()


