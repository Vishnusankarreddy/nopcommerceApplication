from SampleProject.POMPrijectDemo.Locators.locators import Locators


class Loginpage():

    def __init__(self,driver):
        self.driver = driver

        self.username_textbox_id = Locators.username_textbox_id
        self.password_textbox_id = "password"
        self.login_button_id     = "Login"

    def enter_username(self, username):
        self.driver.find_element_by_id(Locators.username_testbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(self.login_button_id).click()