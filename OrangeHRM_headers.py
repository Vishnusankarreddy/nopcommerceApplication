from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.orangehrm.com/")

try:
    header_xpaths = [
        "//a[text()='Solutions']",
        "//a[text()='Why OrangeHRM']",
        "//a[text()='Resources']",
        "//a[text()='Company']"
    ]

    for i, xpath in enumerate(header_xpaths, start=1):
        header_element = driver.find_element(By.XPATH, xpath)
        assert header_element.is_displayed(), f"Header {i} is not displayed"

    print("All headers are displayed")
except NoSuchElementException as e:
    print(f"Header not found: {e}")

driver.quit()
