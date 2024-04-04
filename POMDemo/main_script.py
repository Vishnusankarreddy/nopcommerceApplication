from orangehrm_page import OrangeHRMPage


class WebDriverFactory:
    pass


if __name__ == "__main__":
    driver = WebDriverFactory.create_driver()
    orangehrm_page = OrangeHRMPage(driver)
    orangehrm_page.navigate_to("https://www.orangehrm.com/")
    orangehrm_page.login("admin", "password")
    orangehrm_page.logout()
    driver.quit()
