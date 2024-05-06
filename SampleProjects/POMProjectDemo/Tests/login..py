import unittest
import time

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
class LoginTest(unittest.Testcase):

        @classmethod
        def setupclass(cls):
            cls.driver = webdriver.Chrome()
            cls.driver.implicitly_wait(10)
            cls.driver.maximize_window()

        def test_login_valid(self):
            self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
            self.driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
            self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
            self.driver.find_element(By.XPATH, "//button[text()=' Login ']").click()
            self.driver.find_element(By.XPATH, "//span[@class='oxd-userdropdown-tab']").click()
            self.driver.find_element(By.XPATH, "//a[text()='Logout']").click()

        @classmethod
        def tearDoenClass(cls):
            cls.driver.close()
            cls.driver.quit()
            print("Test completed")

if __name__ == '__main__':
    unittest.main()