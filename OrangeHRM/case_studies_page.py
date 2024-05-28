# case_studies_page.py
from selenium.webdriver.common.by import By

from OrangeHRM.base_page import BasePage


class CaseStudiesPage(BasePage):
    MASSY_DISTRIBUTION_TEXT = (By.XPATH, "//p[text()='Massy Distribution']")
    SATO_EUROPE_TEXT = (By.XPATH, "//p[normalize-space()='SATO Europe']")
    TLSCONTACT_TEXT = (By.XPATH, "//p[normalize-space()='TLScontact']")
    RUTGERS_UNIVERSITY_TEXT = (By.XPATH, "//p[normalize-space()='Rutgers University']")
    CARIATI_LAW_TEXT = (By.XPATH, "//p[normalize-space()='Cariati Law']")
    FOODCLOUD_TEXT = (By.XPATH, "//p[normalize-space()='FoodCloud']")
    HR_SOLUTIONS_GROUP_TEXT = (By.XPATH, "//p[normalize-space()='The Human Resources Solutions Group']")
    HYPERCORE_NETWORKS_TEXT = (By.XPATH, "//p[normalize-space()='Hypercore Networks']")

    def verify_case_studies_displayed(self):
        assert self.is_displayed(*self.MASSY_DISTRIBUTION_TEXT)
        assert self.is_displayed(*self.SATO_EUROPE_TEXT)
        assert self.is_displayed(*self.TLSCONTACT_TEXT)
        assert self.is_displayed(*self.RUTGERS_UNIVERSITY_TEXT)
        assert self.is_displayed(*self.CARIATI_LAW_TEXT)
        assert self.is_displayed(*self.FOODCLOUD_TEXT)
        assert self.is_displayed(*self.HR_SOLUTIONS_GROUP_TEXT)
        assert self.is_displayed(*self.HYPERCORE_NETWORKS_TEXT)