from selenium.webdriver.common.by import By


import unittest

class LoginTest(unittest.TestCase):

    def __init__(self, driver):
        self.driver = driver

        self.username_testbox_id = "email"
        self.password_textbox_id = "pass"
        self.login_button_name = "login"

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_testbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_id(self.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_name(self.login_button_name).click()