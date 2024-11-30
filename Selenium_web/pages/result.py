"""
This file will contain duckduckgo result page.
The page object for the page is the DuckDuckGo result page.
"""

from selenium.webdriver.common.by import By


class DuckDuckGoResultPage:
    # Locators
    RESULT_LINKS = (By.CSS_SELECTOR, 'a.result__a')
    SEARCH_INPUT = (By.ID, 'search_form_input')

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods
    def result_link_titles(self):
        links = self.browser.find_elements(*self.RESULT_LINKS)
        links = [link.text for link in links]
        return links

    def search_input(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        values = search_input.get_attribute('value')
        return values

    def title(self):
        return self.browser.title
