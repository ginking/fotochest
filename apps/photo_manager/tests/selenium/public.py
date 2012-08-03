from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class Public(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8000/"
        self.verificationErrors = []
    
    def test_public(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("FotoChest").click()
        driver.find_element_by_link_text("Albums").click()
        driver.find_element_by_link_text("Map").click()
        driver.find_element_by_xpath("//div[@id='map']/div/div/div/div[4]/div/div/div[13]/canvas").click()
        driver.find_element_by_link_text("Manhattan, KS (144)").click()
        driver.find_element_by_css_selector("img[alt=\"blh\"]").click()
        driver.find_element_by_link_text("From yo yo daw").click()
        driver.find_element_by_link_text("Home").click()
        driver.find_element_by_css_selector("img[alt=\"5400384687366.JPG\"]").click()
        driver.find_element_by_link_text("Full Screen").click()
        driver.find_element_by_link_text("Previous").click()
        driver.find_element_by_css_selector("i.icon-arrow-right").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
