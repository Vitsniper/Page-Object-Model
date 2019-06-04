from PageObjectModel.Wordpress.Locators.locators import PostsPageLoc
from PageObjectModel.Wordpress.Locators.locators import BasePageLoc
from PageObjectModel.Wordpress.Pages.BasePage import BasePage
from PageObjectModel.Wordpress.Navigation.navigation import Posts
from PageObjectModel.Wordpress.Tools.UIObject import UIObject
from selenium.webdriver.common.by import By


class PostsPage(BasePage):
    def get_posts_count(self):
        posts_count = UIObject(*PostsPageLoc.posts_count).get_text()
        a = list(posts_count)
        return int(a[0])

    def goto_published(self):
       UIObject(*PostsPageLoc.published_link).click()

    def delete_post(self, title):
        if not self.is_at():
            posts_nav = Posts(self.driver)
            posts_nav.goto_posts()

        post_title = UIObject(By.LINK_TEXT, title)
        post_title.mouse_over()

        UIObject(*PostsPageLoc.move_to_trash_link).click()

    def search_post(self, title):
        if not self.is_at():
            posts_nav = Posts(self.driver)
            posts_nav.goto_posts()

        search_field = UIObject(*PostsPageLoc.post_search_field)
        search_field.click()
        search_field.type_text(title)
        UIObject(*PostsPageLoc.post_search_button).click()

    def is_at(self):
        return UIObject(*BasePageLoc.header).get_text() == "Posts"