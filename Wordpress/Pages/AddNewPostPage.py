from PageObjectModel.Wordpress.Locators.locators import AddNewPostPageLoc
from PageObjectModel.Wordpress.Pages.BasePage import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class AddNewPostPage(BasePage):

    def add_new_post(self, title="Default title", message = "Default message"):
        # filling the post title
        post_title = self.driver.find_element(*AddNewPostPageLoc.post_title)
        post_title.clear()
        post_title.send_keys(title)

        # clicking on text box to be able write post body
        text_box = self.driver.find_element(*AddNewPostPageLoc.text_box)
        text_box.click()

        # filling the post body
        text_area = self.driver.find_element(*AddNewPostPageLoc.text_area)
        text_area.clear()
        text_area.send_keys(message)

        # publishing the post and wait to be published
        self.driver.find_element(*AddNewPostPageLoc.publish_button).click()
        self.driver.find_element(*AddNewPostPageLoc.publish_button_confirm).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Post published')]")))