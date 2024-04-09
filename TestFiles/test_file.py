import pytest

from basePackage.BasePo import BasePo
from enums.HeaderMenuItemsEnum import HeaderMenuItemsEnum
from steps.HomeSteps import HomeSteps


@pytest.fixture(scope="class")
def setup(request):
    basePo = BasePo()
    basePo.browser_launch()
    home_steps = HomeSteps(basePo.driver)
    request.cls.home_steps = home_steps
    yield
    basePo.close_browser()

@pytest.mark.usefixtures("setup")
class Test1:
     def test_top_level_menu_accessibility(self):
        self.home_steps.user_lands_on_home_page()
        for item in [HeaderMenuItemsEnum.solutoion, HeaderMenuItemsEnum.whyorangehrm, HeaderMenuItemsEnum.resources, HeaderMenuItemsEnum.company, HeaderMenuItemsEnum.bookafreedemo, HeaderMenuItemsEnum.contactsales]:
            print(item)
