"""
This file will contain duckduckgo result page.
The page object for the page is the DuckDuckGo result page.
"""


class DuckDuckGoResultPage:
    def __init__(self, browser):
        self.browser = browser

    def search_input(self):
        return self.browser.find_element_by_id('search_form_input_homepage')

    def result_link_titles(self):
        return self.browser.find_elements_by_css_selector('.result__title')

    def title(self):
        pass
