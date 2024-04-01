import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

class BasePage:
    def __init__(self, driver):
        self.driver = driver

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://www.orangehrm.com/")

    def navigate_to_free_demo(self):
        demo_button = self.driver.find_element(By.XPATH, "//div[@class='d-flex web-menu-btn']//button[text()='Book a Free Demo']")
        demo_button.click()

class DemoFormPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def fill_demo_form(self, full_name):
        full_name_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='Form_getForm_FullName']")))
        full_name_field.send_keys(full_name)
        submit_button = self.driver.find_element(By.XPATH, "//input[@id='Form_getForm_action_submitForm']")
        submit_button.click()

def main():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)

    try:
        home_page = HomePage(driver)
        home_page.navigate_to_free_demo()

        demo_page = DemoFormPage(driver)
        demo_page.fill_demo_form("vishnu")

        # Add assertions or further test steps if needed

        time.sleep(9)

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
