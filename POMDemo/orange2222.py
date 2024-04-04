from selenium.webdriver.common.by import By
from selenium import webdriver

class ElementUtils:
    @staticmethod
    def is_element_displayed(driver, locator):
        try:
            return driver.find_element(*locator).is_displayed()
        except NoSuchElementException:
            return False

# Instantiate WebDriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.orangehrm.com/")

# Define locators
solutions_locator = (By.XPATH, "//a[text()='Solutions']")
why_orangehrm_locator = (By.XPATH, "//a[text()='Why OrangeHRM']")
resources_locator = (By.XPATH, "//a[text()='Resources']")
company_locator = (By.XPATH, "//a[text()='Company']")

# Check if elements are displayed
solutions_displayed = ElementUtils.is_element_displayed(driver, solutions_locator)
why_orangehrm_displayed = ElementUtils.is_element_displayed(driver, why_orangehrm_locator)
resources_displayed = ElementUtils.is_element_displayed(driver, resources_locator)
company_displayed = ElementUtils.is_element_displayed(driver, company_locator)

# Use the displayed variables as needed
print("Solutions displayed:", solutions_displayed)
print("Why OrangeHRM displayed:", why_orangehrm_displayed)
print("Resources displayed:", resources_displayed)
print("Company displayed:", company_displayed)

# Quit the WebDriver
driver.quit()
