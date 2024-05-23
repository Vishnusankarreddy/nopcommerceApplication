# base_page.py



class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def click(self, *locator):
        self.find_element(*locator).click()

    def is_displayed(self, *locator):
        return self.find_element(*locator).is_displayed()

