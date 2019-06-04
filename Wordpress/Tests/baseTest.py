from PageObjectModel.Wordpress.Pages.LoginPage import LoginPage
from PageObjectModel.Wordpress.Tools.PostCreator import PostCreator
from PageObjectModel.Wordpress.Tools.BrowserManager import Browser
from selenium import webdriver

import unittest

class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.create_new_driver(Browser.CHROME)
        self.driver.maximize_window()
        login_page = LoginPage(self.driver)
        login_page.go_to()
        login_page.do_login("root", "12369874", True)

    def screen_shot(self):
        """Take a Screenshot on Failure."""
        for method, error in self._outcome.errors:
            if error:
                self.driver.get_screenshot_as_file("screenshot" + self.id() + ".png")
        
    def tearDown(self):
        PostCreator.trash_post(self)
        # self.screen_shot
        Browser.quit()