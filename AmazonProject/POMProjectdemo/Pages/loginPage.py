from selenium.webdriver.common.by import By

class AmazonLoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_input = (By.ID, 'ap_email')
        self.button (By.ID, 'continue')
        self.password_input = (By.ID, 'ap_password')
        self.sign_in_submit_button = (By.ID, 'signInSubmit')

    def set_email(self, email):
        self.driver.find_element(*self.email_input).send_keys(email)

    def set_continue(self):
        self.driver.find_element(*self.button).click()

    def set_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_sign_in_submit(self):
        self.driver.find_element(*self.sign_in_submit_button).click()





class AmazonProductPage:

    def __init__(self, driver):
        self.driver = driver
        self.add_to_cart_button = (By.ID, 'add-to-cart-button')

    def click_add_to_cart(self):
        self.driver.find_element(*self.add_to_cart_button).click()