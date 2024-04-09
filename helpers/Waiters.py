from telnetlib import EC
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from basePackage.BasePo import BasePo


class Waiters(BasePo):
    timeout_in_seconds = 10

    @staticmethod
    def wait_with_sleep_timeout():
        sleep(5)  # Sleep for 5 seconds

    @staticmethod
    def wait_for_element_to_be_displayed(locator):
        WebDriverWait(Waiters.driver, Waiters.timeout_in_seconds).until(EC.visibility_of_element_located(locator))
