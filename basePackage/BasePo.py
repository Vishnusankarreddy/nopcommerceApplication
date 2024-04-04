from selenium import webdriver

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


def driver():
    return None