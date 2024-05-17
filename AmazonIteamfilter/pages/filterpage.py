from selenium.webdriver.common.by import By


class AmazonFiltersPage:
    def __init__(self, driver):
        self.driver = driver

    def apply_filters(self):
        brand_filter = (By.XPATH, "//li[@id='p_89/Van Heusen']//i[@class='a-icon a-icon-checkbox']")
        material_filter = (By.XPATH, "//li[@id='p_n_material_browse/1974776031']//i[@class='a-icon a-icon-checkbox']")
        size_filter = (By.XPATH, "//li[@id='p_n_size_browse-vebin/1975396031']//span[@class='a-size-base a-color-base']")

        self.driver.find_element(*brand_filter).click()
        self.driver.find_element(*material_filter).click()
        self.driver.find_element(*size_filter).click()