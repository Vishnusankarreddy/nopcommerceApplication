from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    WHY_ORANGEHRM_LINK = (By.XPATH, "//a[text()='Why OrangeHRM?']")

    def __init__(self, driver):
        super().__init__(driver)

    def click_why_orangehrm(self):
        self.click(self.WHY_ORANGEHRM_LINK)
