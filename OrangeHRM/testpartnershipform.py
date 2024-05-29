import pytest
from selenium import webdriver
from OrangeHRM.home_page import HomePage
from OrangeHRM.partner_page import PartnersPage
class TestOrangeHRM:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def teardown_method(self):
        self.driver.quit()

    def test_case_studies(self):
        self.driver.get("https://www.orangehrm.com/")
        home_page = HomePage(self.driver)
        partners_page = PartnersPage(self.driver)  # Instantiate the class

        home_page.click_why_orangehrm()
        partners_page.navigate_to_partners()
        partners_page.fill_partnership_form(
            "aswain", "8899774455", "guru@gmail.com", "maxmium", "India", "Referral partnership", "hello orangeHRM this for testing purpose"
        )
