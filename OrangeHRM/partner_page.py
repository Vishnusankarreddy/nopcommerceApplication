from selenium.webdriver.common.by import By
from .base_page import BasePage

class PartnersPage(BasePage):
    PARTNERS_LINK = (By.XPATH, "//li[contains(text(),'Partners')]")
    OUR_PARTNERS_LINK = (By.XPATH, "//a[text()='Our Partners']/parent::h6")
    BECOME_PARTNER_LINK = (By.XPATH, "//a[contains(text(),'Become a Partner')]")
    NAME_FIELD = (By.ID, "Form_getForm_Name")
    CONTACT_FIELD = (By.ID, "Form_getForm_Contact")
    EMAIL_FIELD = (By.ID, "Form_getForm_Email")
    COMPANY_NAME_FIELD = (By.ID, "Form_getForm_CompanyName")
    COUNTRY_DROPDOWN = (By.ID, "Form_getForm_Country")
    PARTNERSHIP_TYPE_DROPDOWN = (By.ID, "Form_getForm_PartnershipType")
    COMMENT_FIELD = (By.ID, "Form_getForm_Comment")

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_partners(self):
        self.click(self.PARTNERS_LINK)
        self.click(self.OUR_PARTNERS_LINK)
        self.click(self.BECOME_PARTNER_LINK)

    def fill_partnership_form(self, name, contact, email, company_name, country, partnership_type, comment):
        self.send_keys(self.NAME_FIELD, name)
        self.send_keys(self.CONTACT_FIELD, contact)
        self.send_keys(self.EMAIL_FIELD, email)
        self.send_keys(self.COMPANY_NAME_FIELD, company_name)
        self.select_by_visible_text(self.COUNTRY_DROPDOWN, country)
        self.select_by_visible_text(self.PARTNERSHIP_TYPE_DROPDOWN, partnership_type)
        self.send_keys(self.COMMENT_FIELD, comment)
