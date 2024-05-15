from selenium.webdriver.common.by import By

class InstagramLoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.instagram.com/"
        self.username_input = (By.XPATH, "//input[@name='username']")
        self.password_input = (By.XPATH, "//input[@type='password']")
        self.login_button = (By.XPATH, "//button[@type='submit']")

    def load(self):
        self.driver.get(self.url)

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()