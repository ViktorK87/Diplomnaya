from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.fixture
def driver():
    browser = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

    browser.implicitly_wait(4) 
    browser.maximize_window()

    yield browser #Возврат браузера

    browser.quit()