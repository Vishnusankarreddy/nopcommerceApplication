from selenium.webdriver.common.by import By


class AmazonLoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.amazon.in/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26useRedirectOnSuccess%3D1%26signIn%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0"
        self.email_textbox = (By.XPATH, "//input[@id='ap_email']")
        self.continue_button = (By.XPATH, "//input[@id='continue']")
        self.password_textbox = (By.XPATH, "//input[@id='ap_password']")
        self.signin_button = (By.XPATH, "//input[@id='signInSubmit']")

    def open(self):
        self.driver.get(self.url)

    def login(self, email, password):
        self.driver.find_element(*self.email_textbox).send_keys(email)
        self.driver.find_element(*self.continue_button).click()
        self.driver.find_element(*self.password_textbox).send_keys(password)
        self.driver.find_element(*self.signin_button).click()