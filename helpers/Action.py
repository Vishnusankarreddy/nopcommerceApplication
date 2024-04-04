from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver

from basePackage.BasePo import driver, BasePo
from helpers.DataRroviders import DataProviders


class ActionUtils():
    @staticmethod
    def double_click_element(driver, locator):
        element = driver.find_element(*locator)
        actions = ActionChains(driver)
        actions.double_click(element).perform()

# Instantiate WebDriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.orangehrm.com/")

# Define locators
email_input_locator = (By.XPATH, "//input[@id='Form_submitForm_EmailHomePage']")
submit_button_locator = (By.XPATH, "//input[@id='Form_submitForm_action_request']")
double_click_locator = (By.XPATH, "//input[@id='Form_getForm_action_submitForm']")

# Perform actions
driver.find_element(*email_input_locator).send_keys("vishnusankar.reddy@softsuave.com")
driver.find_element(*submit_button_locator).click()
ActionUtils.double_click_element(driver, double_click_locator)

# Quit the WebDriver
driver.quit()