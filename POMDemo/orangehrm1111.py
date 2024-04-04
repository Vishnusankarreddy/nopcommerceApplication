import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.orangehrm.com/")

# driver.find_element(By.XPATH, "//a[text()='Solutions']").is_displayed()
# driver.find_element(By.XPATH, "//a[text()='Why OrangeHRM']").is_displayed()
# driver.find_element(By.XPATH, "//a[text()='Resources']").is_displayed()
# driver.find_element(By.XPATH, "//a[text()='Company']").is_displayed()
driver.find_element(By.XPATH, "//input[@id='Form_submitForm_EmailHomePage']").send_keys("vishnusankar.reddy@softsuave.com")
driver.find_element(By.XPATH, "//input[@id='Form_submitForm_action_request']").click()
doubleclick = driver.find_element(By.XPATH, "//input[@id='Form_getForm_action_submitForm']")
actions = ActionChains(driver)
actions.double_click(doubleclick).perform()
# time.sleep(9)
# driver.quit()