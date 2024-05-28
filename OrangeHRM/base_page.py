# base_page.py
from telnetlib import EC

from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def click(self, *locator):
        self.find_element(*locator).click()

    def is_displayed(self, *locator):
        return self.find_element(*locator).is_displayed()

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, by_locator):
        element = self.wait.until(EC.element_to_be_clickable(by_locator))
        element.click()

    def send_keys(self, by_locator, text):
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        element.send_keys(text)

    def select_by_value(self, by_locator, value):
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        for option in element.find_elements_by_tag_name('option'):
            if option.get_attribute('value') == value:
                option.click()
                break

    def is_displayed(self, by_locator):
        try:
            self.wait.until(EC.visibility_of_element_located(by_locator))
            return True
        except:
            return False