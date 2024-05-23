# home_page.py
from selenium.webdriver.common.by import By

from OrangeHRM.base_page import BasePage


class HomePage(BasePage):
    SOLUTIONS_LINK = (By.XPATH, "//a[text()='Solutions']")
    WHY_ORANGEHRM_LINK = (By.XPATH, "//a[text()='Why OrangeHRM']")
    RESOURCES_LINK = (By.XPATH, "//a[text()='Resources']")
    COMPANY_LINK = (By.XPATH, "//a[text()='Company']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://www.orangehrm.com/")

    def verify_elements_displayed(self):
        assert self.is_displayed(*self.SOLUTIONS_LINK)
        assert self.is_displayed(*self.WHY_ORANGEHRM_LINK)
        assert self.is_displayed(*self.RESOURCES_LINK)
        assert self.is_displayed(*self.COMPANY_LINK)

    def click_why_orangehrm(self):
        self.click(*self.WHY_ORANGEHRM_LINK)

