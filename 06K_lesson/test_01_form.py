from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

search_input_Fname = driver.find_element(By.CSS_SELECTOR, "[name='first-name']").send_keys("Иван")
search_input_Lname = driver.find_element(By.CSS_SELECTOR, "[name='last-name']").send_keys("Петров")
search_input_address = driver.find_element(By.CSS_SELECTOR, "[name='address']").send_keys("Ленина, 55-3")
search_input_email = driver.find_element(By.CSS_SELECTOR, "[name='e-mail']").send_keys("test@skypro.com")
search_input_phone = driver.find_element(By.CSS_SELECTOR, "[name='phone']").send_keys("+7985899998787")
search_input_zip = driver.find_element(By.CSS_SELECTOR, "[name='zip-code']").send_keys("")
search_input_city = driver.find_element(By.CSS_SELECTOR, "[name='city']").send_keys("Москва")
search_input_country = driver.find_element(By.CSS_SELECTOR, "[name='country']").send_keys("Россия")
search_input_job = driver.find_element(By.CSS_SELECTOR, "[name='job-position']").send_keys("QA")
search_input_company = driver.find_element(By.CSS_SELECTOR, "[name='company']").send_keys("SkyPro")

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
