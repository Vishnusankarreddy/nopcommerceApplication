from selenium import webdriver
import time
import unittest

from POMDemo.pages.login_page import LoginPage
from SampleProject.POMPrijectDemo.Pages.homePage import HomePage


class LoginTest(unittest.TestCase):
   @classmethod
   def setupClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.close()
        cls.driver.quit()

   def test_login_valid(self):
        driver = self.driver

        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()



        homepage = HomePage(driver)
        homepage.click_Zenon_e_Pesado()
        homepage.click_logout()
        time.sleep(2)

   @classmethod
   def tearDownclass(cls):
       cls.driver.close()
       cls.driver.quit()
       print("Test completed")

if __name__ == '__main__':
    unittest.main()



