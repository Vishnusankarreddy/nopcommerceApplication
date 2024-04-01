import time

from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.orangehrm.com/")
driver.find_element(By.XPATH, "//a[text()='Solutions']").is_displayed()
driver.find_element(By.XPATH, "//a[text()='Why OrangeHRM']").is_displayed()
driver.find_element(By.XPATH, "//a[text()='Resources']").is_displayed()
driver.find_element(By.XPATH, "//a[text()='Company']").is_displayed()
driver.find_element(By.XPATH, "//div[@class='d-flex web-menu-btn']//button[text()='Book a Free Demo']").click()
driver.find_element(By.XPATH, "//input[@id='Form_getForm_FullName']").send_keys("vishnu")
driver.find_element(By.XPATH, "//input[@id='Form_getForm_action_submitForm']").click()
time.sleep(9)
driver.quit()




