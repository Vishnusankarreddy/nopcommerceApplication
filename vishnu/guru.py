import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.instagram.com/")
driver.find_element(By.XPATH, "//input[@name='username']").send_keys("7032424667")
driver.find_element(By.XPATH, "//input[@type='password']").send_keys("mishareddy")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//span[text()='Explore']").click()
driver.find_element(By.XPATH, "//div[@class='_aagw']").click()
driver.close()