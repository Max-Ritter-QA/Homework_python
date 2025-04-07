from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class ShopPage:
    def __init__(self, driver):
        """Конструктор класса MainAvtorPage.
           :param driver: WebDriver — объект драйвера Selenium.
        """
        self._driver = driver

    @allure.step("Открытие сайта")
    def open(self):
        """ Открывает страницу запонения формы.
            :rtype: object"""
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(2)
        self._driver.maximize_window()

    @allure.step("Авторизация на сайте")
    def avtorization(self):
        """Авторизовывается на сайте, логин и пароль указан в ТЗ"""
        search_input_username = self._driver.find_element(By.CSS_SELECTOR, "#user-name")
        search_input_username.clear()
        search_input_username.send_keys("standard_user")

        search_input_password = self._driver.find_element(By.CSS_SELECTOR, "#password")
        search_input_password.clear()
        search_input_password.send_keys("secret_sauce")

        self._driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    @allure.step("Добавление товаров в корзину")
    def cart(self):
        """Добавляет товар в горзину согласно ТЗ"""
        waiter = WebDriverWait(self._driver, 40)
        waiter.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack"))
        ).click()

        waiter.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt"))
        ).click()

        waiter.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie"))
        ).click()

        self._driver.find_element(By.CSS_SELECTOR, "[data-test='shopping-cart-link']").click()

        waiter.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#checkout"))
        ).click()

    @allure.step("Заполнение полей формы на доставку")
    def forma(self):
        """Заполняет поля согласно ТЗ"""
        waiter = WebDriverWait(self._driver, 40)
        waiter.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#first-name"))
        ).send_keys("Max")

        waiter.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#last-name"))
        ).send_keys("Ivanov")

        waiter.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#postal-code"))
        ).send_keys("356773")

        self._driver.find_element(By.CSS_SELECTOR, "#continue").click()

    @allure.step("Получение результата стоимости корзины")
    def total(self):
        """Возвращает текущий результат стоимости товаров в корзине.
           :return: str — текст результата."""
        waiter = WebDriverWait(self._driver, 40)
        waiter.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.summary_total_label"))
        )
        total = self._driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text
        return total
