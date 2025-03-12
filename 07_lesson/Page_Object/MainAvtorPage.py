from selenium.webdriver.common.by import By

class MainAvtorPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(2)
        self._driver.maximize_window()

    def avtorization(self):
        search_input_username = self._driver.find_element(By.CSS_SELECTOR, "#user-name")
        search_input_username.clear()
        search_input_username.send_keys("standard_user")

        search_input_password = self._driver.find_element(By.CSS_SELECTOR, "#password")
        search_input_password.clear()
        search_input_password.send_keys("secret_sauce")

        self._driver.find_element(By.CSS_SELECTOR, "#login-button").click()
