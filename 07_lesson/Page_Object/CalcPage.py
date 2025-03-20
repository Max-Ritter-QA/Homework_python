from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalcPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        WebDriverWait(driver, 40).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#delay")))
        self._driver.maximize_window()

    def test_calc(self, delay, number_one, operation, number_two, result):
        delay_input = self._driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(f"{delay}")
        self._driver.find_element(By.XPATH, f"//span[text()='{number_one}']").click()
        self._driver.find_element(By.XPATH, f"//span[text()='{operation}']").click()
        self._driver.find_element(By.XPATH, f"//span[text()='{number_two}']").click()
        self._driver.find_element(By.XPATH, "//span[text()='=']").click()
        WebDriverWait(self._driver, delay + 1).until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, ".screen"), str(result)))

    def result(self):
        res = self._driver.find_element(By.CSS_SELECTOR, ".screen").text
        return res
