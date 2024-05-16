from selenium.webdriver.common.by import By


class AmazonHomePage:
    def __init__(self, driver):
        self.driver = driver
        self.search_textbox = (By.XPATH, "//input[@id='twotabsearchtextbox']")
        self.search_button = (By.XPATH, "//input[@id='nav-search-submit-button']")
        self.filter_button = (By.XPATH, "//button[@id='a-autoid-3-announce']")
        self.filter_dropdown = (By.XPATH, "(//span[@class='a-dropdown-prompt'])[2]")
        self.filter_option = (By.XPATH, "//span[@data-action='a-dropdown-button'] [1]")
        self.filter_value = (By.XPATH, "//input[@value='5']")
        self.delete_filter = (By.XPATH, "//input[@title='Delete']")

    def search(self, keyword):
        self.driver.find_element(*self.search_textbox).send_keys(keyword)
        self.driver.find_element(*self.search_button).click()

    def filter_results(self):
        self.driver.find_element(*self.filter_button).click()
        self.driver.find_element(*self.filter_dropdown).click()
        self.driver.find_element(*self.filter_option).click()
        self.driver.find_element(*self.filter_value).click()
        self.driver.find_element(*self.delete_filter).click()