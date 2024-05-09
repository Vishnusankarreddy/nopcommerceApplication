from selenium.webdriver.common.by import By


class AmazonHomePage:
    def __init__(self, driver):
        self.driver = driver

    def search_product(self, keyword):
        search_box = self.driver.find_element(By.ID, "twotabsearchtextbox")
        search_box.send_keys(keyword)
        search_button = self.driver.find_element(By.ID, "nav-search-submit-button")
        search_button.click()

    def click_first_search_result(self):
        first_result = self.driver.find_element(By.ID, "a-autoid-1-announce")
        first_result.click()


class AmazonCartPage:
    def __init__(self, driver):
        self.driver = driver

    def delete_item_from_cart(self):
        delete_button = self.driver.find_element(By.XPATH, "//input[@title='Delete']")
        delete_button.click()