from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class FromPage:
    def __init__(self, browser):
        """Конструктор класса FromPage.
           :param browser: WebDriver — объект драйвера Selenium.
        """
        self._driver = browser
        self.wait = WebDriverWait(browser, 2)

    @allure.step("Открытие сайта")
    def open(self):
        """ Открывает страницу запонения формы.
            :rtype: object"""
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.implicitly_wait(1)
        self._driver.maximize_window()

    @allure.step("Заполнение полей")
    def enter_from(self):
        """ Зполняет форму согласно ТЗ."""
        self._driver.find_element(By.CSS_SELECTOR, "[name='first-name']").send_keys("Иван")
        self._driver.find_element(By.CSS_SELECTOR, "[name='last-name']").send_keys("Петров")
        self._driver.find_element(By.CSS_SELECTOR, "[name='address']").send_keys("Ленина, 55-3")
        self._driver.find_element(By.CSS_SELECTOR, "[name='e-mail']").send_keys("test@skypro.com")
        self._driver.find_element(By.CSS_SELECTOR, "[name='phone']").send_keys("+7985899998787")
        self._driver.find_element(By.CSS_SELECTOR, "[name='zip-code']").send_keys("")
        self._driver.find_element(By.CSS_SELECTOR, "[name='city']").send_keys("Москва")
        self._driver.find_element(By.CSS_SELECTOR, "[name='country']").send_keys("Россия")
        self._driver.find_element(By.CSS_SELECTOR, "[name='job-position']").send_keys("QA")
        self._driver.find_element(By.CSS_SELECTOR, "[name='company']").send_keys("SkyPro")
        self._driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    @allure.step("Поиск полей красного цвета и получение результата")
    def search_red(self):
        """Ищет поля красного цвета
           Возвращает результат.
           :return: str — текст цвета результата."""
        color = self._driver.find_element(By.CSS_SELECTOR, "#zip-code").get_attribute("class")
        return color

    @allure.step("Поиск полей зеленого цвета и получение результата")
    def search_green(self):
        """Ищет поля зеленого цвета
           Возвращает результат.
           :return: str — текст цвета результата."""
        name = self._driver.find_element(By.CSS_SELECTOR, "#first-name")
        last_name = self._driver.find_element(By.CSS_SELECTOR, "#last-name")
        address = self._driver.find_element(By.CSS_SELECTOR, "#address")
        email = self._driver.find_element(By.CSS_SELECTOR, "#e-mail")
        phone = self._driver.find_element(By.CSS_SELECTOR, "#phone")
        city = self._driver.find_element(By.CSS_SELECTOR, "#city")
        country = self._driver.find_element(By.CSS_SELECTOR, "#country")
        job = self._driver.find_element(By.CSS_SELECTOR, "#job-position")
        company = self._driver.find_element(By.CSS_SELECTOR, "#company")

        fields = [name,last_name, address, email, phone, city, country, job, company]
        for field in fields:
            color_2 = field.get_attribute("class")
            return color_2
