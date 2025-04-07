import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import allure

from Page_Object.FromPage import FromPage

@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.
    """
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Тестирование заполнения полей формы")
@allure.description("Тест проверяет корректность работы формы согласно ТЗ.")
@allure.feature("Поля")
@allure.severity(allure.severity_level.NORMAL)
def test_form():
    """
       Тест проверяет работу калькулятора с различными операциями."""

    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    page = FromPage(browser)

    with allure.step("Открытие страницы заполнения формы"):
        page.open()

    with allure.step("Заполнение полей формы согласно ТЗ"):
        page.enter_from()

    with allure.step("Поиск полей красного цвета"):
        red = page.search_red()

    with allure.step("Поиск полей зеленого цвета"):
        green = page.search_green()

    assert red == "alert py-2 alert-danger"
    assert green == "alert py-2 alert-success"

    browser.quit()
