from PageObjectModel.Wordpress.Locators.locators import DashboardPageLoc
from PageObjectModel.Wordpress.Pages.BasePage import BasePage
from PageObjectModel.Wordpress.Tools.UIObject import UIObject
from selenium.webdriver.common.action_chains import ActionChains

class DashboardPage(BasePage):

    def do_logout(self):
        profile_tab = UIObject(*DashboardPageLoc.profile_tab)
        profile_tab.mouse_over()

        logout_link = UIObject(*DashboardPageLoc.logout)
        logout_link.click()