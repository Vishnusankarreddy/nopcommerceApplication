import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class NoSuchElementException(Exception):
    pass


driver = webdriver.Chrome()
action_chains = ActionChains(driver)
driver.maximize_window()
driver.get("https://www.orangehrm.com/")

try:
    driver.find_element(By.ID, "Form_submitForm_EmailHomePage").send_keys("vishnusankarr.reddy@softsuave.com")
    time.sleep(2)
    driver.find_element(By.ID, "Form_submitForm_action_request").click()
    time.sleep(2)

    aa = driver.find_element(By.XPATH, "//input[@value='Get Your Free Trial']")
    action_chains.double_click(aa).perform()
    time.sleep(5)

    cc = driver.find_element(By.ID, "Form_getForm_Email")
    bb = driver.find_element(By.XPATH, "//span[text()='You must supply a valid name for the trial.']")

    assert bb.is_displayed(), "Error message element is not displayed"
    assert cc.is_displayed(), "Email input element is not displayed"
    print("All elements are displayed")

except NoSuchElementException:
    print("Element not found")

finally:
    driver.quit()
