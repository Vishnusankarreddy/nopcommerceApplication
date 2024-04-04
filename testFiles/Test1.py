import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from basePackage import BasePo
from enums import Enum
from steps.HomeSteps import HomeSteps


class Test1(BasePo):
    def setUp(self):
        self.browser_launch()

    def tearDown(self):
        self.close_browser()

    def test_top_level_menu_accessibility(self):
        home_steps = HomeSteps(self.driver)
        home_steps.user_lands_on_home_page()
        home_steps.click_on_menu_item(Enum.HeaderMenuItemsEnum.OurSolution)
        home_steps.assert_menu_item(Enum.HeaderMenuItemsEnum.OurSolution)
        home_steps.click_on_menu_item(Enum.HeaderMenuItemsEnum.OurStory)
        home_steps.assert_menu_item(Enum.HeaderMenuItemsEnum.OurStory)
        home_steps.click_on_menu_item(Enum.HeaderMenuItemsEnum.WhyTendableWithSpecialCharacter)
        home_steps.assert_menu_item(Enum.HeaderMenuItemsEnum.WhyTendable)

    def test_request_a_demo_button_presence_and_is_active(self):
        home_steps = HomeSteps(self.driver)
        home_steps.user_lands_on_home_page()
        home_steps.click_on_menu_item(Enum.HeaderMenuItemsEnum.OurSolution)
        home_steps.assert_request_demo_button(Enum.HeaderMenuItemsEnum.RequestADemo.value)
        home_steps.click_on_menu_item(Enum.HeaderMenuItemsEnum.OurStory)
        home_steps.assert_request_demo_button(Enum.HeaderMenuItemsEnum.RequestADemo.value)
        home_steps.click_on_menu_item(Enum.HeaderMenuItemsEnum.WhyTendableWithSpecialCharacter)
        home_steps.assert_request_demo_button(Enum.HeaderMenuItemsEnum.RequestADemo.value)

    def test_contact_us_form_submission(self):
        home_steps = HomeSteps(self.driver)
        home_steps.user_lands_on_home_page()
        home_steps.click_on_menu_item(Enum.HeaderMenuItemsEnum.ContactUs)
        home_steps.clicking_on_contact_button()
        home_steps.fill_contact_form(Enum.FormEnum.FullName, Enum.ContactDetailsEnum.FullName)
        home_steps.fill_contact_form(Enum.FormEnum.OrganisationName, Enum.ContactDetailsEnum.OrganisationName)
        home_steps.fill_contact_form(Enum.FormEnum.CellPhone, Enum.ContactDetailsEnum.CellPhone)
        home_steps.fill_contact_form(Enum.FormEnum.Email, Enum.ContactDetailsEnum.Email)
        home_steps.select_job_role_in_drop_down(Enum.JobRoleEnum.Management)
        home_steps.clicking_on_submit_button()
        home_steps.asserting_error_message()

if __name__ == "__main__":
    unittest.main()
