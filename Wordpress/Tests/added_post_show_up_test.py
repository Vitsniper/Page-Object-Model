from PageObjectModel.Wordpress.Tests.baseTest import BaseTest
from PageObjectModel.Wordpress.Navigation.navigation import Posts
from PageObjectModel.Wordpress.Pages.PostsPage import PostsPage
from PageObjectModel.Wordpress.Pages.AddNewPostPage import AddNewPostPage
from PageObjectModel.Wordpress.Tools.PostCreator import PostCreator

class PostTest(BaseTest):

    def test_added_post_show_up(self):
        driver = self.driver
        # go to All Posts page
        posts_nav = Posts(driver)
        posts_nav.goto_posts()

        # getting current posts count
        posts = PostsPage(driver)
        current_posts_count = posts.get_posts_count()

        #adding a new post
        post_creator = PostCreator(driver)
        post_creator.create_new_post()

        # go to All Posts page
        posts_nav.goto_posts()

        # check if posts count incremented
        updated_posts_count = posts.get_posts_count()
        self.assertEqual(current_posts_count + 1, updated_posts_count, "Posts count was not updated")

        # check if post was published
        self.assertIn(PostCreator.previous_title, driver.page_source, "Post was not published")