# from selenium.webdriver.chrome.options import Options
from PageObjectModel.Wordpress.Pages.LoginPage import LoginPage
from PageObjectModel.Wordpress.Tools.PostCreator import PostCreator
from selenium import webdriver
import unittest

class BaseTest(unittest.TestCase):
    def setUp(self):
        # chrome_options = Options()
        # chrome_options.add_argument("--headless")
        # self.driver = webdriver.Chrome(options=chrome_options)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        PostCreator.initialize(self)
        login_page = LoginPage(self.driver)
        login_page.go_to()
        login_page.do_login("root", "12369874", True)
        self.driver.implicitly_wait(10)
        
    def tearDown(self):
        PostCreator.trash_post(self)
        self.driver.quit()