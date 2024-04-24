import pytest
import time
from selenium.webdriver.chrome import webdriver
from POMDemo.login_test import LoginPage

from selenium import webdriver

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_login(driver):
    login_page = LoginPage(driver)
    login_page.open_page("https://www.facebook.com/")
    time.sleep(1)
    login_page.enter_username("8106620472")
    time.sleep(1)
    login_page.enter_password("nivya reddy")
    time.sleep(1)
    login_page.click_login()
    time.sleep(5)
