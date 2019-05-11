from PageObjectModel.Wordpress.Locators.locators import PostsPageLoc
from PageObjectModel.Wordpress.Locators.locators import BasePageLoc
from PageObjectModel.Wordpress.Pages.BasePage import BasePage
from PageObjectModel.Wordpress.Navigation.navigation import Posts
from selenium.webdriver.common.action_chains import ActionChains


class PostsPage(BasePage):
    def get_posts_count(self):
        posts_count = self.driver.find_element(*PostsPageLoc.posts_count).text
        a = list(posts_count)
        return int(a[0])

    def goto_published(self):
       self.driver.find_element(*PostsPageLoc.published_link).click()

    def delete_post(self, title):
        if not self.is_at():
            posts_nav = Posts(self.driver)
            posts_nav.goto_posts()

        actions = ActionChains(self.driver)
        post_title = self.driver.find_element_by_link_text(title)

        actions.move_to_element(post_title).perform()
        self.driver.find_element(*PostsPageLoc.move_to_trash_link).click()

    def search_post(self, title):
        if not self.is_at():
            posts_nav = Posts(self.driver)
            posts_nav.goto_posts()

        search_field = self.driver.find_element(*PostsPageLoc.post_search_field)
        search_field.click()
        search_field.send_keys(title)
        self.driver.find_element(*PostsPageLoc.post_search_button).click()

    def is_at(self):
        return self.driver.find_element(*BasePageLoc.header).text == "Posts"