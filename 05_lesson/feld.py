from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/inputs")
search_input = driver.find_element(By.CSS_SELECTOR, "[type='number']")
search_input.send_keys("1000")
search_input.clear()
search_input.send_keys("999")
