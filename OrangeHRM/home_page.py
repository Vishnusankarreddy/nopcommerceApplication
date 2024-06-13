from selenium.webdriver.common.by import By

class HomePage(BasePage):
    def hover_over_header(self):
        self.hover_over_element(By.XPATH, "//a[text()='Why OrangeHRM']")

    def hover_over_stakeholder(self):
        self.hover_over_element(By.XPATH, "//li[contains(text(),' Stakeholder Solutions')]")

    def click_hr_manager(self):
        self.click(By.XPATH, "//a[text()='IT Manager'][1]")

    def click_book_demo(self):
        self.click(By.XPATH, "//a[contains(text(),'Book a Free Demo')][1]")

    WHY_ORANGEHRM = (By.XPATH, "//a[text()='Why OrangeHRM']")
    STAKEHOLDER_SOLUTIONS = (By.XPATH, "//li[contains(text(),' Stakeholder Solutions')]")
    IT_MANAGER = (By.XPATH, "//a[text()='IT Manager'][1]")

    def __init__(self, driver):
        super().__init__(driver)
        self.action = ActionChains(driver)

    def hover_on_why_orangehrm(self):
        header = self.find_element(*self.WHY_ORANGEHRM)
        self.action.move_to_element(header).perform()

    def hover_on_stakeholder_solutions(self):
        stakeholder = self.find_element(*self.STAKEHOLDER_SOLUTIONS)
        self.action.move_to_element(stakeholder).perform()

    def click_it_manager(self):
        hrmanager = self.find_element(*self.IT_MANAGER)
        self.action.move_to_element(hrmanager).perform()
        hrmanager.click()