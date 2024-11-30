"""
This file will contain shared fixtures
"""

import json
import pytest
import selenium.webdriver


@pytest.fixture
def config(scope='session'):

    # Load the configuration json file
    with open('../../config.json') as config_file:
        config = json.load(config_file)
        print(config)

    # Assert variables are Accepted
    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0
    # Return the configuration dictionary
    return config


@pytest.fixture
def browser(config):
    # Initialize the chromeDriver instance
    if config['browser'] == 'Firefox':
        b = selenium.webdriver.Firefox()
    elif config['browser'] == 'Chrome':
        b = selenium.webdriver.Chrome
    elif config['browser'] == 'Headless Chrome':
        options = selenium.webdriver.ChromeOptions()
        options.add_argument('--headless')
        b = selenium.webdriver.Chrome(options=options)
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')

    # Make its calls wait up to 10 seconds for elements to appear
    b.implicitly_wait(config['ImplicitWait'])

    # Return the webdriver instance for the setup
    yield b

    # Quit the webdriver instance for the cleanup
    b.quit()
