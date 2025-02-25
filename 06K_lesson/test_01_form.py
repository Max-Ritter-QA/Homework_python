import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

def test_1_form(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.find_element(By.CSS_SELECTOR, "[name='first-name']").send_keys("Иван")
    driver.find_element(By.CSS_SELECTOR, "[name='last-name']").send_keys("Петров")
    driver.find_element(By.CSS_SELECTOR, "[name='address']").send_keys("Ленина, 55-3")
    driver.find_element(By.CSS_SELECTOR, "[name='e-mail']").send_keys("test@skypro.com")
    driver.find_element(By.CSS_SELECTOR, "[name='phone']").send_keys("+7985899998787")
    driver.find_element(By.CSS_SELECTOR, "[name='zip-code']").send_keys("")
    driver.find_element(By.CSS_SELECTOR, "[name='city']").send_keys("Москва")
    driver.find_element(By.CSS_SELECTOR, "[name='country']").send_keys("Россия")
    driver.find_element(By.CSS_SELECTOR, "[name='job-position']").send_keys("QA")
    driver.find_element(By.CSS_SELECTOR, "[name='company']").send_keys("SkyPro")
    driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

# проверка поля подсвеченного красным
    red = driver.find_element(By.CSS_SELECTOR, "#zip-code").get_attribute("class")
    assert red == "alert py-2 alert-danger"

# проверка полей подсвеченых зеленым
    name = driver.find_element(By.CSS_SELECTOR, "#first-name")
    last_name = driver.find_element(By.CSS_SELECTOR, "#last-name")
    address = driver.find_element(By.CSS_SELECTOR, "#address")
    email = driver.find_element(By.CSS_SELECTOR, "#e-mail")
    phone = driver.find_element(By.CSS_SELECTOR, "#phone")
    city = driver.find_element(By.CSS_SELECTOR, "#city")
    country = driver.find_element(By.CSS_SELECTOR, "#country")
    job =  driver.find_element(By.CSS_SELECTOR, "#job-position")
    company = driver.find_element(By.CSS_SELECTOR, "#company")

    fields = [name,last_name, address, email, phone, city, country, job, company]
    for field in fields:
        green = field.get_attribute("class")

    assert green == "alert py-2 alert-success"

    driver.quit()
