import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from hamcrest import assert_that, equal_to, contains_string


class QK_Main:

    def __init__(self, driver):
        """
        Initialises Main page model. It retrieves the current selenium webdriver object
        by parameter and sets its own variable. It also loads the selectors configuration file
        :param driver: current selenium webdriver object
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.selectors = json.load(open('sut/selectors/main.json'))

    def get_title_value(self):
        """
        Gets main page title value
        :return: string
        """
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.selectors['title_css'])))

        return self.driver.find_element_by_css_selector(self.selectors['title_css']).text

    def verify_field_visibility(self, field):
        """
        Verifies the visibility of a given field of the main page
        :param field: string
        :return: null|TimeoutException|AssertionError
        """
        selector_key = "_".join(field.split(' ')) + "_css"

        if selector_key in self.selectors.keys():
            try:
                self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.selectors[selector_key])))
            except TimeoutException:
                assert False
        else:
            print('Field "' + field + '" is not recognised')
            assert False

    def search_for_word(self, word):
        """
        Enters the word at search field and executes the query
        :param word: string, searching word
        """
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.selectors['search_field_css'])))
        self.driver.find_element_by_css_selector(self.selectors['search_field_css']).send_keys(word)
        self.driver.find_element_by_css_selector(self.selectors['search_magnifier_css']).click()

    def verify_searched_word_in_abstracts(self, word):
        """
        Verifies the word is present at the first 3 search results, at least at the abstract of the document
        :param word: string, Word to be searched at abstracts
        """
        self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, self.selectors['search_result_abstract_css'])
        ))
        print(f"Looking for ... {word}")
        for abstract in self.driver.find_elements_by_css_selector(self.selectors['search_result_abstract_css'])[:3]:
            abstract.location_once_scrolled_into_view
            assert_that(abstract.text, contains_string(word))

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

