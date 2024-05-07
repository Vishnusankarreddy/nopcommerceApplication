import unittest
from selenium.webdriver.chrome import webdriver


class LoginPage:
    pass


class LoginTest(unittest.TestCase):

        @classmethod
        def setupclass(cls):
            cls.driver = webdriver.Chrome()
            cls.driver.implicitly_wait(10)
            cls.driver.maximize_window()

        def test_login_valid(self):
            driver = self.driver

            driver.get("https://www.facebook.com/")

            login = LoginPage(driver)
            login.enter_username("8106620472")
            login.enter_password("nivya reddy")
            login.click_login()


        @classmethod
        def tearDoenClass(cls):
            cls.driver.close()
            cls.driver.quit()
            print("Test completed")

if __name__ == '__main__':
    unittest.main()