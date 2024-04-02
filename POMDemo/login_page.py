import time

import pytest
from selenium import webdriver
from POMDemo.login_test import LoginPage

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.close()

def test_login(driver):
    login_page = LoginPage(driver)
    login_page.open_page("https://www.facebook.com/")
    time.sleep(2)
    login_page.enter_username("8106620472")
    time.sleep(2)
    login_page.enter_password("nivya reddy")
    time.sleep(2)
    login_page.click_login()
    time.sleep(2)
