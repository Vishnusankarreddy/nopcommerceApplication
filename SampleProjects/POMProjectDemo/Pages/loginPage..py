from selenium.webdriver.common.by import By


class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.username_testbox_xpath = "//input[@name='username']"
        self.password_textbox_xpath = "//input[@name='password']"
        self.login_button_xpath = "//button[text()=' Login ']"

    def enter_username(self, username):
        self.driver.find_element(By.XPATH, (self.username_testbox_xpath)).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, (self.password_textbox_xpath)).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, (self.login_button_xpath)).click()