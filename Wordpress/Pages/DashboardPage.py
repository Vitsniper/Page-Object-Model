from PageObjectModel.Wordpress.Locators.locators import DashboardPageLoc
from PageObjectModel.Wordpress.Pages.BasePage import BasePage
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium import webdriver

class DashboardPage(BasePage):
    # def __init__(self):
    #     self.driver = webdriver.Chrome()

    def do_logout(self):
        profile_tab = self.driver.find_element(*DashboardPageLoc.profile_tab)
        actions = ActionChains(self.driver)

        actions.move_to_element(profile_tab).perform()
        # self.driver.implicitly_wait(3)
        # logout = WebDriverWait(self.driver, 10).until\
        #     (EC.presence_of_element_located((By.XPATH, "//a[@class='ab-item'][contains(text(),'Log Out')]")))
        # logout.click()
        logout_link = self.driver.find_element(*DashboardPageLoc.logout)
        logout_link.click()