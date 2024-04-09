from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class BasePo:
    driver = None

    @classmethod
    def browser_launch(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    @classmethod
    def close_browser(cls):
        if cls.driver:
            cls.driver.quit()
            cls.driver = None