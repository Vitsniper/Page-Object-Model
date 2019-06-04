import random
from PageObjectModel.Wordpress.Navigation.navigation import Posts
from PageObjectModel.Wordpress.Pages.AddNewPostPage import AddNewPostPage
from PageObjectModel.Wordpress.Pages.BasePage import BasePage
from PageObjectModel.Wordpress.Pages.PostsPage import PostsPage

# Dictionaries to generate title and body of the post
words = ["cat", "dog", "new", "post", "need", "speed", "creativity"]
articles = ["a", "the", "for", "to", "in", "as", "of", "from"]

class PostCreator(BasePage):
    previous_title = None
    previous_body = None

    def create_random_string(self):
        # generates string for title and body
        s = []
        for i in range(random.randint(2, len(words))):
            s.append(random.choice(words))
            s.append(" ")
            s.append(random.choice(articles))
            s.append(" ")
            s.append(random.choice(words))
            s.append(" ")
            return s

    @property
    def create_title(self):
        title = self.create_random_string()
        PostCreator.previous_title = "".join(title) + "title"
        return PostCreator.previous_title

    @property
    def create_body(self):
        body = self.create_random_string()
        PostCreator.previous_body = "".join(body) + "body"
        return PostCreator.previous_body

    def create_new_post(self):
        # go to Posts -> Add New page
        posts_nav = Posts(self.driver)
        posts_nav.add_new_click()

        # executing functions to have strings
        self.create_title
        self.create_body

        # creating new post with generated title and body
        add_new = AddNewPostPage(self.driver)
        add_new.add_new_post(PostCreator.previous_title, PostCreator.previous_body)

    def trash_post(self):
        if PostCreator.previous_title != None:
            posts_page = PostsPage(self.driver)
            posts_page.delete_post(PostCreator.previous_title)