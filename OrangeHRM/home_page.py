from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    WHY_ORANGEHRM_LINK = (By.XPATH, "//a[text()='Why OrangeHRM?']")

    def __init__(self, driver):
        super().__init__(driver)

    def click_why_orangehrm(self):
        self.click(self.WHY_ORANGEHRM_LINK)



        self.header = (By.XPATH, "//a[text()='Why OrangeHRM']")
        self.stakeholder = (By.XPATH, "//li[contains(text(),' Stakeholder Solutions')]")
        self.hr_manager = (By.XPATH, "//a[text()='IT Manager'][1]")
        self.book_demo = (By.XPATH, "//a[contains(text(),'Book a Free Demo')][1]")


    def hover_over_header(self):
        self.hover_over_element(*self.header)

    def hover_over_stakeholder(self):
        self.hover_over_element(*self.stakeholder)

    def click_hr_manager(self):
        self.hover_over_element(*self.hr_manager)
        self.click_element(*self.hr_manager)

    def click_book_demo(self):
        self.click_element(*self.book_demo)