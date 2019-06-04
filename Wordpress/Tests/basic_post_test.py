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