"""
This file will contain duckduckgo searches page.
The page object for the page is the DuckDuckGo search page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class DuckDuckGoSearchPage:

    # URL
    URL = 'https://duckduckgo.com'

    # Locators
    SEARCH_INPUT = 'search_form_input_homepage'

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def search(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)
