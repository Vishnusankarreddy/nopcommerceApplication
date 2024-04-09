from selenium.webdriver.common.by import By
from basePackage.BasePo import BasePo
from helpers.DataProviders import DataProviders
from helpers.Waiters import Waiters

class HomePage(BasePo):
    def __init__(self, driver):
        self.driver = driver

    def header_item(self, item_name):
        return By.LINK_TEXT, item_name

    def open_landing_page(self):
        url = DataProviders.orangeHRmURl
        self.driver.get(url)
    def get_current_url(self):
        return self.driver.current_url

    def click_on_header_menu_button(self, item_name):
        locator = self.header_item(item_name)
        Waiters.wait_for_element_to_be_displayed(locator)
        element = self.driver.find_element(*locator)
        element.click()
