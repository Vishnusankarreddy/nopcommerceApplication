from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AmazonSearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.ID, 'twotabsearchtextbox')
        self.search_button = (By.ID, 'nav-search-submit-button')

    def search_for_item(self, item_name):
        search_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.search_box))
        search_input.send_keys(item_name)
        self.driver.find_element(*self.search_button).click()
