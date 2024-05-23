import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.orangehrm.com/")
driver.find_element(By.XPATH, "//a[text()='Solutions']").is_displayed()
driver.find_element(By.XPATH, "//a[text()='Why OrangeHRM']")
driver.find_element(By.XPATH, "//a[text()='Resources']")
driver.find_element(By.XPATH, "//a[text()='Company']")
driver.find_element(By.XPATH, "//a[text()='Why OrangeHRM']").click()
driver.find_element(By.XPATH, "//li[contains(text(),'Our Customers')]").click()
driver.find_element(By.XPATH, "//a[text()='Case Studies']/parent::h6").click()
driver.find_element(By.XPATH, "//p[text()='Massy Distribution']").is_displayed()
driver.find_element(By.XPATH, "//p[normalize-space()='SATO Europe']").is_displayed()
driver.find_element(By.XPATH, "//p[normalize-space()='TLScontact']").is_displayed()
driver.find_element(By.XPATH, "//p[normalize-space()='Rutgers University']").is_displayed()
driver.find_element(By.XPATH, "//p[normalize-space()='Cariati Law']").is_displayed()
driver.find_element(By.XPATH, "//p[normalize-space()='FoodCloud']").is_displayed()
driver.find_element(By.XPATH, "//p[normalize-space()='The Human Resources Solutions Group']").is_displayed()
driver.find_element(By.XPATH, "//p[normalize-space()='Hypercore Networks']").is_displayed()
time.sleep(5)
driver.quit()
