from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
waiter = WebDriverWait(driver, 40, 0.1)
driver.get("http://uitestingplayground.com/textinput")
search_input = driver.find_element(By.CSS_SELECTOR, "[type='text']")
search_input.send_keys("SkyPro")
driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()
waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#updatingButton"), "SkyPro")
)

button = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text

print(button)

driver.quit()
