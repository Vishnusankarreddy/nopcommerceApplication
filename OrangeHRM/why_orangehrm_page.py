# why_orangehrm_page.py
from selenium.webdriver.common.by import By
from base_page import BasePage


class WhyOrangeHRMPage(BasePage):
    OUR_CUSTOMERS_LINK = (By.XPATH, "//li[contains(text(),'Our Customers')]")
    CASE_STUDIES_LINK = (By.XPATH, "//a[text()='Case Studies']/parent::h6")

    def click_our_customers(self):
        self.click(*self.OUR_CUSTOMERS_LINK)

    def click_case_studies(self):
        self.click(*self.CASE_STUDIES_LINK)
