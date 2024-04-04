from selenium.webdriver.common.by import By

class OrangeHRMPage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to(self, url):
        self.driver.get(url)

    def login(self, username, password):
        username_field = self.driver.find_element(By.ID, "txtUsername")
        password_field = self.driver.find_element(By.ID, "txtPassword")
        login_button = self.driver.find_element(By.ID, "btnLogin")

        username_field.clear()
        username_field.send_keys(username)

        password_field.clear()
        password_field.send_keys(password)

        login_button.click()

    def logout(self):
        welcome_menu = self.driver.find_element(By.ID, "welcome")
        welcome_menu.click()
        logout_link = self.driver.find_element(By.LINK_TEXT, "Logout")
        logout_link.click()
