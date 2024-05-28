from selenium.webdriver.common.by import By

from OrangeHRM.base_page import BasePage


class PartnersPage(BasePage):
    PARTNERS_MENU = (By.XPATH, "//li[contains(text(),'Partners')]")
    OUR_PARTNERS_LINK = (By.XPATH, "//a[text()='Our Partners']/parent::h6")
    BECOME_A_PARTNER_LINK = (By.XPATH, "//a[contains(text(),'Become a Partner')]")

    def __init__(self, driver):
        super().__init__(driver)

    def click_partners_menu(self):
        self.click(self.PARTNERS_MENU)

    def click_our_partners(self):
        self.click(self.OUR_PARTNERS_LINK)

    def click_become_a_partner(self):
        self.click(self.BECOME_A_PARTNER_LINK)
