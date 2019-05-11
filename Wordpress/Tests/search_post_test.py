from PageObjectModel.Wordpress.Tests.baseTest import BaseTest
from PageObjectModel.Wordpress.Navigation.navigation import Posts
from PageObjectModel.Wordpress.Pages.PostsPage import PostsPage
from PageObjectModel.Wordpress.Pages.AddNewPostPage import AddNewPostPage

from PageObjectModel.Wordpress.Tools.PostCreator import PostCreator

class PostTest(BaseTest):

    def test_can_search_post(self):
        driver = self.driver

        # go to Add New post page
        posts_nav = Posts(driver)
        posts_nav.add_new_click()

        # adding new post
        post_creator = PostCreator(driver)
        post_creator.create_new_post()

        # searching for post
        posts = PostsPage(driver)
        posts.search_post(PostCreator.previous_title)

        # verify that post is present in result
        self.assertIn(PostCreator.previous_title, driver.page_source, "Unable to find post")