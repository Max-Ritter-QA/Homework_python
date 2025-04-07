from selenium import webdriver
from Page_Object.ShopPage import ShopPage
import allure

@allure.title("Тестирование функциональности магазина")
@allure.description("Тест проверяет корректность работы интернет-магазина.")
@allure.feature("Магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_calc():
    """Тест проверяет работу интернет-магазина."""
    browser = webdriver.Chrome()
    shop = ShopPage(browser)

    with allure.step("Открытие страницы интернет-магазина"):
        shop.open()

    with allure.step("Авторизация на сайте"):
        shop.avtorization()

    with allure.step("Добавление товара в корзину"):
        shop.cart()

    with allure.step("Заполнения формы на доставку"):
        shop.forma()

    with allure.step("Проверка результата"):
        total = shop.total()

    assert total == 'Total: $58.29'
    browser.quit()
