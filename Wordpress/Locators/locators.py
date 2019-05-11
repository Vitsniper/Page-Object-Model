from selenium.webdriver.common.by import By

class BasePageLoc():
    # common elements for pages
    header = (By.CLASS_NAME, "wp-heading-inline")

class LoginPageLoc():
    # Login Page objects
    username_field = (By.ID, "user_login")
    password_field = (By.ID, "user_pass")
    login_button = (By.ID, "wp-submit")
    remeber_me_chk = (By.ID, "rememberme")
    login_page_url = "http://localhost/wordpress/wp-login.php"

class PostsPageLoc():
    # Posts Page objects
    add_new_button = (By.XPATH, "//a[@class='page-title-action']")
    posts_count = (By.CLASS_NAME, "displaying-num")
    published_link = (By.PARTIAL_LINK_TEXT, "Publish")
    published_posts_title = (By.LINK_TEXT, "row-title")
    move_to_trash_link = (By.LINK_TEXT, "Move to Trash")
    post_search_field = (By.ID, "post-search-input")
    post_search_button = (By.ID, "search-submit")
    undo_link = (By.LINK_TEXT, "Undo")

class DashboardPageLoc():
    # Dashboard Page objects
    logout = (By.XPATH, "//a[@class='ab-item'][contains(text(),'Log Out')]")
    profile_tab = (By.PARTIAL_LINK_TEXT, "Howd")

class NavigationLoc():
    # Navigation objects
    posts = (By.ID, "menu-posts")
    all_posts = (By.LINK_TEXT, "All Posts")
    add_new = (By.LINK_TEXT, "Add New")
    pages = (By.ID, "menu-pages")
    all_pages = (By.LINK_TEXT, "All Pages")


class PagesPageLoc():
    # Pages Page objects
    sample_page = (By.LINK_TEXT, "Sample Page")

class AddNewPostPageLoc():
    # Add New Post Page objects
    post_title = (By.ID, "post-title-0")
    text_box = (By.XPATH, "//textarea[@class='editor-default-block-appender__content']")
    text_area = (By.XPATH, "//p[@id='mce_0']")
    publish_button = (By.XPATH, "//button[@class='components-button editor-post-publish-panel__toggle is-button is-primary']")
    publish_button_confirm = (By.XPATH, "//button[@class='"
                                        "components-button editor-post-publish-button is-button is-default is-primary is-large']")
    close_popup = (By.CLASS_NAME, "dashicon dashicons-no-alt")
    view_post_link = (By.XPATH, "//*[contains(text(), 'Post published')]")