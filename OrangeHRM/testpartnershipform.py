import pytest
from selenium import webdriver
from OrangeHRM.home_page import HomePage
from OrangeHRM.partners_page import PartnersPage
from demo_page import DemoPage
class TestOrangeHRM:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        request.cls.driver = driver
        yield driver
        driver.quit()

    def teardown_method(self):
        request.cls.driver = driver
        yield driver
        driver.quit()

    def test_case_studies(self):
        self.driver.get("https://www.orangehrm.com/")
        home_page = HomePage(self.driver)
        partners_page = PartnersPage(self.driver)

        home_page.click_why_orangehrm()
        partners_page.navigate_to_partners()
        partners_page.fill_partnership_form(
            "aswain", "8899774455", "guru@gmail.com", "maxmium", "India", "Referral partnership", "hello orangeHRM this for testing purpose"
        )

    def test_case_header(self):
        self.driver.get("https://www.orangehrm.com/")

        home_page = HomePage(self.driver)
        home_page.hover_over_header()
        home_page.hover_over_stakeholder()
        home_page.click_hr_manager()
        home_page.click_book_demo()

        demo_page = DemoPage(self.driver)
        demo_page.fill_demo_form(
            name="vishnureddy",
            email="bussiness99@gmail.com",
            company="goldfeild",
            contact="7788994455"
        )

        assert "Thank you" in self.driver.page_source