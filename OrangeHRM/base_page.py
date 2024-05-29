from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Increased timeout to 20 seconds

    def click(self, by_locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(by_locator))
            element.click()
        except TimeoutException:
            print(f"TimeoutException: Could not click on the element with locator {by_locator}")

    def send_keys(self, by_locator, text):
        try:
            element = self.wait.until(EC.visibility_of_element_located(by_locator))
            element.send_keys(text)
        except TimeoutException:
            print(f"TimeoutException: Could not find the element with locator {by_locator} to send keys")

    def select_by_visible_text(self, by_locator, text):
        try:
            element = self.wait.until(EC.visibility_of_element_located(by_locator))
            select = Select(element)
            select.select_by_visible_text(text)
        except TimeoutException:
            print(f"TimeoutException: Could not find the element with locator {by_locator} to select by visible text")
