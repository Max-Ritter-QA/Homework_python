import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    browser.quit()

@pytest.mark.parametrize("delay, number_one, operation, number_two, result", [
    (45, 7, "+", 8, 15),
    (3, 3, "-", 2, 1)
])
def test_calc(driver, delay, number_one, operation, number_two, result):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    WebDriverWait(driver, 40).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#delay")))

    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys(f"{delay}")

    driver.find_element(By.XPATH, f"//span[text()='{number_one}']").click()
    driver.find_element(By.XPATH, f"//span[text()='{operation}']").click()
    driver.find_element(By.XPATH, f"//span[text()='{number_two}']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    WebDriverWait(driver, delay+1).until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, ".screen"), str(result)))

    res = driver.find_element(By.CSS_SELECTOR, ".screen").text
    assert res == str(result)