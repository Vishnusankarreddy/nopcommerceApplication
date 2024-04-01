from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrangeHRMPage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_page(self, url):
        self.driver.get(url)

    def verify_headers_displayed(self, header_xpaths):
        for i, xpath in enumerate(header_xpaths, start=1):
            header_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            )
            assert header_element.is_displayed(), f"Header {i} is not displayed"
        print("All headers are displayed")




# Usage example:
from selenium import webdriver

driver = webdriver.Chrome()
orangehrm_page = OrangeHRMPage(driver)
orangehrm_page.navigate_to_page("https://www.orangehrm.com/")

header_xpaths = [
    "//a[text()='Solutions']",
    "//a[text()='Why OrangeHRM']",
    "//a[text()='Resources']",
    "//a[text()='Company']"
]

orangehrm_page.verify_headers_displayed(header_xpaths)

driver.quit()
