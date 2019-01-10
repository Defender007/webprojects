from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewPostTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_open_the_homepage(self):
        self.browser.get(self.live_server_url)

        # self.assertIn('To-do', self.browser.title)
        self.fail('Finish the test!')
