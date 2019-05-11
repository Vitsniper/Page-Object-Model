from PageObjectModel.Wordpress.Locators.locators import LoginPageLoc
from PageObjectModel.Wordpress.Pages.BasePage import BasePage

# from selenium import webdriver

class LoginPage(BasePage):

    def do_login(self, username, password, remember_me_chk=False):
        username_field = self.driver.find_element(*LoginPageLoc.username_field)
        password_field = self.driver.find_element(*LoginPageLoc.password_field)
        login_button = self.driver.find_element(*LoginPageLoc.login_button)

        username_field.clear()
        username_field.send_keys(username)

        password_field.clear()
        password_field.send_keys(password)

        if remember_me_chk == True:
            self.driver.find_element(*LoginPageLoc.remeber_me_chk).click()

        login_button.click()

    def go_to(self):
        self.driver.get(LoginPageLoc.login_page_url)