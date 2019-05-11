from PageObjectModel.Wordpress.Locators.locators import PagesPageLoc
from PageObjectModel.Wordpress.Pages.BasePage import BasePage

class PagesPage(BasePage):
    def click_on_page_title(self):
        page_title = self.driver.find_element(*PagesPageLoc.sample_page).click()