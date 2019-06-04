from PageObjectModel.Wordpress.Locators.locators import PagesPageLoc
from PageObjectModel.Wordpress.Pages.BasePage import BasePage
from PageObjectModel.Wordpress.Tools.UIObject import UIObject

class PagesPage(BasePage):
    def click_on_page_title(self):
        page_title = UIObject(*PagesPageLoc.sample_page).click()