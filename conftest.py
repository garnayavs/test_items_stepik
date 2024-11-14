import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default='ru',
                     help="Choose language: ru, en, es, fr, etc.")
    

@pytest.fixture()
def browser(request):
    user_language = request.config.getoption("--language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()



