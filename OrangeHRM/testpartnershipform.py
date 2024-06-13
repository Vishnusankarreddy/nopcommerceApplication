from selenium.webdriver.common.by import By

class TestOrangeHRM:
    def setup_method(self, method):
        self.driver = ...
        self.home_page = HomePage(self.driver)

    def teardown_method(self):
        self.driver.quit()

    def test_example(self):
        assert self.home_page.some_method() == expected_value
    def test_case_studies(self):
        self.driver.get("https://www.orangehrm.com/")
        self.home_page.hover_over_header()
        self.home_page.hover_over_stakeholder()
        self.home_page.click_hr_manager()

    def test_case_header(self):
        self.driver.get("https://www.orangehrm.com/")
        self.home_page.hover_over_header()
        self.home_page.hover_over_stakeholder()
        self.home_page.click_hr_manager()
        self.home_page.click_book_demo()
        self.home_page.send_keys(By.XPATH, "//input[@id='Form_getForm_FullName']", "vishnureddy")
        self.home_page.send_keys(By.XPATH, "//input[@id='Form_getForm_Email']", "bussiness99@gmail.com")
        self.home_page.send_keys(By.XPATH, "//input[@id='Form_getForm_CompanyName']", "goldfeild")
        self.home_page.click(By.XPATH, "//select[@id='Form_getForm_Country']")
        self.home_page.click(By.XPATH, "//option[@value='India']")
        self.home_page.send_keys(By.XPATH, "//input[@id='Form_getForm_Contact']", "7788994455")
        self.home_page.click(By.XPATH, "//input[@id='Form_getForm_action_submitForm']")

    home_page = HomePage(driver)
    home_page.hover_on_why_orangehrm()
    home_page.hover_on_stakeholder_solutions()
    home_page.click_it_manager()

    demo_page = DemoPage(driver)
    demo_page.book_free_demo("vishnureddy", "bussiness99@gmail.com", "goldfeild", "7788994455")