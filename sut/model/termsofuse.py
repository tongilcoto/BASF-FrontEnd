import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class QK_TermsOfUse:

    def __init__(self, driver):
        """
        Initialises Terms Of Use popup model. It retrieves the current selenium webdriver object
        by parameter and sets its own variable. It also loads the selectors configuration file
        :param driver: current selenium webdriver object
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.selectors = json.load(open('sut/selectors/terms_of_use.json'))

    def is_terms_of_use_present(self):
        """
        Verifies if the Terms Of Use popup is present by just checking popup window title
        :return: boolean True- Pop Up is present. False- Pop Up is not present
        """
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.selectors['title_css'])))

        return self.driver.find_element_by_css_selector(self.selectors['title_css']) != ''

    def accept_terms_of_use(self):
        """
        It clicks on Terms Of Use checkbox
        """
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.selectors['checkbox_terms_of_use_css'])))

        self.driver.find_element_by_css_selector(self.selectors['checkbox_terms_of_use_css']).click()

    def proceed(self):
        """
        It clicks on Proceed to QKnow button
        :return: The current selenium driver object in order to be managed by the next page
        """
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.selectors['button_proceed_css'])))

        self.driver.find_element_by_css_selector(self.selectors['button_proceed_css']).click()
        return self.driver

    def close(self):
        """
        Closes the selenium webdriver
        """
        self.driver.close()

    def save_screenshot(self, screenshot_name):
        """
        Saves the screenshot of current page
        :param screenshot_name: screenshot file name
        """
        self.driver.save_screenshot(screenshot_name)