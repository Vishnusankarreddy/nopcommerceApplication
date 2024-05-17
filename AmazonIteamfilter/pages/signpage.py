from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class AmazonSignInPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_input = (By.ID, 'ap_email')
        self.continue_button = (By.ID, 'continue')
        self.password_input = (By.ID, 'ap_password')
        self.sign_in_button = (By.ID, 'signInSubmit')

    def sign_in(self, email, password):
        email_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.email_input))
        email_input.send_keys(str(email))
        self.driver.find_element(*self.continue_button).click()

        password_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.password_input))
        password_input.send_keys(password)
        self.driver.find_element(*self.sign_in_button).click()
