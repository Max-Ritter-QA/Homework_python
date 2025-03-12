from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FormaPage:
    def __init__(self, browser):
        self._driver = browser

    def forma(self):
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

    def total(self):
        waiter = WebDriverWait(self._driver, 40)
        waiter.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.summary_total_label"))
        )
        total = self._driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text
        return total

