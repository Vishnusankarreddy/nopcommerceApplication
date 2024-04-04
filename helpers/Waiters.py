from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from basePackage.BasePo import driver

class Waiters:
    timeoutInSeconds = 10
    wait = WebDriverWait(driver, timeoutInSeconds)

    @staticmethod
    def waitWithSleepTimeout():
        import time
        time.sleep(3)

    @staticmethod
    def waitForElementToBeDisplayed(locator):
        Waiters.wait.until(EC.visibility_of_element_located(locator))

    @staticmethod
    def waitForElementToBeVisible(locator):
        Waiters.wait.until(EC.visibility_of_element_located(locator))

    @staticmethod
    def waitForElementToBeClickable(locator):
        Waiters.wait.until(EC.element_to_be_clickable(locator))



