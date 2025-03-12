import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from Page_Object.CalcPage import CalcPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

def test_calc():
    browser = webdriver.Chrome()
    calc = CalcPage(browser)
    result = 15
    calc.test_calc(45, 7, "+", 8, result)
    res =  calc.result()

    assert res == str(result)
    browser.quit()
