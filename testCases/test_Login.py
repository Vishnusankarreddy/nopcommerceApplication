import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage

class Test_001_Login:
    baseURl = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"

    def test_homePageTitle(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURl)
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Your store. Login":
            assert True
        else:
            assert False

    def test_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        self.driver.close()
        if act_title =="Dashboard / nopCommerce administration":
            assert True
        else:
            assert False

