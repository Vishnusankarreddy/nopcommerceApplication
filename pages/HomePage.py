from argparse import Action

from selenium.webdriver.common.by import By

from helpers.DataRroviders import DataProviders
from helpers.Waiters import Waiters


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def headerItem(self, itemName):
        return By.text(itemName)

    def contactForm(self, formname):
        return By.name(formname)

    def openLandingPage(self):
        self.driver.get(DataProviders.getUrlTestData("https://www.orangehrm.com"))

    def getCurrentUrl(self):
        return self.driver.current_url

    def clickOnHeaderMenuButton(self, itemName):
        locator = By.link_text(itemName)
        Waiters.waitForElementToBeDisplayed(locator)
        Action.clickByLocator(locator, 0)