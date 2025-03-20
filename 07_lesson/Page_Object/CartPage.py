from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, browser):
        self._driver = browser

    def cart(self):
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
