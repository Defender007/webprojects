from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewPostTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_open_the_homepage(self):
        self.browser.get('http://localhost:8000')

        self.assertIn('To-do', self.browser.title)
        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')


# browser = webdriver.Firefox()
# browser.get('http://localhost:8000')
# assert 'Django' in browser.title
#
# browser.quit()
#
