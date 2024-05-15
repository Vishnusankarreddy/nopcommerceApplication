from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InstagramExplorePage:
    def __init__(self, driver):
        self.driver = driver
        self.explore_button = (By.XPATH, "//span[text()='Explore']")
        self.first_post = (By.XPATH, "//div[@class='_aagw']")

    def explore(self):
        self.driver.find_element(*self.explore_button).click()

    def open_first_post(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.first_post)).click()
