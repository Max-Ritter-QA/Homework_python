import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

def test_shop(driver):
    waiter = WebDriverWait(driver, 40)
    driver.get("https://www.saucedemo.com/")

    search_input_username = driver.find_element(By.CSS_SELECTOR, "#user-name")
    search_input_username.clear()
    search_input_username.send_keys("standard_user")

    search_input_password = driver.find_element(By.CSS_SELECTOR, "#password")
    search_input_password.clear()
    search_input_password.send_keys("secret_sauce")

    driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    waiter.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack"))
    ).click()

    waiter.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt"))
    ).click()

    waiter.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie"))
    ).click()

    driver.find_element(By.CSS_SELECTOR, "[data-test='shopping-cart-link']").click()

    waiter.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#checkout"))
    ).click()

    waiter.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#first-name"))
    ).send_keys("Max")

    waiter.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#last-name"))
    ).send_keys("Ivanov")

    waiter.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#postal-code"))
    ).send_keys("356773")

    driver.find_element(By.CSS_SELECTOR, "#continue").click()

    waiter.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div.summary_total_label"))
    )

    total= driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text

    print(total)

    driver.quit()

    assert total == 'Total: $58.29'
