from PageObjectModel.Wordpress.Pages.PagesPage import PagesPage
from PageObjectModel.Wordpress.Navigation.navigation import Pages
from PageObjectModel.Wordpress.Tests.baseTest import BaseTest

class PageTest(BaseTest):

    def test_page(self):
        driver = self.driver

        pages = Pages(driver)
        pages.goto_pages()

        pages_page = PagesPage(driver)
        pages_page.click_on_page_title()
        self.assertEqual("Sample Page", driver.find_element_by_id("post-title-0").text, "Wrong page loaded")