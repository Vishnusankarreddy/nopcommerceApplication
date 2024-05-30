from selenium.webdriver.common.by import By
from .base_page import BasePage

class DemoPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.full_name = (By.XPATH, "//input[@id='Form_getForm_FullName']")
        self.email = (By.XPATH, "//input[@id='Form_getForm_Email']")
        self.company_name = (By.XPATH, "//input[@id='Form_getForm_CompanyName']")
        self.country = (By.XPATH, "//select[@id='Form_getForm_Country']")
        self.country_option = (By.XPATH, "//option[@value='India']")
        self.contact = (By.XPATH, "//input[@id='Form_getForm_Contact']")
        self.submit = (By.XPATH, "//input[@id='Form_getForm_action_submitForm']")

    def fill_demo_form(self, name, email, company, contact):
        self.send_keys_to_element(*self.full_name, name)
        self.send_keys_to_element(*self.email, email)
        self.send_keys_to_element(*self.company_name, company)
        self.click_element(*self.country)
        self.click_element(*self.country_option)
        self.send_keys_to_element(*self.contact, contact)
        self.click_element(*self.submit)
