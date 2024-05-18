
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.orangehrm.com/")



def assert_element_displayed(by, value):
    try:
        assert driver.find_element(by, value).is_displayed(), f"Element {by}={value} is not displayed"
    except NoSuchElementException:
        assert False, f"Element {by}={value} not found on the page"


assert_element_displayed(By.XPATH, "//a[text()='Solutions']")
assert_element_displayed(By.XPATH, "//a[text()='Why OrangeHRM']")
assert_element_displayed(By.XPATH, "//a[text()='Resources']")
assert_element_displayed(By.XPATH, "//a[text()='Company']")

print("All assertions passed successfully.")

driver.quit()