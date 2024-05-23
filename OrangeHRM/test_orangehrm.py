# test_orangehrm.py
import time
from selenium import webdriver

from OrangeHRM.case_studies_page import CaseStudiesPage
from OrangeHRM.home_page import HomePage
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

    time.sleep(5)

    driver.quit()

if __name__ == "__main__":
    test_case_studies()
