from selenium.webdriver.common.by import By


class AmazonHomePage:
    def __init__(self, driver):
        self.driver = driver

    def search_product(self, keyword):
        search_box = self.driver.find_element(By.ID, "twotabsearchtextbox")
        search_box.send_keys(keyword)
        search_button = self.driver.find_element(By.ID, "nav-search-submit-button")
        search_button.click()
        search_box = self.driver.find_element(By.ID, "twotabsearchtextbox")
        search_box.send_keys(keyword)
        search_button = self.driver.find_element(By.ID, "nav-search-submit-button")
        search_button.click()
        search_box = self.driver.find_element(By.ID, "twotabsearchtextbox")
        search_box.send_keys(keyword)
        search_button = self.driver.find_element(By.ID, "nav-search-submit-button")
        search_button.click()

    def clear_search_bar(self):
        search_box = self.driver.find_element(By.ID, "twotabsearchtextbox")
        search_box.clear()

    def click_first_search_result(self):
        first_result = self.driver.find_element(By.ID, "a-autoid-1-announce")
        first_result.click()
        first_result = self.driver.find_element(By.ID, "a-autoid-7-announce")
        first_result.click()
        first_result = self.driver.find_element(By.ID, "a-autoid-2-announce")
        first_result.click()