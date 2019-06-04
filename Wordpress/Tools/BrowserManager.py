import pickle
import pprint as pp

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


class Browser:

    CHROME = 1
    FF = 2
    PHANTOM = 3
    IE = 4
    OPERA = 5

    browser_instance = None
    cookies_location = "C:\\Users\\Vitalik\\PycharmProjects\\Selenium\\" \
                       "venv\\PageObjectModel\\Wordpress\\Tools\\cookies.txt"

    @staticmethod
    def create_new_driver(driver_id):
        def set_driver():
            if Browser.PHANTOM == driver_id:
                Browser.browser_instance = webdriver.PhantomJS()

            elif Browser.CHROME == driver_id:
                chrome_options = Options()
                chrome_options.add_argument("--headless")
                # Browser.browser_instance = webdriver.Chrome(options=chrome_options)
                Browser.browser_instance = webdriver.Chrome()

            elif Browser.FF == driver_id:
                Browser.browser_instance = webdriver.Firefox()

            elif Browser.OPERA == driver_id:
                Browser.browser_instance = webdriver.Opera()

            elif Browser.IE == driver_id:
                Browser.browser_instance = webdriver.Ie()
            else:
                raise Exception("There is no support for driver_id: {}".format(driver_id))
            return Browser.browser_instance

        Browser.browser_instance = set_driver()
        return Browser.browser_instance

    @staticmethod
    def forward():
        Browser.browser_instance.forward()

    @staticmethod
    def back():
        Browser.browser_instance.back()

    @staticmethod
    def open_new_tab():
        Browser.browser_instance.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')

    @staticmethod
    def quit():
        Browser.browser_instance.quit()

    @staticmethod
    def switch_to_window(window):
        Browser.browser_instance.switch_to_window(window)

    @staticmethod
    def switch_to_latest_active_window():
        windows = Browser.browser_instance.window_handles
        if len(windows) == 1:
            Browser.browser_instance.switch_to_window(windows[0])
            return
        for index in range(1, len(windows)):
            Browser.browser_instance.switch_to_window(windows[-index])
            return

    @staticmethod
    def close_current_active_window():
        windows = Browser.browser_instance.window_handles
        if len(windows) == 1:
            return
        for index in range(1, len(windows)):
            Browser.browser_instance.close()
            Browser.switch_to_latest_active_window()
            return

    @staticmethod
    def accept_alert():
        Browser.browser_instance.switch_to_alert().accept()

    @staticmethod
    def decline_alert():
        Browser.browser_instance.switch_to_alert.dismiss()

    @staticmethod
    def get_alert_text():
        Browser.browser_instance.switch_to_alert.text

    @staticmethod
    def save_cookies(cookies_location = Browser.cookies_location):
        pickle.dump(Browser.browser_instance.get_cookies(), open(cookies_location, "wb"))

    @staticmethod
    def load_cookies(cookies_location = Browser.cookies_location, url=None):
        cookies = pickle.load(open(cookies_location, "rb"))
        Browser.browser_instance.delete_all_cookies()
        # have to be on a page before you can add any cookies, any page - does not matter which
        Browser.browser_instance.get("https://google.com" if url is None else url)
        for cookie in cookies:
            Browser.browser_instance.add_cookie(cookie)

    @staticmethod
    def delete_cookies(domains=None):

        if domains is not None:
            cookies = Browser.browser_instance.get_cookies()
            original_len = len(cookies)
            for cookie in cookies:
                if str(cookie["domain"]) in domains:
                    cookies.remove(cookie)
            if len(cookies) < original_len:  # if cookies changed, we will update them
                # deleting everything and adding the modified cookie object
                Browser.browser_instance.delete_all_cookies()
                for cookie in cookies:
                    Browser.browser_instance.add_cookie(cookie)
        else:
            Browser.browser_instance.delete_all_cookies()
    #TODO: is_alert_displayed