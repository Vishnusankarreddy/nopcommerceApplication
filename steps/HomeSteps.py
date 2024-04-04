from basePackage.BasePo import driver
from helpers.StepUtiles import StepUtils
from pages.HomePages import HomePage


class HomeSteps:
    def __init__(self):
        self.homepage = HomePage(driver)

    def userLandsOnHomePage(self):
        self.homepage.openLandingPage()

    def clickOnMenuItem(self, item):
        self.homepage.clickOnHeaderMenuButton(item.value)
        StepUtils.addLog("The User clicks on the " + item.name + " button")