from basePackage.BasePo import BasePo
from pages.HomePage import HomePage


class HomeSteps(BasePo):
    def __init__(self, driver):
        self.driver = driver
        self.homepage = HomePage(driver)

    def displayed_on_the_item(self, item_name, xpath):
        element = self.driver.find_element_by_xpath(xpath)
        return element.is_displayed()

    def user_lands_on_home_page(self):
        self.homepage.open_landing_page()
