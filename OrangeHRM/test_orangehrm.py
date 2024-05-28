# test_orangehrm.py
import time
from selenium import webdriver

from OrangeHRM.becomepartnerpage import BecomePartnerPage
from OrangeHRM.case_studies_page import CaseStudiesPage
from OrangeHRM.home_page import HomePage
from OrangeHRM.partnerspage import PartnersPage
from OrangeHRM.why_orangehrm_page import WhyOrangeHRMPage


def test_case_studies():
    driver = webdriver.Chrome()
    driver.maximize_window()

    home_page = HomePage(driver)
    why_orangehrm_page = WhyOrangeHRMPage(driver)
    case_studies_page = CaseStudiesPage(driver)

    home_page.verify_elements_displayed()
    home_page.click_why_orangehrm()

    why_orangehrm_page.click_our_customers()
    why_orangehrm_page.click_case_studies()

    case_studies_page.verify_case_studies_displayed()

    home_page = HomePage(driver)
    home_page.click_why_orangehrm()

    partners_page = PartnersPage(driver)
    partners_page.click_partners_menu()
    partners_page.click_our_partners()
    partners_page.click_become_a_partner()

    become_partner_page = BecomePartnerPage(driver)
    become_partner_page.fill_form(
        name ="aswain",
        contact ="8899774455",
        email ="guru@gmail.com",
        company_name ="maxmium",
        country ="India",
        partnership_type ="Referral partnership",
        comment ="hello orangeHRM this for testing perpose"
    )

    time.sleep(5)

    driver.quit()

if __name__ == "__main__":
    test_case_studies()
