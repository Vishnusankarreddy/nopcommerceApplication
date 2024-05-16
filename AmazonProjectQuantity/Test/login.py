import time

from selenium import webdriver

from AmazonProjectQuantity.pages.LoginPage import AmazonLoginPage
from AmazonProjectQuantity.pages.homepage import AmazonHomePage

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)

    login_page = AmazonLoginPage(driver)
    login_page.open()
    login_page.login("7032424667", "Vishnu@123")

    home_page = AmazonHomePage(driver)
    home_page.search("pen")
    home_page.filter_results()

    time.sleep(5)  # Adding a delay for demonstration purposes
    driver.quit()