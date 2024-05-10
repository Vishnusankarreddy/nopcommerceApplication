
from selenium.webdriver.common.by import By

class AmazonSignInPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_email(self, email):
        email_input = self.driver.find_element(By.ID, "ap_email")
        email_input.send_keys(email)

    def click_continue(self):
        continue_button = self.driver.find_element(By.ID, "continue")
        continue_button.click()

    def enter_password(self, password):
        password_input = self.driver.find_element(By.ID, "ap_password")
        password_input.send_keys(password)

    def click_sign_in(self):
        sign_in_button = self.driver.find_element(By.ID, "signInSubmit")
        sign_in_button.click()

class AmazonHomePage:
    def __init__(self, driver):
        self.driver = driver

    def search_product(self, keyword):
        search_box = self.driver.find_element(By.ID, "twotabsearchtextbox")
        search_box.send_keys(keyword)
        search_button = self.driver.find_element(By.ID, "nav-search-submit-button")
        search_button.click()
        search_box = self.driver.find_element(By.ID, "twotabsearchtextbox")
        search_box.send_keys(keyword)
        search_button = self.driver.find_element(By.ID, "nav-search-submit-button")
        search_button.click()
        search_box = self.driver.find_element(By.ID, "twotabsearchtextbox")
        search_box.send_keys(keyword)
        search_button = self.driver.find_element(By.ID, "nav-search-submit-button")
        search_button.click()


    def clear_search_bar(self):
        search_box = self.driver.find_element(By.ID, "twotabsearchtextbox")
        search_box.clear()


    def click_first_search_result(self):
        first_result = self.driver.find_element(By.ID, "a-autoid-1-announce")
        first_result.click()
        first_result = self.driver.find_element(By.ID, "a-autoid-7-announce")
        first_result.click()
        first_result = self.driver.find_element(By.ID, "a-autoid-2-announce")