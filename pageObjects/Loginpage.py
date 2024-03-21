class Login:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[@class='button-1 login-button']"
    link_Logout_linktext = "Logout"

    def __int__(self,driver):
        self.drive = driver

    def setUserName(self,username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).sendkeys(username)

    def setPassword(self,password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).sendkeys(password)

    def clickLogin(self):
        self.driver.find_element_by_id(self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_id(self.  link_Logout_linktext).click()
