from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")
search_input = driver.find_element(By.CSS_SELECTOR, "input#username")
search_input.send_keys("tomsmith")
search_input_2 = driver.find_element(By.CSS_SELECTOR, "input#password")
search_input_2.send_keys("SuperSecretPassword!")
search_input_3 = driver.find_element(By.CSS_SELECTOR, ".radius")
search_input_3.click()
