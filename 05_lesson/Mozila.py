from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/entry_ad")
sleep(3)

button_1 = driver.find_element(By.CSS_SELECTOR, "div.modal-footer")
button_1.click()

