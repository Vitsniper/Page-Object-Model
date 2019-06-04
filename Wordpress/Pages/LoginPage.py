from PageObjectModel.Wordpress.Locators.locators import LoginPageLoc
from PageObjectModel.Wordpress.Pages.BasePage import BasePage
from PageObjectModel.Wordpress.Tools.BrowserManager import Browser
from PageObjectModel.Wordpress.Tools.UIObject import UIObject

class LoginPage(BasePage):

    def do_login(self, username, password, remember_me_chk=False):
        username_field = UIObject(*LoginPageLoc.username_field)
        password_field = UIObject(*LoginPageLoc.password_field)
        login_button = UIObject(*LoginPageLoc.login_button)

        username_field.set_text(username)
        password_field.set_text(password)

        if remember_me_chk == True:
            UIObject(*LoginPageLoc.remeber_me_chk).click()
        login_button.click()

    def go_to(self):
        Browser.browser_instance.get(LoginPageLoc.login_page_url)