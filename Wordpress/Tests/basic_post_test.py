from PageObjectModel.Wordpress.Pages.AddNewPostPage import AddNewPostPage
from PageObjectModel.Wordpress.Pages.PostsPage import PostsPage
from PageObjectModel.Wordpress.Navigation.navigation import Posts
from PageObjectModel.Wordpress.Tests.baseTest import BaseTest
from PageObjectModel.Wordpress.Tools.PostCreator import PostCreator

class PostTest(BaseTest):

    def test_basic_post_creation(self):
        driver = self.driver

        # adding new post
        post_creator = PostCreator(driver)
        post_creator.create_new_post()

        # check if post was published
        self.assertIn("Published", driver.page_source, "Post not published")