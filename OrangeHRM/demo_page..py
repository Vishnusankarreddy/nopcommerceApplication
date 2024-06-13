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

    BOOK_FREE_DEMO = (By.XPATH, "//a[contains(text(),'Book a Free Demo')][1]")
    FULL_NAME = (By.XPATH, "//input[@id='Form_getForm_FullName']")
    EMAIL = (By.XPATH, "//input[@id='Form_getForm_Email']")
    COMPANY_NAME = (By.XPATH, "//input[@id='Form_getForm_CompanyName']")
    COUNTRY = (By.XPATH, "//select[@id='Form_getForm_Country']")
    INDIA = (By.XPATH, "//option[@value='India']")
    CONTACT = (By.XPATH, "//input[@id='Form_getForm_Contact']")
    SUBMIT = (By.XPATH, "//input[@id='Form_getForm_action_submitForm']")

    def book_free_demo(self, full_name, email, company_name, contact):
        self.click_element(*self.BOOK_FREE_DEMO)
        self.send_keys(*self.FULL_NAME, full_name)
        self.send_keys(*self.EMAIL, email)
        self.send_keys(*self.COMPANY_NAME, company_name)
        self.click_element(*self.COUNTRY)
        self.click_element(*self.INDIA)
        self.send_keys(*self.CONTACT, contact)
        self.click_element(*self.SUBMIT)