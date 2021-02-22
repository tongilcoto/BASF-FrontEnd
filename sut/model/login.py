from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import json


class QK_Login:

    def __init__(self):
        """
        Initialises LogIn page model. It creates the selenium webdriver object and loads the selectors configuration file
        """
        self.driver = webdriver.Chrome()
        self.driver.get('https://qknows-qa.basf.com')
        self.wait = WebDriverWait(self.driver, 10)
        self.selectors = json.load(open('sut/selectors/login.json'))

    def set_user_credentials(self):
        """
        Enters user crendentials, i.e. username and password, into the log in page
        It retrieves the values from system environment in order to provide a security layer
        """

        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.selectors['input_username_css'])))

        self.driver.find_element_by_css_selector(self.selectors['input_username_css'])\
            .send_keys(os.environ.get('QKNOWS_USER'))
        self.driver.find_element_by_css_selector(self.selectors['input_password_css'])\
            .send_keys(os.environ.get('QKNOWS_PASSWORD'))

    def login(self):
        """
        Clicks on Log In button at log in page.
        :return: The current selenium driver object in order to be managed by the next page
        """

        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.selectors['button_login_css'])))

        self.driver.find_element_by_css_selector(self.selectors['button_login_css']).click()
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