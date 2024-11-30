"""
These tests cover DuckDuckGo searches.
"""
from Learning_Courses.Selenium_web.pages.result import DuckDuckGoResultPage
from Learning_Courses.Selenium_web.pages.search import DuckDuckGoSearchPage
from selenium.webdriver.support.ui import WebDriverWait


def test_basic_duckduckgo_search(browser):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)
    phrase = 'panda'

    # Given the DuckDuckGo home page is displayed
    search_page.load()

    # When the user searches for "panda"
    search_page.search(phrase)

    # Then the search result query is "panda"
    assert phrase == result_page.search_input_value()

    # And the search result links pertain to "panda"
    titles = result_page.result_link_titles()
    matches = [t for t in titles if PHRASE.lower() in t.lower()]
    assert len(matches) > 0

    # And the search result title contains "panda"
    assert phrase in result_page.title()