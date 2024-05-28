from selenium.webdriver.common.by import By

from OrangeHRM.base_page import BasePage


class BecomePartnerPage(BasePage):
    NAME_INPUT = (By.ID, "Form_getForm_Name")
    CONTACT_INPUT = (By.ID, "Form_getForm_Contact")
    EMAIL_INPUT = (By.ID, "Form_getForm_Email")
    COMPANY_NAME_INPUT = (By.ID, "Form_getForm_CompanyName")
    COUNTRY_SELECT = (By.ID, "Form_getForm_Country")
    PARTNERSHIP_TYPE_SELECT = (By.ID, "Form_getForm_PartnershipType")
    COMMENT_TEXTAREA = (By.ID, "Form_getForm_Comment")

    def __init__(self, driver):
        super().__init__(driver)

    def fill_form(self, name, contact, email, company_name, country, partnership_type, comment):
        self.send_keys(self.NAME_INPUT, name)
        self.send_keys(self.CONTACT_INPUT, contact)
        self.send_keys(self.EMAIL_INPUT, email)
        self.send_keys(self.COMPANY_NAME_INPUT, company_name)
        self.select_by_value(self.COUNTRY_SELECT, country)
        self.select_by_value(self.PARTNERSHIP_TYPE_SELECT, partnership_type)
        self.send_keys(self.COMMENT_TEXTAREA, comment)

