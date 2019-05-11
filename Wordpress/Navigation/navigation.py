from PageObjectModel.Wordpress.Locators.locators import NavigationLoc
from PageObjectModel.Wordpress.Pages.BasePage import BasePage

class Posts(BasePage):
    def goto_posts(self):
        MenuSelector.select(self, *NavigationLoc.posts, *NavigationLoc.all_posts)

    def add_new_click(self):
        MenuSelector.select(self, *NavigationLoc.posts, *NavigationLoc.add_new)

class Pages(BasePage):
    def goto_pages(self):
        MenuSelector.select(self, *NavigationLoc.pages, *NavigationLoc.all_pages)

class MenuSelector(BasePage):
    def select(self, method1, top_level_menu_id, method2, sub_menu_link_text):

        # selecting corresponding page from left navigation menu
        self.top_level_menu_id = top_level_menu_id
        self.sub_menu_link_text = sub_menu_link_text
        self.method1 = method1
        self.method2 = method2

        self.driver.find_element_by_id(top_level_menu_id).click()
        self.driver.find_element_by_link_text(sub_menu_link_text).click()
