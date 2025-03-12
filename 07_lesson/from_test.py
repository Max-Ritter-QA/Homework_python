import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from Page_Object.FromPage import FromPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

def test_form():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    page = FromPage(browser)
    page.enter_from()
    red = page.search_red()
    green = page.search_green()

    assert red == "alert py-2 alert-danger"
    assert green == "alert py-2 alert-success"

    browser.quit()
