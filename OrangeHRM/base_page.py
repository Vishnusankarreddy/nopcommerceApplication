# OrangeHRM/pages/base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, by, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, value)))

    def click(self, by, value):
        self.wait_for_element(by, value).click()

    def send_keys(self, by, value, text):
        self.wait_for_element(by, value).send_keys(text)

    def hover_over_element(self, by, value):
        element = self.wait_for_element(by, value)
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    def find_element(self, by, value):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by, value)))

    def click_element(self, by, value):
        element = self.find_element(by, value)
        element.click()

    def send_keys(self, by, value, keys):
        element = self.find_element(by, value)
        element.send_keys(keys)