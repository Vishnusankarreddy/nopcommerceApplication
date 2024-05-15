import time

from selenium import webdriver

from InstgramProject.Pages.LoginPage import InstagramLoginPage


class InstagramExplorePage:
    pass


class InstagramPOM:
    def __init__(self, driver):
        self.driver = driver
        self.login_page = InstagramLoginPage(self.driver)
        self.explore_page = InstagramExplorePage(self.driver)

    def setup(self):
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

if __name__ == "__main__":
    driver = webdriver.Chrome()
    instagram = InstagramPOM(driver)
    instagram.setup()

    instagram.login_page.load()
    instagram.login_page.login("7032424667", "mishareddy")

    time.sleep(5)

    instagram.explore_page.explore()
    instagram.explore_page.open_first_post()

    time.sleep(5)

    instagram.teardown()