from PageObjectModel.Wordpress.Tests.baseTest import BaseTest

class LoginTest(BaseTest):

    def test_login_valid(self):
        driver = self.driver
        self.assertIn("Dashboard", driver.page_source, "Login failed")